from typing import Optional, List

from ytmusicapi.ytmusic import YTMusic
from pytube import YouTube
from app.usefull.functions import feat_finder
import re

ytm = YTMusic()


class MusicTrack:
    def __init__(self, track_id=None, search_result=0, downloaded=0, title=None,
                 artists=None, album=None, release_year=None, total_tracks=0,
                 track_number=0, genre=None, cover_art=None, lyrics=None):
        """

        :param track_id:
        :param search_result: 1 if should be downloaded, 0 if should not be downloaded, 2 cant find with YTM
        :param downloaded:
        :param title:
        :param artists:
        :param album:
        :param release_year:
        :param total_tracks:
        :param track_number:
        :param genre:
        :param cover_art:
        :param lyrics:
        """

        self.__id: str = track_id
        self.__search_result: int = search_result
        self.__downloaded: int = downloaded
        self.__title: str = title
        ft = feat_finder(self.__title)
        self.feats = ft if ft else ''
        if artists:
            res_artists = []
            for artist in artists:
                artist = re.sub(' feat.', ',', artist).replace('&', ',')
                for art in artist.split(','):
                    art = re.sub('The Black Eyed Peas', 'Black Eyed Peas', art)
                    art = re.sub('[Гг]руппа', '', art)
                    art = re.sub('30 Seconds To Mars', 'Thirty Seconds to Mars', art)
                    art = art.replace('"', '').replace('$', 's')
                    art = re.sub(" +", ' ', art).strip()
                    if art not in res_artists:
                        res_artists.append(art)
            for artist in re.split(r'[,&]', re.sub(r'[()]', '', self.feats.replace('feat.', ''))):
                artist = artist.replace('$', 's')
                if artist not in res_artists and artist != '':
                    res_artists.append(artist.strip())
        else:
            res_artists = []
        self.original_artists: list = artists if artists else None
        self.__artists: list = res_artists
        self.__album: str = album
        self.__release_year: str = release_year
        self.__total_tracks: int = total_tracks
        self.__track_number: int = track_number
        self.__genre: str = genre
        self.__cover_art: str = cover_art
        self.__lyrics: str = lyrics

    id: str = property(lambda self: self.__id)
    downloaded: int = property(lambda self: self.__downloaded)
    title: str = property(lambda self: self.__title.strip())
    album: str = property(lambda self: str(self.__album).strip() if self.__album else None)
    artists: str = property(lambda self: self.artists)
    artist: str = property(lambda self: ', '.join(self.artists))
    release_year: int = property(lambda self: self.__release_year)
    total_tracks: int = property(lambda self: self.__total_tracks)
    track_number: int = property(lambda self: self.__track_number)
    genre: str = property(lambda self: self.__genre)
    cover_art: str = property(lambda self: self.__cover_art)
    lyrics: str = property(lambda self: self.__lyrics)
    title_without_feat: str = property(lambda self: self.__title.replace(f'{self.feats}', '').strip())

    @property
    def search_result(self):
        return self.__search_result

    @search_result.setter
    def search_result(self, result):
        self.__search_result = result

    @staticmethod
    def normalized(raw_string: str) -> str:
        res = re.sub(r'[(][^(]+?[)]', '', raw_string)
        while raw_string != res:
            raw_string = res
            res = re.sub(r'[(][^(]+?[)]', '', raw_string)
        res = re.sub(r'[\[][^\[]+?[]]', '', res)
        while raw_string != res:
            raw_string = res
            res = re.sub(r'[\[][^\[]+?[]]', '', res)
        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
        return res

    @staticmethod
    def soft_normalized(raw_str: str):
        res = re.sub(r'[(].*?[)]', '', raw_str)
        while raw_str != res:
            raw_str = res
            res = re.sub(r'[(].*?[)]', '', raw_str)
        return res


    def get(self):
        return (self.id, self.search_result, self.downloaded, self.title,
                ', '.join(self.artists), self.album, self.release_year,
                self.total_tracks, self.track_number, self.genre, self.cover_art, self.lyrics)

    def __str__(self):
        return self.title + ' -|- ' + ', '.join(self.original_artists) + ' -|- ' + self.album


class YouTubeMusicTrack(MusicTrack):
    def __init__(self, track: dict):
        super().__init__(track_id=track['videoId'], title=track['title'],
                         artists=[artist['name'] for artist in track['artists']] if track['artists'] else ['Unknown'],
                         album=track['album']['name'] if track['album'] else None,
                         cover_art=track['thumbnails'][-1]['url'])


class YouTubeTrack(MusicTrack):
    def __init__(self, video: YouTube):
        meta_album = None
        self.__meta_name = None
        self.__meta_artist = None

        if len(video.metadata.metadata):
            meta = video.metadata.metadata[0]
            self.__meta_name = meta.get("Song")
            self.__meta_artist = meta.get("Artist")
            meta_album = meta.get("Album")

        artist = video.author
        if self.__meta_artist is not None:
            if video.title.lower().find(self.__meta_artist.lower()) != -1:
                artist = self.__meta_artist

        super().__init__(track_id=video.video_id, title=video.title, artists=artist.split(','), album=meta_album)

    meta_name: str = property(lambda self: self.__meta_name)
    meta_artist: str = property(lambda self: self.__meta_artist)

    @property
    def get_meta_artists(self):
        res = []
        artists = [re.split(r'[,&]', artist) for artist in self.meta_artist.split(',')]
        for i in range(len(artists)):
            for elem in artists[i]:
                res.append(self.normalized(elem))

        return set(res)

    def get_music_tracks(self) -> List[MusicTrack]:
        """
        need to be fixed!

        Возвращает список треков приведенных к типу MusicTrack.\n
        Если при поиске нашелся тот же id то вернет список из 1 объекта [ytm_track].\n
        Если при поиске нашелся другой id то вернет список из 2 объектов [yt_track, ytm_track].\n
        Если поиск авершился с ошибкой то вернет список из 1 объекта [yt_track].

        :return: list[MusicTrack]
        """
        ytm_track = self.__search_yt_track_on_ytm()
        res = []
        if ytm_track is not None:
            if self.id == ytm_track.id:
                ytm_track.search_result = 1
                res.append(ytm_track)
            else:
                self.search_result = 0
                res.append(self)
                ytm_track.search_result = 1
                res.append(ytm_track)
        else:
            self.search_result = 2
            res.append(self)
        return res

    def __search_yt_track_on_ytm(self) -> Optional[YouTubeMusicTrack]:
        """
        Возвращает YouTubeMusicTrack, если трек найден на YTMusic, иначе None

        :return: Optional[YouTubeMusicTrack]
        """
        ytm_track = self.__find_ytm('id')
        if ytm_track is None:
            ytm_track = self.__find_ytm('name')
        if ytm_track is None:
            ytm_track = self.__find_ytm('meta')
        if ytm_track is None:
            return
        else:
            return ytm_track

    def __find_ytm(self, key='') -> Optional[YouTubeMusicTrack]:
        tracks = None
        if key == 'id':
            tracks = ytm.search(self.id, filter='songs', limit=1, ignore_spelling=True)
        elif key == 'name':
            tracks = ytm.search(self.title + ' ' + self.artist, filter='songs', limit=1)
        elif key == 'meta':
            title = self.meta_name if self.meta_name else self.title
            artist = self.meta_artist if self.meta_artist else self.artist
            tracks = ytm.search(title + ' ' + artist, filter='songs', limit=1)

        if tracks:
            ytm_track = YouTubeMusicTrack(tracks[0])
            if ytm_track.id == self.id:  # found track has the same ID
                return ytm_track
            if self.__has_same_title(ytm_track) and self.__has_same_artist(ytm_track):
                return ytm_track
        return

    def __is_contains_artist(self, artists: set):
        for artist in artists:
            if self.normalized(self.title).find(artist) != -1:
                return True
        return False

    def __has_same_title(self, ytm_track: YouTubeMusicTrack):
        ytm_title = ytm_track.normalized(ytm_track.title)
        if self.normalized(self.title).find(ytm_title) != -1:
            return True
        if self.meta_name is not None:
            if self.normalized(self.meta_name).find(ytm_title) != -1:
                return True
        return False

    def __has_same_artist(self, ytm_track: YouTubeMusicTrack):
        ytm_artists = set(ytm_track.artists)
        yt_artists = set(self.artists)

        if not yt_artists.isdisjoint(ytm_artists):
            return True

        if self.meta_artist is not None:
            yt_meta_artist = self.get_meta_artists
            if not yt_meta_artist.isdisjoint(ytm_artists):
                return True
            for ytm_artist in ytm_artists:
                for yt_artist in yt_meta_artist:
                    if self.normalized(yt_artist).find(ytm_artist) != -1:
                        return True
        if self.__is_contains_artist(ytm_artists):
            return True

        for ytm_artist in ytm_artists:
            for yt_artist in yt_artists:
                if self.normalized(yt_artist).find(ytm_artist) != -1:
                    return True
        return False
