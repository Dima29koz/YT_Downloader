from app.database.database import DataBase
from app.run import DBHandler


def main(playlist_id: str):
    db_h = DBHandler(DataBase())
    db_h.add_playlist_to_db(playlist_id)
    # show_data(table.get_all_data())
    # show_data_sp(table_.get_data_by_param('search_result', 1))
    # search_dz(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 2))
    # show_data(table_.get_data_by_param('artists', 'Taylor Swift'))
    # track = get_db_track(table_.get_track_by_param('id', 'H1LdQntDnFY'))


if __name__ == "__main__":
    test_id = 'PL8wnwtwgCjP_GKWAxsapNIrBNY3tu41g6'
    main(test_id)
