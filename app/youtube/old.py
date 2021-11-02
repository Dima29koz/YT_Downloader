from ytmusicapi import YTMusic

from app.database.db_track import DBTrack
from app.youtube.exceptions import SearchingError
from app.youtube.youtube_music_track import YouTubeMusicTrack

ytm = YTMusic()


class YTMSearcher:
    def __init__(self, original_track: YouTubeMusicTrack):
        self.yt_track = original_track
        self.meta_name = None
        self.meta_artist = None

    def ytm_search_result(self) -> list[DBTrack]:
        """

        Возвращает список треков приведенных к типу DBTrack.\n
        Если при поиске нашелся тот же id то вернет список из 1 объекта [ytm_track].\n
        Если при поиске нашелся другой id то вернет список из 2 объектов [yt_track, ytm_track].\n
        Если поиск завершился с ошибкой то вернет список из 1 объекта [yt_track].

        :return: list[MusicTrack]
        """
        if self.__duration():
            return [self.yt_track.to_db_track(state=3)]
        ytm_track = self.__ytm_searching()
        res = []
        if self.yt_track.is_available:
            if ytm_track is not None:
                if self.yt_track.track_id == ytm_track.track_id:
                    res.append(ytm_track.to_db_track(state=1))
                else:
                    res.append(self.yt_track.to_db_track(state=0))
                    res.append(ytm_track.to_db_track(state=1))
            else:
                res.append(self.yt_track.to_db_track(state=2))
        else:
            if ytm_track is not None:
                res.append(ytm_track.to_db_track(state=1))
            else:
                raise SearchingError

        return res

    def __duration(self):
        """
        Возвращает True если длина трека >=14 минут
        """
        if self.yt_track.duration:
            time = self.yt_track.duration.split(':')
            if len(time) == 2 and int(time[-2]) >= 14:
                return True
            if len(time) == 3:
                return True
        return False
