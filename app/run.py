from typing import List

from youtube_playlist_downloader.database.database import TracksTable
from youtube_playlist_downloader.spotify.search_sp import SpSearcher
from youtube_playlist_downloader.youtube.search_ytm import playlist_getter, YTMSearcher
from youtube_playlist_downloader.database.db_track import DBTrack
from youtube_playlist_downloader.usefull.exceptions import SearchingError
from youtube_playlist_downloader.youtube.youtube_track import YouTubeMusicTrack
from youtube_playlist_downloader.deezer_.search_dz import DZSearcher


def add_playlist_to_db(table: TracksTable, playlist_id):
    with open('Unavailable_videos.txt', 'a', encoding='utf-8') as log:
        for i, track in enumerate(playlist_getter(playlist_id)):
            if not table.contains_id(track.track_id):
                try:
                    table.add_tracks(YTMSearcher(track).ytm_search_result())
                except SearchingError:
                    log.write(str(track) + '\n')
            print(f"Added {i+1} tracks...")


def search_on_spotify(db_track: DBTrack):
    """

    Ищет трек на Spotify  если находит то что нужно, заменяет свои данные

    """
    sp_track = SpSearcher(db_track).get_sp_best_search_result()
    if sp_track:
        # замена значений
        # print("successful search")
        # print(sp_track)
        return True
    else:
        # print(self)
        # print("searching ERR")
        return False


def show_data_sp(data: List[DBTrack]):
    err_counter = 0
    for i, track in enumerate(data[:100]):
        # if track.title.find('Dusk Till Dawn') != -1:
        # print(i, track)
        print()
        if not search_on_spotify(track):

            # print(i, track)
            err_counter += 1
    print(err_counter)


def show_data(data: List[DBTrack]):
    for i, track in enumerate(data):
        if track.title.find('Champion') != -1:
            print(i, track.get())


def search_dz(data: List[DBTrack]):
    """

    Ищет трек на Deezer если находит то что нужно, заменяет свои данные

    """
    with open('Dz_searching_err.txt', 'a', encoding='utf-8') as log:
        idx = 369
        # for i, track in enumerate(data):
        for i, track in enumerate(data[idx:idx+1]):
            print(i)
            print('->  ', track)
            try:
                dz_track = DZSearcher(track).get_best_search_result()
                if dz_track:
                    # замена значений
                    # print("successful search")
                    print(dz_track)
                    # return True
                else:
                    # print(self)
                    # print("searching ERR")
                    # return False
                    pass
            except SearchingError:
                log.write(str(track) + '\n')


if __name__ == "__main__":
    URL = 'https://music.youtube.com/playlist?list=PL8wnwtwgCjP8zbM0Z0viLEWlSNkmo_T08'  # music
    table_ = TracksTable()
    # add_playlist_to_db(table_, 'PL8wnwtwgCjP8zbM0Z0viLEWlSNkmo_T08')
    # show_data(table_.get_all_data())
    # show_data_sp(table_.get_data_by_param('search_result', 1))
    search_dz(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 2))
    # show_data(table_.get_data_by_param('artists', 'Taylor Swift'))
    # track = get_db_track(table_.get_track_by_param('id', 'H1LdQntDnFY'))
