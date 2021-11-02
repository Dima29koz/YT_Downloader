from app.usefull.functions import artist_splitter, artist_fixer, feat_finder
from app.database.db_track import DBTrack


class YouTubeMusicTrack:
    def __init__(self, track: dict):
        self.artist_ids: list = [str(artist['id']) for artist in track['artists']] if track['artists'] else ['Unknown']
        self.track_id: str = track['videoId']
        self.title: str = track['title']
        self.artists: list = artist_splitter([artist['name'] for artist in track['artists']]) if track['artists'] else ['Unknown']
        self.album: str = str(track['album']['name']) if track['album'] else None
        self.cover_art: str = track['thumbnails'][-1]['url']
        try:
            self.is_available: bool = track['isAvailable']
        except KeyError:
            self.is_available: bool = True
        self.duration: str = track['duration']

    artist: str = property(lambda self: ', '.join(self.artists))
    artists_list: list = property(lambda self: self.artists)

    def to_db_track(self, state):
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
                       artists=', '.join(artist_splitter(artist_fixer(self.artists_list) + [feat_arts])),
                       album=self.album,
                       cover_art=self.cover_art)

    def __str__(self):
        return str(self.track_id) + ' -|- ' + self.title + ' -|- ' + self.artist + ' -|- ' + str(self.album)
