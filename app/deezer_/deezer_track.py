from youtube_playlist_downloader.usefull.functions import feat_finder


class DeezerTrack:
    def __init__(self, search: dict):
        self.track_id = search['id']
        self.title = search['title']
        self.title_short = search['title_short']
        self.artist_id = search['artist']['id']
        self.artist_name = search['artist']['name']
        self.artist_picture = search['artist']['picture_xl']

        self.album_id = search['album']['id']
        self.album_title = str(search['album']['title'])
        self.album_cover = search['album']['cover_xl']

        self.track_pos = 0
        self.disk_number = 0
        self.track_bpm = 0
        self.contributors_ids = []
        self.contributors_names = []
        self.contributors_covers = []
        self.contributors_roles = []

        self.album_main_genre = 0
        self.album_genres_ids = []
        self.album_genres_names = []
        self.album_total_tracks = 0
        self.album_release_date = ''
        self.record_type = ''

        self.album_contributors_names = []

        self.album_artist = ''

        self.record_type_id = 0
        self.search_rating = 0

    def add_track_info(self, track: dict, album: dict):
        self.track_pos = track['track_position']
        self.disk_number = track['disk_number']
        self.track_bpm = track['bpm']
        self.contributors_ids = [contributor['id'] for contributor in track['contributors']]
        self.contributors_names = [contributor['name'] for contributor in track['contributors']]
        if self.artist_name not in self.contributors_names:
            self.contributors_names.append(self.artist_name)
        self.contributors_covers = [contributor['picture_xl'] for contributor in track['contributors']]
        self.contributors_roles = [contributor['role'] for contributor in track['contributors']]

        self.album_main_genre = album['genre_id']
        self.album_genres_ids = [genre['id'] for genre in album['genres']]
        self.album_genres_names = [genre['name'] for genre in album['genres']]
        self.album_total_tracks = album['nb_tracks']
        self.album_release_date = album['release_date']
        self.record_type = album['record_type']
        self.album_contributors_names = [contributor['name'] for contributor in album['contributors']]
        self.album_artist = album['artist']['name']

        if self.record_type != 'compile':
            if self.album_artist == 'Разные исполнители':
                self.record_type = 'compile'
            elif set(self.contributors_names).isdisjoint(set(self.album_contributors_names)):
                self.record_type = 'compile'
            elif self.contributors_names[0] == 'Разные исполнители':
                self.record_type = 'compile'
                self.contributors_names.remove('Разные исполнители')

        self.record_type_id = self.__get_type_id()

    def __get_type_id(self):
        if self.record_type == 'single':
            return 3
        elif self.record_type == 'ep':
            return 4
        elif self.record_type == 'album':
            return 5
        elif self.record_type == 'compile':
            return 1
        else:
            return 0

    def __str__(self):
        feat = feat_finder(self.title)
        return f'({self.search_rating}) ' + self.title_short.replace(feat, '').strip() + ' -|- ' + \
               ', '.join(self.contributors_names) + ' -|- ' + \
               self.album_title + f' -||- record type: {self.record_type}'


