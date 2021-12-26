from mysql.connector import connect, Error
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

    def contains_video(self, video_id: str):
        """
        Проверяет было ли видео уже обработано (таблица Video-Song)
        """
        if not video_id:
            return False

        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM video_song where id_Video='{video_id}'")
        if cur.fetchone():
            return True
        return False

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

    def get_data_by_param(self, param, value):
        """
        Возвращает все записи из БД по заданному параметру.

        :param param: name of parameter
        :param value: value of parameter
        :return: list[MusicTrack]
        """
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"SELECT * FROM {self.filename} where {param}='{value}'")
            rows = cur.fetchall()
            cur.close()
            tracks = []
            for row in rows:
                tracks.append(self.__make_db_track_from_db_row(row))
            return tracks

    def get_all_data(self):
        """
        Возвращает все записи из БД.

        :return: list[MusicTrack]

        """
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"SELECT * FROM {self.filename}")
            rows = cur.fetchall()
            cur.close()
            tracks = []
            for row in rows:
                tracks.append(self.__make_db_track_from_db_row(row))
            return tracks

    def get_track_by_param(self, param, value):
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"SELECT * FROM {self.filename} where {param}='{value}'")
            row = cur.fetchone()
            cur.close()
            return self.__make_db_track_from_db_row(row)

    @staticmethod
    def __make_db_track_from_db_row(row):
        return DBTrack(track_id=row[0], state=row[1], downloaded=row[2], title=row[3],
                       artists=row[4], album=row[5], release_year=row[6],
                       total_tracks=row[7], track_number=row[8], genre=row[9],
                       cover_art=row[10], lyrics=row[11])

# def delete_id(filename: str, video_id):
#     con = sql.connect(f'{filename}.db')
#     with con:
#         cur = con.cursor()
#         cur.execute(f"DELETE FROM {filename} WHERE id='{video_id}';")
#         con.commit()
#         cur.close()
#
#
# def update_id(filename: str, video_id, key, value):
#     con = sql.connect(f'{filename}.db')
#     with con:
#         cur = con.cursor()
#         cur.execute(f"Update {filename} set '{key}' = '{value}' where id = '{video_id}'")
#         con.commit()
#         cur.close()
