import re

from youtube_playlist_downloader.database.db_track import DBTrack
from youtube_playlist_downloader.usefull.functions import feat_finder, without_feat, artist_splitter, artist_splitter_runtime


class SpotifyTrack:
    def __init__(self, track: dict):
        self.sp_url = track['external_urls']['spotify']
        self.alb_type = track['album']['album_type']
        self.alb_artists = track['album']['artists'][0]['name']
        self.alb_url = track['album']['external_urls']['spotify']
        self.rating_title = 0
        self.rating_artist = 0
        self.rating_album = 0
        self.search_rating = 0
        self.__title = track['name'].strip()
        # ft = feat_finder(self.__title)
        # self.feats = ft if ft else ''

        artists = []
        for artist in [artist['name'] for artist in track['artists']]:
            arts = re.split(r'[,&]', artist)
            for art in arts:
                art = art.replace("’", "'")
                if art not in artists and art != '':
                    artists.append(art.strip())
        for artist in re.split(r'[,&]', re.sub(r'[()]', '', feat_finder(self.__title).replace('feat.', ''))):
            artist = artist.replace('$', 's').replace("’", "'").strip()
            if artist not in artists and artist != '':
                artists.append(artist.strip())

        self.__artists = artists
        self.__album = str(track['album']['name']).strip() if track['album']['name'] else None
        self.cover_art = track['album']['images'][0]['url'] if len(track['album']['images']) != 0 else None
        self.release_year = track['album']['release_date']
        self.total_tracks = track['album']['total_tracks']
        self.track_number = track['track_number']

    title: str = property(lambda self: self.__title)
    artists: list = property(lambda self: self.__artists)
    artist: str = property(lambda self: ', '.join(self.__artists))
    album: str = property(lambda self: self.__album)

    def __str__(self):
        return f'{self.search_rating:<3}' + ' ' + \
               f'({self.rating_title:<2})' + ' ' + self.title + ' -|- ' + \
               f'({self.rating_artist:<2})' + ' ' + self.artist + ' -|- ' + \
               f'({self.rating_album:<2})' + ' ' + self.album + \
               ' -||- ' + self.alb_type + ' ' + self.alb_artists + \
               ' ' + self.sp_url + ' ' + self.alb_url

    def __eq__(self, other):
        return self.sp_url == other.sp_url

    @staticmethod
    def __normalized(raw_str: str):
        res = raw_str.replace('[', '(').replace(']', ')').replace('$', 's')
        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', " ", res)))
        return res.strip().lower()

    @staticmethod
    def __normalizer_of_title(raw_title: str):
        res = re.sub(r'[(].+?[)]', '', raw_title)
        while raw_title != res:
            raw_title = res
            res = re.sub(r'[(].+?[)]', '', raw_title)

        # res = re.sub(r'\(Featuring.+?\)', '', res)
        # res = re.sub(r'\(with.+?\)', '', res)
        res = re.sub(r'[$]', 's', res)
        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
        return res

    @staticmethod
    def __normalizer_of_artist(raw_artist: str):
        res = re.sub(r'[$]', 's', raw_artist)
        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
        return res

    @staticmethod
    def __soft_alb_normalizer(raw_album: str):
        res = re.sub(r'[$]', 's', raw_album).lower()
        res = res.replace('[', '(').replace(']', ')')
        res = re.sub(r'\(deluxe.*?\)', '', res)
        res = re.sub(r'\(expanded.*?\)', '', res)
        res = re.sub(r'\(ultimate.*?\)', '', res)
        res = re.sub(r'\(полная.*?\)', '', res)
        res = re.sub(r'\(with.*?\)', '', res)
        res = re.sub(r'\(feat.*?\)', '', res)
        res = re.sub(r'\(international.*?\)', '', res)
        return res.strip()

    @staticmethod
    def __normalizer_of_album(raw_album: str):
        res = re.sub(r'\(single.*?\)', '', raw_album)
        res = re.sub(r'\(special.*?\)', '', res)
        res = re.sub(r'\(rock.*?\)', '', res)
        res = re.sub(r'deluxe edition', '', res)
        res = re.sub(r'ultimate', '', res)
        res = re.sub(r'single', '', res)
        res = re.sub(r'ep', '', res)

        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
        return res

    def __calc_title(self, original_track: DBTrack):
        s_title = without_feat(self.__title)
        o_title = without_feat(original_track.title)
        if self.__normalized(s_title) == self.__normalized(o_title):
            return 33
        if self.__normalizer_of_title(s_title) == self.__normalizer_of_title(o_title):
            return 30
        if self.__normalizer_of_title(self.title).find(self.__normalizer_of_title(original_track.title)) != -1:
            return 15
        return 0

    def __calc_artist(self, original_track: DBTrack):
        """
        Важно чтобы в списках артистов не было дубликатов , и все артисты были разделены запятыми
        """
        s_art = self.artists
        o_art = artist_splitter_runtime(
            [original_track.artists] +
            [re.sub('[()]', '', feat_finder(original_track.title).replace('feat.', ''))]
        )
        common_artist = set(artist.lower() for artist in s_art) & set(
            artist.lower() for artist in o_art)
        if len(common_artist) > 0:
            # k = len(common_artist) / max(len(original_track.artists), len(self.artists))
            # return int(k * 33)
            return 33 - (max(len(o_art), len(s_art)) - len(common_artist))
        return 0

    def __calc_album(self, original_track: DBTrack):
        if self.alb_type == 'compilation':
            return -33
        diff = 0
        if self.alb_artists == 'Разные исполнители':
            diff = 18
        if self.alb_type == 'single':
            diff = 3

        s_alb = self.__soft_alb_normalizer(self.album)
        o_alb = self.__soft_alb_normalizer(original_track.album)
        if s_alb == o_alb:
            return 33 - diff
        if self.__normalizer_of_album(s_alb) == self.__normalizer_of_album(o_alb):
            return 25 - diff
        if self.alb_type == 'single':
            if self.album.split(' ')[0].lower().strip() == original_track.album.split(' ')[0].lower().strip():
                return 15 - diff
            if self.__normalized(without_feat(original_track.title)).find(self.__normalized(s_alb)) != -1:
                return 15 - diff
            if self.__normalizer_of_title(original_track.title).find(self.__normalizer_of_album(s_alb)) != -1:
                return 15 - diff
        if self.alb_type == 'album' and self.rating_title >= 30 and self.rating_artist >= 16:
            if self.album.lower().find('collection') == -1:
                return 32 - diff
            else:
                return 31 - diff

        return 0

    def calculate_search_rating(self, original_track: DBTrack):
        self.rating_title = self.__calc_title(original_track)
        self.rating_artist = self.__calc_artist(original_track)
        self.rating_album = self.__calc_album(original_track)

        self.search_rating = self.rating_title + self.rating_artist + self.rating_album
