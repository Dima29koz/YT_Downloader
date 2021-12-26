class DBTrack:
    def __init__(self, track_id, title, release_year=None,
                 track_number=1, disk_number=1, genre_id=None, lyrics=None, duration=0):
        self.track_id: str = track_id
        self.title = title
        self.release_year: str = release_year
        self.track_number: int = track_number
        self.disk_number: int = disk_number
        self.genre_id: int = genre_id
        self.lyrics: str = lyrics
        self.duration: int = duration

    def get(self):
        return (self.track_id, self.title, self.release_year, self.track_number,
                self.disk_number, self.genre_id, self.lyrics, self.duration)


class DBArtist:
    def __init__(self, artist_id, artist_name, cover):
        self.artist_id: str = artist_id
        self.artist_name: str = artist_name
        self.cover: str = cover

    def get(self):
        return (self.artist_id, self.artist_name,
                self.cover)


class DBAlbum:
    def __init__(self, album_id, title, year=None, disks_amount=1,
                 track_amount=1, alb_genre_id=None, cover=None, alb_type_id=None):
        self.album_id = album_id
        self.title = title
        self.year = year
        self.disks_amount = disks_amount
        self.track_amount = track_amount
        self.alb_genre_id = alb_genre_id
        self.cover = cover
        self.alb_type_id = alb_type_id

    def get(self):
        return (self.album_id, self.title, self.year, self.disks_amount,
                self.track_amount, self.alb_genre_id, self.cover, self.alb_type_id)
