class DBTrack:
    def __init__(self, track_id=None, state=0, downloaded=0, title=None,
                 artists=None, album=None, release_year=None, total_tracks=0,
                 track_number=0, genre=None, cover_art=None, lyrics=None):
        self.id: str = track_id
        self.state: int = state
        self.downloaded: int = downloaded
        self.title: str = str(title)
        self.artists: str = artists
        self.album: str = str(album)
        self.release_year: str = release_year
        self.total_tracks: int = total_tracks
        self.track_number: int = track_number
        self.genre: str = genre
        self.cover_art: str = cover_art
        self.lyrics: str = lyrics

    def get(self):
        return (self.id, self.state, self.downloaded, self.title,
                self.artists, self.album, self.release_year,
                self.total_tracks, self.track_number, self.genre, self.cover_art, self.lyrics)

    def __str__(self):
        # return self.id + ' -|- ' + str(self.state) + ' -|- ' + self.title + ' -|- ' + self.artists + ' -|- ' + self.album
        return self.title + ' -|- ' + self.artists + ' -|- ' + self.album
