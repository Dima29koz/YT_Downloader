import re

from youtube_playlist_downloader.usefull.functions import without_feat, artist_splitter_runtime, feat_finder


class SRCalculator:
    def __init__(self, original_title: str, norm_original_artists: list, original_album: str):
        self.original_title = original_title  # title without feats
        self.original_album = original_album
        self.norm_original_artists: list = norm_original_artists

        self.__norm_original_title = self.__normalizer_of_title(self.original_title)
        self.__norm_original_album = self.__soft_alb_normalizer(self.original_album)

        self.new_title: str = ''
        self.new_artists: list = []
        self.new_album: str = ''
        self.new_album_type: str = ''

        self.rating_title = 0
        self.rating_artist = 0
        self.rating_album = 0

    def calculate_sr(self, new_title: str, new_artists: list, new_album: str, new_album_type: str):
        self.new_title = new_title
        self.new_artists: list = new_artists
        self.new_album = new_album
        self.new_album_type = new_album_type

        self.rating_title = self.__calc_title_rating()
        self.rating_artist = self.__calc_artist_rating()
        self.rating_album = self.__calc_album_rating()

        return self.rating_title + self.rating_artist + self.rating_album

    def __calc_title_rating(self):
        o_title = self.original_title
        s_title = without_feat(self.new_title)
        if s_title == o_title:
            return 33
        if self.__normalized(s_title) == self.__normalized(o_title):
            return 32
        if self.__normalizer_of_title(s_title) == self.__norm_original_title:
            return 30
        if self.__normalizer_of_title(self.new_title).find(self.__norm_original_title) != -1:
            return 15
        if self.__norm_original_title.find(self.__normalizer_of_title(self.new_title)) != -1:
            return 15
        return 0

    def __calc_artist_rating(self):
        orig_art = self.norm_original_artists
        new_art = artist_splitter_runtime(self.new_artists)
        common_artist = set(new_art) & set(orig_art)
        if len(common_artist) > 0:
            return 33 - (max(len(orig_art), len(new_art)) - len(common_artist)) * 2
        return 0

    def __calc_album_rating(self):
        diff = 0
        if self.new_album_type == 'compilation' or self.new_album_type == 'compile':
            diff = 20
        orig_alb = self.__norm_original_album
        new_alb = self.__soft_alb_normalizer(self.new_album)
        if new_alb == orig_alb:
            return 33 - diff
        if self.__normalizer_of_album(new_alb) == self.__normalizer_of_album(orig_alb):
            return 25 - diff
        if self.new_album_type == 'single':
            if self.new_album.split(' ')[0].lower().strip() == self.original_album.split(' ')[0].lower().strip():
                return 16 - diff
            if self.new_album.split(' ')[0].lower().strip() == self.original_title.split(' ')[0].lower().strip():
                return 16 - diff
            if self.__normalized(without_feat(self.original_title)).find(self.__normalized(new_alb)) != -1:
                return 16 - diff
            if self.__norm_original_title.find(self.__normalizer_of_album(new_alb)) != -1:
                return 16 - diff
        if self.new_album_type == 'album' or self.new_album_type == 'ep':
            if self.rating_title >= 30 and self.rating_artist >= 16:
                return 33 - diff
        return 0

    @staticmethod
    def __normalized(raw_str: str):
        res = raw_str.replace('[', '(').replace(']', ')').replace('$', 's')
        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', " ", res)))
        return res.strip().lower()

    @staticmethod
    def __normalizer_of_title(raw_title: str):
        res = re.sub(r'[(][^(]+?[)]', '', raw_title)
        while raw_title != res:
            raw_title = res
            res = re.sub(r'[(][^(]+?[)]', '', raw_title)

        res = re.sub(r'[$]', 's', res)
        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
        return res

    @staticmethod
    def __soft_alb_normalizer(raw_album: str):
        """
        Возвращает название альбома в нижнем регистре, удаляя некоторые скобки

        """
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

        res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).strip()
        return res
