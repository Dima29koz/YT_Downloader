from app.database.db_object import DBTrack
from app.deezer_.search_dz import DZSearcher
from app.spotify.search_sp import SpSearcher
from app.usefull.exceptions import SearchingError


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


def show_data_sp(data: list[DBTrack]):
    err_counter = 0
    for i, track in enumerate(data[:100]):
        # if track.title.find('Dusk Till Dawn') != -1:
        # print(i, track)
        print()
        if not search_on_spotify(track):

            # print(i, track)
            err_counter += 1
    print(err_counter)


def show_data(data: list[DBTrack]):
    for i, track in enumerate(data):
        print(i, track.get())


def search_dz(data: list[DBTrack]):
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

