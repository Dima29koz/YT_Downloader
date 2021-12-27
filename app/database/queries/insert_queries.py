
def add_genre(genre_id: int, genre_name: str):
    query = f"""insert ignore into genres values ({genre_id}, '{genre_name}');"""
    return query


def add_album_type(type_id: int, album_type: str):
    query = f"""insert ignore into album_type values ({type_id}, '{album_type}');"""
    return query


def add_track(track_id: str, title: str, year: int, tr_number: int, disk_number: int,
              genre_id: int, lyrics: str, duration: int):
    query = f"""
        insert ignore into track values 
        ('{track_id}', "{title}", 
        {f"{year}" if year else 'NULL'},
        {tr_number}, {disk_number}, 
        {f"{genre_id}" if genre_id else 'NULL'}, 
        {f"'{lyrics}'" if lyrics else 'NULL'}, {duration});"""
    return query


def add_album(id_album: str, album_title: str,
              year: int, disks_amount: int, track_amount: int,
              alb_genre_id: int, cover_art: str, alb_type_id: int):
    query = f"""
        insert ignore into album values 
        ('{id_album}', '{album_title}', 
        {f"{year}" if year else 'NULL'},
        {disks_amount}, {track_amount},
        {f"{alb_genre_id}" if alb_genre_id else 'NULL'},
        '{cover_art}',
        {alb_type_id if alb_type_id else 'NULL'});"""
    return query


def add_artist(id_artist: str, name: str, cover: str):
    query = f"""
        insert ignore into artists (id_artist, name, cover_art) values 
        ('{id_artist}', '{name}', '{cover}');"""
    return query


def add_link_album_track(id_album: str, id_track: str):
    query = f"""
        insert ignore into album_track (id_track, id_album) values 
        ('{id_track}', '{id_album}');"""
    return query


def add_link_track_artist(id_track: str, id_artist: str):
    query = f"""
        insert ignore into track_artists (id_track, id_artist) values 
        ('{id_track}', '{id_artist}');"""
    return query


def add_link_artist_album(id_artist: str, id_album: str):
    query = f"""
        insert ignore into artist_album (id_artist, id_album) values 
        ('{id_artist}', '{id_album}');
    """
    return query


def add_user(user_email: str, user_name: str, password: str):
    query = f"""
        insert ignore into user (email, username, password, create_time) values 
        ('{user_email}', '{user_name}', '{password}', CURRENT_TIMESTAMP);"""
    return query


def add_favorite_track_to_user(user_email: str, id_track: str):
    query = f"""
        insert ignore into favorite (user_email, id_track) values 
        ('{user_email}', '{id_track}');"""
    return query


def add_link_video_track(video_id: str, track_id: str):
    query = f"""
        insert ignore into video_song values 
        ('{video_id}', '{track_id}');"""
    return query
