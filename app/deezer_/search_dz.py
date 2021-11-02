import deezer
from app.usefull.exceptions import SearchingError
from app.database.db_track import DBTrack
from app.deezer_.deezer_track import DeezerTrack
from app.usefull.functions import soft_normalized, artist_splitter_runtime
from app.usefull.search_rating_calculator import SRCalculator

dz = deezer.Client()


class DZSearcher:
    def __init__(self, db_track: DBTrack):
        self.db_track = db_track
        self.dt_track_norm_arts = artist_splitter_runtime([self.db_track.artists])
        self.search_result = self.__dz_searching()
        if len(self.search_result) > 0:
            sr_calc = SRCalculator(self.db_track.title, self.dt_track_norm_arts, self.db_track.album)
            for track in self.search_result:
                track.add_track_info(dz.get_track(track.track_id).asdict(), dz.get_album(track.album_id).asdict())
                track.search_rating = sr_calc.calculate_sr(track.title,
                                                           track.contributors_names + [track.artist_name],
                                                           track.album_title, track.record_type)

                if track.search_rating >= 99 and track.record_type == 'album':
                    break

            self.search_result = sorted(self.search_result,
                                        key=lambda tr: (tr.search_rating, tr.record_type_id, tr.album_total_tracks),
                                        reverse=True)

    def get_best_search_result(self):
        if len(self.search_result) > 0 and self.search_result[0].search_rating >= 64:
            for tr in self.search_result:
                print(tr)
                # print(tr.contributors_names)
                # print(tr.album_artist)
                # print(tr.album_contributors_names)
            return self.search_result[0]
        else:
            raise SearchingError

    def __dz_searching(self):
        title = soft_normalized(self.db_track.title)
        artist = ", ".join(self.dt_track_norm_arts)
        q = f'track:"{title}" artist:"{artist}"=undefined'
        tracks = []
        search_result = dz.search(q, relation='track', limit=5)
        for track in search_result:
            tracks.append(DeezerTrack(track.asdict()))
        if len(tracks) == 0:
            q = f'{title} - {artist}'
            search_result = dz.search(q, relation='track', limit=5)
            for track in search_result:
                tracks.append(DeezerTrack(track.asdict()))
        return tracks
