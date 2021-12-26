from app.database.database import DataBase
from youtube.yt_handler import YTMSearcher
from app.run import DBHandler


def main(playlist_id: str):
    # yt.print_search_result(('Mvb6NQozYsE',))
    # yt.print_artist_info('UC02e0Ntqqe7JSRkXTfy1R8g')
    # yt.print_artist_album('UCycDQgnBrm6VCI-Q_DxrK6g', '6gPbAUNxRUJDb0VCQ25JQUFHVnVBQUZTVlFBQlVsVUFBUUJHUlcxMWMybGpYMlJsZEdGcGJGOWhjblJwYzNRQUFRQUJRd0FBQUFFQUFRQUFBUUVFQWFBVnlRaVhBeG9ZVlVONVkwUlJaMjVDY20wMlZrTkpMVkZmUkhoeVN6Wm5nZ0VZVlVONVkwUlJaMjVDY20wMlZrTkpMVkZmUkhoeVN6Wm5BQUVRMGNiM3pKU0I5QUlhQW14dkdBQXFEMkZ5ZEdsemRGOXlaV3hsWVhObGN6Q3gxTkRsbF9ISjhuQQ%3D%3D')
    # yt.print_album_info('MPREb_yYMh3GhN4Jj')
    # 'https://music.youtube.com/watch?v=6wsm5y07qDs&feature=share'
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
