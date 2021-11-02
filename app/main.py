from app.database.database import TracksTable
from youtube.yt_handler import YTMSearcher
from app.run import add_playlist_to_db, show_data


def main(playlist_id: str):
    table = TracksTable()
    # add_playlist_to_db(table, playlist_id)
    show_data(table.get_all_data())
    # show_data_sp(table_.get_data_by_param('search_result', 1))
    # search_dz(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 2))
    # show_data(table_.get_data_by_param('artists', 'Taylor Swift'))
    # track = get_db_track(table_.get_track_by_param('id', 'H1LdQntDnFY'))


if __name__ == "__main__":
    URL = 'https://music.youtube.com/playlist?list=PL8wnwtwgCjP8zbM0Z0viLEWlSNkmo_T08'  # music
    ytm_playlist_id = 'PL8wnwtwgCjP_GKWAxsapNIrBNY3tu41g6'
    main(ytm_playlist_id)
