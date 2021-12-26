from ytmusicapi.ytmusic import YTMusic

from app.youtube.youtube_music_track import YouTubeMusicTrack
from app.youtube.exceptions import SearchingError, DurationError


class YTMSearcher:
    def __init__(self):
        self.ytm = YTMusic()

    def get_track_list_from_playlist(self, playlist_id: str):
        """
        список треков плейлиста
        :param playlist_id: pure playlist id ('PL8wnw. . .')
        :return:
        """
        playlist = self.ytm.get_playlist(playlist_id, limit=2000)
        # todo можно забрать информацию о плейлисте (длина, название, ...)
        for track in playlist['tracks']:
            yield YouTubeMusicTrack(track)

    def get_search_result(self, track: YouTubeMusicTrack):
        """
        Возвращает ytm_track в случае если найден трек,
        при ошибке поиска вызовет исключение SearchingError

        :raise SearchingError: если не удалось найти track по входной информации;
        :raise DurationError: если длительность трека больше 900 сек;
        """
        if track.duration > 900:
            raise DurationError  # трек скорее всего является сборником
        try:
            song_track = self.search_ytm_song(track)
        except SearchingError:
            raise SearchingError
        else:
            return song_track

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
                if track.is_equal(ytm_track):  # todo добавить оптимизацию, хранящую ссылки на уже найденные видео
                    return ytm_track
        raise SearchingError

    @staticmethod
    def convert_to_ytm_track(search_result: dict):
        search_result.update({'isAvailable': True})
        return search_result

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

    def print_song_lyrics(self, song_id: str):
        print(self.ytm.get_lyrics(song_id))

    def print_w_playlist(self, song_id):
        print(self.ytm.get_watch_playlist(song_id)['tracks'][0])

    def print_search_result(self, query):
        try:
            print(self._search_song_by_query(*query))
        except SearchingError:
            print('Error ' + query[0])

    def get_artist_info(self, query):
        return self.ytm.get_artist(query)

    def print_artist_album(self, artist_id, params):
        print(self.ytm.get_artist_albums(artist_id, params))

    def get_album_info(self, album_id):
        return self.ytm.get_album(album_id)
