from mysql.connector import connect, Error, DatabaseError
from app.database.db_object import DBTrack, DBAlbum, DBArtist
import app.database.queries.insert_queries as insert
import app.database.queries.select_query as select


class DataBase:
    def __init__(self):
        self.basename = 'ytmusic_analizer'

        try:
            self.con = connect(
                    host="localhost",
                    user="Admin",
                    password="admin",
                    database="ytmusic_analizer",
            )
        except Error as e:
            print(e)

    def add_track(self, db_track: DBTrack):
        cur = self.con.cursor()
        cur.execute(insert.add_track(*db_track.get()))
        self.con.commit()

    def add_artist(self, db_artist: DBArtist):
        cur = self.con.cursor()
        cur.execute(insert.add_artist(*db_artist.get()))
        self.con.commit()

    def add_album(self, db_album: DBAlbum):
        cur = self.con.cursor()
        cur.execute(insert.add_album(*db_album.get()))
        self.con.commit()

    def contains_video(self, video_id: str) -> str | None:
        """
        Проверяет было ли видео уже обработано (таблица Video-Song)
        """
        if not video_id:
            return

        cur = self.con.cursor()
        cur.execute(f"SELECT id_song FROM video_song where id_Video='{video_id}'")
        track = cur.fetchone()
        if track:
            return track[0]

    def contains_track(self, track_id: str):
        """
        Проверяет, был ли track уже обработан (таблица track)
        """
        if not track_id:
            return False
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM track where id_track='{track_id}'")
        if cur.fetchone():
            return True
        return False

    def contains_artist(self, artist_id: str):
        """
        Проверяет, был ли artist уже обработано (таблица artists)
        """
        if not artist_id:
            return False
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM artists where id_artist='{artist_id}'")
        if cur.fetchone():
            return True
        return False

    def contains_album(self, album_id: str):
        """
        Проверяет, был ли album уже обработано (таблица album)
        """
        if not album_id:
            return False
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM album where id_album='{album_id}'")
        if cur.fetchone():
            return True
        return False

    def contains_favorite(self, email: str, track_id: str):
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM favorite where user_email='{email}' and id_track='{track_id}'")
        if cur.fetchone():
            return True
        return False

    def add_link_track_artist(self, track_id, artist_id):
        cur = self.con.cursor()
        cur.execute(insert.add_link_track_artist(track_id, artist_id))
        self.con.commit()

    def add_link_artist_album(self, artist_id, album_id):
        cur = self.con.cursor()
        cur.execute(insert.add_link_artist_album(artist_id, album_id))
        self.con.commit()

    def add_link_album_track(self, album_id, track_id):
        cur = self.con.cursor()
        cur.execute(insert.add_link_album_track(album_id, track_id))
        self.con.commit()

    def add_link_video_song(self, video_id, track_id):
        cur = self.con.cursor()
        cur.execute(insert.add_link_video_track(video_id, track_id))
        self.con.commit()

    def get_album_type_id(self, type_name: str):
        cur = self.con.cursor()
        cur.execute(f"SELECT id_album_type FROM album_type where type_name='{type_name}'")
        type_id = cur.fetchone()
        if type_id:
            return type_id[0]
        return None

    def check_user(self, email: str, password: str):
        cur = self.con.cursor()
        cur.execute(select.get_user_data_by_email(email))
        user = cur.fetchone()
        if user and user[1] == password:
            return True
        return False

    def add_user(self, email: str, login: str, password: str):
        cur = self.con.cursor()
        try:
            cur.execute(insert.add_user(email, login, password))
        except DatabaseError:
            return False
        else:
            self.con.commit()
            return True

    def get_favorite(self, email: str):
        cur = self.con.cursor()
        cur.execute(select.get_track_info_by_user(email))
        tr_info = cur.fetchall()
        if tr_info:
            return tr_info
        return []

    def add_favorite(self, track_id: str, email: str):
        if not self.contains_favorite(email, track_id):
            cur = self.con.cursor()
            cur.execute(insert.add_favorite_track_to_user(email, track_id))
            self.con.commit()
