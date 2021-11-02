from ytmusicapi.ytmusic import YTMusic

from app.youtube.youtube_music_track import YouTubeMusicTrack
from app.youtube.exceptions import SearchingError


class YTMSearcher:
    def __init__(self):
        self.ytm = YTMusic()

    def get_track_list_from_playlist(self, playlist_id: str):
        playlist = self.ytm.get_playlist(playlist_id, limit=2000)
        for track in playlist['tracks']:
            yield YouTubeMusicTrack(track)

    def get_search_result(self, track: YouTubeMusicTrack):
        """
        Возвращает список треков приведенных к типу DBTrack.\n
        Если при поиске нашелся тот же id то вернет список из 1 объекта [ytm_track].\n
        Если при поиске нашелся другой id то вернет список из 2 объектов [yt_track, ytm_track].\n
        Если поиск завершился с ошибкой то вернет список из 1 объекта [yt_track].
        :raise SearchingError: если началный трек недоступен и по доступной информации поиск завершился с ошибкой
        """
        if track.duration > 900:
            return [track.to_db_track(state=3)]  # трек скорее всего является сборником
        res = []
        try:
            song_track = self.search_ytm_song(track)
        except SearchingError:
            if track.track_id:
                res.append(track.to_db_track(state=2))  # не нашлось song аналога, но трек доступен
            else:
                raise SearchingError
        else:
            res.append(song_track.to_db_track(state=1))  # найденный трек типа song
            if track.track_id and track != song_track:
                res.append(track.to_db_track(state=0))  # есть аналог типа song
        return res

    def search_ytm_song(self, track: YouTubeMusicTrack) -> YouTubeMusicTrack:
        """
        Возвращает результат поиска на YouTubeMusic

        :return: YouTubeMusicTrack or None
        :raise SearchingError: если не удалось ничего найти
        """
        query_value = [
            (track.track_id, True),
            (track.title + ' ' + track.get_artists_names_str(),),
            (track.title,),
            (track.get_meta_data(),)
        ]
        for query in query_value:
            try:
                search_result = self._search_song_by_query(*query)
            except SearchingError:
                pass
            else:
                ytm_track = YouTubeMusicTrack(search_result)
                if track.is_equal(ytm_track):
                    return ytm_track
        raise SearchingError

    @staticmethod
    def convert_to_ytm_track(search_result: dict):
        track = {
            'isAvailable': True,
            'videoId': search_result['videoId'],
            'title': search_result['title'],
            'artists': search_result['artists'],
            'album': search_result['album'],
            'thumbnails': search_result['thumbnails'],
            'duration': search_result['duration']
        }
        return track

    def _search_song_by_query(self, query: str, ignore_spelling: bool = False):
        """
        :return: Возвращает первый из найденных треков
        :raise SearchingError: если поиск завершился с ошибкой
        """
        if not query:
            raise SearchingError
        try:
            search_result = self.ytm.search(query, filter='songs', limit=1, ignore_spelling=ignore_spelling)
            return self.convert_to_ytm_track(search_result[0])
        except IndexError:
            raise SearchingError
