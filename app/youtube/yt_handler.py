from ytmusicapi.ytmusic import YTMusic

from app.youtube.youtube_music_track import YouTubeMusicTrack
from app.youtube.exceptions import SearchingError


class YTMSearcher:
    def __init__(self):
        self.ytm = YTMusic()

    def get_tracks_from_playlist(self, playlist_id: str):
        playlist = self.ytm.get_playlist(playlist_id, limit=2000)
        for track in playlist['tracks']:
            yield YouTubeMusicTrack(track)

    def get_song_videos(self, track: YouTubeMusicTrack):
        found_track = self.search_ytm_song(track)
        res = [track]
        if found_track and found_track != track:
            res.append(track)
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
                search_result = self.search_song_by_query(*query)
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

    def search_song_by_query(self, query: str, ignore_spelling: bool = False):
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
