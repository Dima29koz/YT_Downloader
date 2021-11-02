from typing import Optional, List
from ytmusicapi.ytmusic import YTMusic
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

from youtube_playlist_downloader.youtube.youtube_track import YouTubeMusicTrack
from youtube_playlist_downloader.database.db_track import DBTrack
from youtube_playlist_downloader.usefull.functions import normalized, artist_splitter_runtime
from youtube_playlist_downloader.usefull.exceptions import SearchingError

ytm = YTMusic()


class YTMSearcher:
    def __init__(self, original_track: YouTubeMusicTrack):
        self.yt_track = original_track
        self.meta_name = None
        self.meta_artist = None

    def ytm_search_result(self) -> List[DBTrack]:
        """

        Возвращает список треков приведенных к типу DBTrack.\n
        Если при поиске нашелся тот же id то вернет список из 1 объекта [ytm_track].\n
        Если при поиске нашелся другой id то вернет список из 2 объектов [yt_track, ytm_track].\n
        Если поиск завершился с ошибкой то вернет список из 1 объекта [yt_track].

        :return: list[MusicTrack]
        """
        if self.__duration():
            return [self.yt_track.to_db_track(state=3)]
        ytm_track = self.__ytm_searching()
        res = []
        if self.yt_track.is_available:
            if ytm_track is not None:
                if self.yt_track.track_id == ytm_track.track_id:
                    res.append(ytm_track.to_db_track(state=1))
                else:
                    res.append(self.yt_track.to_db_track(state=0))
                    res.append(ytm_track.to_db_track(state=1))
            else:
                res.append(self.yt_track.to_db_track(state=2))
        else:
            if ytm_track is not None:
                res.append(ytm_track.to_db_track(state=1))
            else:
                raise SearchingError

        return res

    def __duration(self):
        """
        Возвращает True если длина трека >=14 минут
        """
        if self.yt_track.duration:
            time = self.yt_track.duration.split(':')
            if len(time) == 2 and int(time[-2]) >= 14:
                return True
            if len(time) == 3:
                return True
        return False

    def __ytm_searching(self) -> Optional[YouTubeMusicTrack]:
        """
        Возвращает результат поиска на YouTubeMusic

        :return: YouTubeMusicTrack or None
        """
        # print('►', self.yt_track)

        if self.yt_track.is_available:
            ytm_track = self.__find_ytm('id')
            if ytm_track and self.__is_equal(ytm_track):
                return ytm_track

        ytm_track = self.__find_ytm('name')
        if ytm_track and self.__is_equal(ytm_track):
            return ytm_track

        ytm_track = self.__find_ytm('no_art')
        if ytm_track and self.__is_equal(ytm_track):
            return ytm_track

        if self.yt_track.is_available:
            self.meta_name, self.meta_artist = get_meta_data(self.yt_track.track_id)
            ytm_track = self.__find_ytm('meta')
            if ytm_track and self.__is_equal(ytm_track):
                return ytm_track
        return None

    def __is_equal(self, ytm_track: YouTubeMusicTrack):
        """
        Проверяет что результат поиска соответствует запросу
        :param ytm_track: резльтат поиска
        :return: True if is_equal else False
        """
        if ytm_track.track_id == self.yt_track.track_id:  # found track has the same ID
            # print('◀', ytm_track)
            return True
        if self.__has_same_title(ytm_track):
            if self.__has_same_artist(ytm_track):
                # print('◀', ytm_track)
                return True
        # print('◁', ytm_track)
        return False

    def __find_ytm(self, key='') -> Optional[YouTubeMusicTrack]:
        tracks = None
        title = self.yt_track.title.replace('"', '')
        if key == 'id':
            tracks = ytm.search(self.yt_track.track_id,
                                filter='songs', limit=1, ignore_spelling=True)
        elif key == 'name':
            tracks = ytm.search(title + ' ' + self.yt_track.artist,
                                filter='songs', limit=1)
        elif key == 'no_art':
            tracks = ytm.search(title,
                                filter='songs', limit=1)
        elif key == 'meta':
            title = self.meta_name if self.meta_name else title
            artist = self.meta_artist if self.meta_artist else self.yt_track.artist
            tracks = ytm.search(title + ' ' + artist,
                                filter='songs', limit=1)

        if tracks:
            ytm_track = YouTubeMusicTrack(tracks[0])
            return ytm_track  # smth found
        else:
            return None

    def __is_contains_artist(self, artists: set):
        for artist in artists:
            if normalized(self.yt_track.title).find(normalized(artist)) != -1:
                return True
        return False

    def __has_same_title(self, ytm_track: YouTubeMusicTrack):
        if self.meta_name is None:
            n_yt = normalized(self.yt_track.title)
        else:
            n_yt = normalized(self.meta_name)
        n_ytm = normalized(ytm_track.title)
        if n_yt.find(n_ytm) != -1:
            return True
        if n_ytm.find(n_yt) != -1:
            return True
        return False

    def __has_same_artist(self, ytm_track: YouTubeMusicTrack):
        if not set(self.yt_track.artist_ids).isdisjoint(set(ytm_track.artist_ids)):
            return True
        if self.meta_artist is None:
            yt_artists = set(artist_splitter_runtime(self.yt_track.artists_list))
        else:
            yt_artists = set(artist_splitter_runtime(self.meta_artist.split(',')))

        ytm_artists = set(artist_splitter_runtime(ytm_track.artists_list))

        if not yt_artists.isdisjoint(ytm_artists):
            return True

        if self.__is_contains_artist(ytm_artists):
            return True

        for ytm_artist in ytm_artists:
            norm_ytm_art = normalized(ytm_artist)
            for yt_artist in yt_artists:
                if normalized(yt_artist).find(norm_ytm_art) != -1:
                    return True
        return False


def get_meta_data(yt_track_id: str):
    try:
        yt = YouTube('https://www.youtube.com/watch?v='+yt_track_id)
    except VideoUnavailable:
        print(yt_track_id + ' VideoUnavailable')
        return None, None
    except KeyError:
        print(yt_track_id + ' video was deleted')
        return None, None
    else:
        try:
            meta = yt.metadata.metadata[0]
            meta_name = meta.get("Song")
            meta_artist = meta.get("Artist")
            return meta_name, meta_artist
        except IndexError:
            # video has no meta data
            return None, None


def playlist_getter(playlist_id: str):
    playlist = ytm.get_playlist(playlist_id, limit=2000)
    for track in playlist['tracks']:
        yield YouTubeMusicTrack(track)
