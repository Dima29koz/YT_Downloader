import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import List

from app.spotify.spotify_track import SpotifyTrack
from app.database.db_track import DBTrack
from app.usefull.functions import without_feat, soft_normalized

spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials('522f24ada7e8409fb7ad667b708c3bbb',
                                                                '2e47207d5fab4364b5350d789d2b198e'),
            language='ru')


class SpSearcher:
    def __init__(self, db_track: DBTrack):
        self.db_track = db_track
        self.search_result = self.__sp_searching()
        if len(self.search_result) > 0:
            for track in self.search_result:
                track.calculate_search_rating(self.db_track)
            # self.search_result = sorted(self.search_result, key=lambda tr: (tr.search_rating,
            # 1/int(re.search(r'\d{4}', tr.release_year).group()), tr.total_tracks), reverse=True)
            self.search_result = sorted(self.search_result, key=lambda tr: (tr.search_rating, tr.total_tracks),
                                        reverse=True)

    def get_sp_best_search_result(self):
        """
        Возвращает наилучший результат поиска

        :return: Optional[SpotifyTrack]
        """
        if len(self.search_result) > 0:
            if self.search_result[0].search_rating >= 78:
                if self.search_result[0].alb_type == 'album':
                    print('➨', self.db_track)
                    print('Ура! Нашелся альбом!!!')
                    print(self.search_result[0])
                    return self.search_result[0]
                elif self.search_result[0].alb_type == 'single':
                    print('➨', self.db_track)
                    print('Нашелся сингл')
                    print(self.search_result[0])
                    return self.search_result[0]
                else:
                    print('Есть результаты с рейтингом >=78', 'ERR of rating algorithm')
                    print('➨', self.db_track)
                    for track in self.search_result:
                        print(track)
                    return
            else:
                print('Нет результатов с рейтингом >=80')
                print('➨', self.db_track)
                for track in self.search_result:
                    print(track)
                return
        else:
            print('➨', self.db_track)
            print('По данному запросу нашлось 0 результатов')
            return

    def __sp_searching(self) -> List[SpotifyTrack]:
        """
        Возвращает список из результатов поиска на Spotify

        :return: list[SpotifyTrack] or []
        """
        title = without_feat(self.db_track.title).replace("'", "")
        search_result = []
        for artist in self.db_track.artists.split(','):
            artist = artist.replace("'", "")
            q = f'{title} {artist}'

            if self.db_track.album:
                album = self.db_track.album.replace("'", "")
                result = spotify.search(q + f' {album}', limit=5, type='track', market='RU')
                # поисковый запрос
                # print(result['tracks']['href'])
                items = result["tracks"]["items"]
                if len(items) > 0:
                    for item in items:
                        # if item['album']['album_type'] != 'compilation':
                        search_result.append(SpotifyTrack(item))

            # album search unsuccessful, try without
            result = spotify.search(q=q, limit=5, type='track', market='RU')
            # поисковый запрос
            # print(result['tracks']['href'])
            items = result["tracks"]["items"]
            if len(items) > 0:
                for item in items:
                    # if item['album']['album_type'] != 'compilation':
                    sp_track = SpotifyTrack(item)
                    if sp_track not in search_result:
                        search_result.append(sp_track)
            if len(search_result) == 0:
                if self.db_track.album:
                    album = self.db_track.album.replace("'", "")
                    q = f'{soft_normalized(title)} {artist} {album}'
                else:
                    q = f'{soft_normalized(title)} {artist}'
                result = spotify.search(q=q, limit=5, type='track', market='RU')
                # поисковый запрос
                # print(result['tracks']['href'])
                items = result["tracks"]["items"]
                if len(items) > 0:
                    for item in items:
                        # if item['album']['album_type'] != 'compilation':
                        sp_track = SpotifyTrack(item)
                        if sp_track not in search_result:
                            search_result.append(sp_track)

        return search_result
