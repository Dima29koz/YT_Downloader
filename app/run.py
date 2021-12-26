from app.database.database import DataBase
from app.youtube.yt_handler import YTMSearcher
from app.youtube.youtube_music_track import YouTubeMusicTrack
from app.database.db_object import DBTrack, DBArtist, DBAlbum
from app.youtube import exceptions as ex


class DBHandler:
    def __init__(self, table: DataBase):
        self.table = table
        self.yt = YTMSearcher()

    def add_playlist_to_db(self, playlist_id: str):
        with open('Unavailable_videos.txt', 'a', encoding='utf-8') as log:
            amount = 0
            for i, track in enumerate(self.yt.get_track_list_from_playlist(playlist_id)):
                if not self.table.contains_video(track.track_id):
                    self.find_track_data(track, log)
                else:
                    amount += 1
                print(f"Added {i + 1} tracks...")
            print(f"{amount} track were duplicated")

    def find_track_data(self, track: YouTubeMusicTrack, log):
        try:
            ytm_track = self.yt.get_search_result(track)
        except ex.SearchingError:  # todo обработать другие исключения,
            # плохо писать в лог то что не нашлось, но доступно
            log.write(str(track) + '\n')
        else:
            if not self.table.contains_track(ytm_track.track_id):
                self.add_data_to_db(ytm_track)
            self.table.add_link_video_song(track.track_id, ytm_track.track_id)

    def add_data_to_db(self, ytm_track: YouTubeMusicTrack):
        # find other info about track
        alb = self.yt.get_album_info(ytm_track.album_id)
        if not self.table.contains_album(ytm_track.album_id):
            db_album = DBAlbum(
                ytm_track.album_id, ytm_track.album, alb['year'],
                track_amount=alb['trackCount'], cover=alb['thumbnails'][-1]['url'],
                alb_type_id=self.table.get_album_type_id(alb['type']))
            self.table.add_album(db_album)
        for j, tr in enumerate(alb['tracks'], 1):
            if tr['videoId'] == ytm_track.track_id or tr['title'] == ytm_track.title:
                ytm_track.tr_number = j
                break
        self.table.add_track(ytm_track.to_db_track())

        for artist in ytm_track.artists:
            artist_id = artist['id']
            art = self.yt.get_artist_info(artist_id)
            if not self.table.contains_artist(artist_id):
                self.table.add_artist(DBArtist(artist_id, artist['name'], art['thumbnails'][-1]['url']))
            self.table.add_link_track_artist(ytm_track.track_id, artist_id)
            self.table.add_link_artist_album(artist_id, ytm_track.album_id)
        self.table.add_link_album_track(ytm_track.album_id, ytm_track.track_id)
