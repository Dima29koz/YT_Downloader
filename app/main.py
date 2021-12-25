from app.database.database import TracksTable
from youtube.yt_handler import YTMSearcher
from app.run import add_playlist_to_db, show_data


def main(playlist_id: str):
    yt = YTMSearcher()
    res = yt.get_track_list_from_playlist(playlist_id)
    for e in res:
        print(e.get_info())
    # t = list(res)[-1]
    # print(str(t) + ' ' + t.get_meta_data())
    # yt.print_search_result(('Mvb6NQozYsE',))
    # yt.print_artist_info('UC02e0Ntqqe7JSRkXTfy1R8g')
    # yt.print_artist_album('UCycDQgnBrm6VCI-Q_DxrK6g', '6gPbAUNxRUJDb0VCQ25JQUFHVnVBQUZTVlFBQlVsVUFBUUJHUlcxMWMybGpYMlJsZEdGcGJGOWhjblJwYzNRQUFRQUJRd0FBQUFFQUFRQUFBUUVFQWFBVnlRaVhBeG9ZVlVONVkwUlJaMjVDY20wMlZrTkpMVkZmUkhoeVN6Wm5nZ0VZVlVONVkwUlJaMjVDY20wMlZrTkpMVkZmUkhoeVN6Wm5BQUVRMGNiM3pKU0I5QUlhQW14dkdBQXFEMkZ5ZEdsemRGOXlaV3hsWVhObGN6Q3gxTkRsbF9ISjhuQQ%3D%3D')
    # yt.print_album_info('MPREb_yYMh3GhN4Jj')
    # 'https://music.youtube.com/watch?v=6wsm5y07qDs&feature=share'
    # table = TracksTable()
    # add_playlist_to_db(table, playlist_id)
    # show_data(table.get_all_data())
    # show_data_sp(table_.get_data_by_param('search_result', 1))
    # search_dz(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 1))
    # show_data(table_.get_data_by_param('search_result', 2))
    # show_data(table_.get_data_by_param('artists', 'Taylor Swift'))
    # track = get_db_track(table_.get_track_by_param('id', 'H1LdQntDnFY'))


if __name__ == "__main__":
    test_url = 'https://music.youtube.com/playlist?list=PL8wnwtwgCjP_GKWAxsapNIrBNY3tu41g6'
    URL = 'https://music.youtube.com/playlist?list=PL8wnwtwgCjP8zbM0Z0viLEWlSNkmo_T08'  # music
    ytm_playlist_id = 'PL8wnwtwgCjP_GKWAxsapNIrBNY3tu41g6'
    test_id = 'PL8wnwtwgCjP_GKWAxsapNIrBNY3tu41g6'
    main(test_id)
    # print(len('https://lh3.googleusercontent.com/ZhHFDrMl4GjwHA4lCN3DwRqlc959T8e5WLPMI0dmiFtZdF2jaXbyiVQ_t9hj-Oa6kcPiuG92EFr8cIUl=w120-h120-l90-rj'))
