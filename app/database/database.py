import sqlite3 as sql
from youtube_playlist_downloader.database.db_track import DBTrack


class TracksTable:
    def __init__(self):
        self.filename = 'tracks_new'
        self.con = sql.connect(f'{self.filename}.db')

        with self.con:
            cur = self.con.cursor()
            cur.execute(f"""CREATE TABLE IF NOT EXISTS `{self.filename}`(
                `id` STRING PRIMARY KEY,
                `search_result` INT,
                `downloaded` INT,
                `title` STRING,
                `artists` STRING,
                `album` STRING,
                `release_year` INT,
                `total_tracks` INT,
                `track_number` INT,
                `genre` STRING,
                `cover_art` STRING,
                `lyrics` STRING
                )
            """)
            self.con.commit()

    def add_track(self, db_track: DBTrack):
        with self.con:
            cur = self.con.cursor()
            cur.execute(
                f"INSERT OR IGNORE INTO {self.filename} VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                db_track.get()
            )
            self.con.commit()

    def add_tracks(self, db_tracks: list[DBTrack]):
        for db_track in db_tracks:
            self.add_track(db_track)

    def contains_id(self, video_id: str):
        if video_id is None:
            return False
        with self.con:
            cur = self.con.cursor()
            cur.execute(f"SELECT * FROM {self.filename} where id='{video_id}'")
            if cur.fetchone():
                return True
        return False

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
