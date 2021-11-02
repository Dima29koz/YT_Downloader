from pytube import YouTube
from pytube.exceptions import VideoUnavailable

from app.usefull.functions import normalized, artist_splitter_runtime

SEP = ' -|- '


class YouTubeMusicTrack:
    def __init__(self, track: dict):
        self.is_available: bool = track['isAvailable']
        self.track_id: str = track['videoId'] if track['videoId'] else ''
        self.title: str = track['title']
        self.artists: list = track['artists']  # 'artists': [{'name': 'STARSET', 'id': 'UCzYd1EYoMbG8tFWQ69Odi4Q'}]
        self.album: str = str(track['album']['name']) if track['album'] else ''
        self.cover_art: str = track['thumbnails'][-1]['url']
        self.duration: str = track['duration']  # 'duration': '3:16'
        self.meta_name: str = ''
        self.meta_artist: str = ''

    def get_artists_names(self):
        return [artist['name'] for artist in self.artists]

    def get_artists_names_str(self):
        return ', '.join(self.get_artists_names())

    def get_artists_ids(self):
        return [artist['id'] for artist in self.artists]

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
                self.meta_name = meta_name if meta_name else self.title
                self.meta_artist = meta_artist if meta_artist else self.get_artists_names_str()

    def is_equal(self, other):
        """
        Проверяет что результат поиска соответствует запросу
        :param other: резльтат поиска
        :return: True if is_equal else False
        """
        if self == other:  # found track has the same ID
            return True
        return self.has_same_title(other) and self.has_same_artist(other)

    def has_same_title(self, other):  # todo
        if not self.meta_name:
            n_yt = normalized(self.title)
        else:
            n_yt = normalized(self.meta_name)
        n_ytm = normalized(other.title)
        if n_yt.find(n_ytm) != -1:
            return True
        if n_ytm.find(n_yt) != -1:
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

    def __str__(self):
        return self.track_id + SEP + self.title + SEP + self.get_artists_names_str() + SEP + self.album

    # def to_db_track(self, state):
    #     norm_title = self.title.replace('[', '(').replace(']', ')')
    #     feat = feat_finder(norm_title)
    #     if feat != '':
    #         title = norm_title.replace(feat, '').strip()
    #         feat_arts = feat.replace('feat.', '')[1:-1]
    #     else:
    #         title = norm_title
    #         feat_arts = ''
    #     return DBTrack(track_id=self.track_id,
    #                    state=state,
    #                    title=title,
    #                    artists=', '.join(artist_splitter(artist_fixer(self.artists_list) + [feat_arts])),
    #                    album=self.album,
    #                    cover_art=self.cover_art)
