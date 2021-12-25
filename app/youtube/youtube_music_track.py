from pytube import YouTube
from pytube.exceptions import VideoUnavailable

from app.database.db_track import DBTrack
from app.usefull.functions import normalized, artist_splitter_runtime, calc_duration, feat_finder, artist_splitter, \
    artist_fixer

SEP = ' -|- '


class YouTubeMusicTrack:
    def __init__(self, track: dict):
        # print(track)
        self.is_available: bool = track['isAvailable']
        self.track_id: str = track['videoId'] if track['videoId'] else ''
        self.title: str = track['title']
        self.artists: list = track['artists']  # 'artists': [{'name': 'STARSET', 'id': 'UCzYd1EYoMbG8tFWQ69Odi4Q'}]
        self.album: str = str(track['album']['name']) if track['album'] else ''
        self.album_id: str = str(track['album']['id']) if track['album'] else ''
        self.cover_art: str = track['thumbnails'][-1]['url']
        try:
            self.duration: int = calc_duration(track['duration'])
        except KeyError:
            self.duration: int = 0
        self.meta_name: str = ''
        self.meta_artist: str = ''

    def get_artists_names(self):
        return [artist['name'] for artist in self.artists]

    def get_artists_names_str(self):
        return ', '.join(self.get_artists_names())

    def get_artists_ids(self):
        return [artist['id'] for artist in self.artists]

    def get_artist_info_tmp(self):
        res = [(artist['id'], artist['name']) for artist in self.artists]
        return ', '.join([str(e) for e in res])

    def get_meta_data(self):
        if not self.meta_name and not self.meta_artist:
            self.set_meta_data()
        return (self.meta_name + ' ' + self.meta_artist).strip()

    def set_meta_data(self):
        if not self.track_id:
            return
        try:
            yt = YouTube('https://www.youtube.com/watch?v=' + self.track_id)
        except VideoUnavailable:  # VideoUnavailable
            return
        except KeyError:  # video was deleted
            return
        else:
            try:
                meta = yt.metadata.metadata[0]
            except IndexError:  # video has no meta data
                return
            else:
                meta_name = meta.get("Song")
                meta_artist = meta.get("Artist")
                meta_album = meta.get("Album")
                self.meta_name = meta_name if meta_name else self.title
                self.meta_artist = meta_artist if meta_artist else self.get_artists_names_str()

    def is_equal(self, other):
        """
        Проверяет что результат поиска и входной трек имеют схожую метадату
        :param other: резльтат поиска
        :return: True if is_equal else False
        """
        if self == other:  # found track has the same ID
            return True
        return self.has_same_title(other) and self.has_same_artist(other)

    def has_same_title(self, other):  # todo
        n_yt = normalized(self.meta_name) if self.meta_name else normalized(self.title)
        n_ytm = normalized(other.title)
        if n_yt.find(n_ytm) != -1 or n_ytm.find(n_yt) != -1:
            return True
        return False

    def has_same_artist(self, other):  # todo
        if not set(self.get_artists_ids()).isdisjoint(set(other.get_artists_ids())):
            return True
        if not self.meta_artist:
            yt_artists = set(artist_splitter_runtime(self.get_artists_names()))
        else:
            yt_artists = set(artist_splitter_runtime(self.meta_artist.split(',')))

        ytm_artists = set(artist_splitter_runtime(other.get_artists_names()))

        if not yt_artists.isdisjoint(ytm_artists):
            return True

        if self._contains_artist(ytm_artists):
            return True

        for ytm_artist in ytm_artists:
            norm_ytm_art = normalized(ytm_artist)
            for yt_artist in yt_artists:
                if normalized(yt_artist).find(norm_ytm_art) != -1:
                    return True
        return False

    def _contains_artist(self, artists: set):  # todo
        for artist in artists:
            if normalized(self.title).find(normalized(artist)) != -1:
                return True
        return False

    def __eq__(self, other):
        return self.track_id == other.track_id

    def get_info(self):
        return self.track_id + SEP + self.title + SEP + self.get_artist_info_tmp() + SEP + '(' + self.album \
               + ' - ' + self.album_id + ')' + SEP + str(self.duration)
        # return self.album + ' - ' + self.album_id + ' ' + self.cover_art

    def __str__(self):
        return self.track_id + SEP + self.title + SEP + self.get_artists_names_str() + SEP + self.album \
               + SEP + str(self.duration)

    def to_db_track(self, state):  # todo
        norm_title = self.title.replace('[', '(').replace(']', ')')
        feat = feat_finder(norm_title)
        if feat != '':
            title = norm_title.replace(feat, '').strip()
            feat_arts = feat.replace('feat.', '')[1:-1]
        else:
            title = norm_title
            feat_arts = ''
        return DBTrack(track_id=self.track_id,
                       state=state,
                       title=title,
                       artists=', '.join(artist_splitter(artist_fixer(self.get_artists_names()) + [feat_arts])),
                       album=self.album,
                       cover_art=self.cover_art)
