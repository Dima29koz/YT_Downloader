def get_track_info_by_album_name(album_name: str):
    """получить информацию о треках по названию альбома"""
    query = f"""
        select track.title, album.album_title, artists.name 
        from track, album, album_track, artists, track_artists
        where 
        album.album_title = '{album_name}' and
        track.id_track = album_track.id_track and
        album.id_album = album_track.id_album and
        artists.id_artist = track_artists.id_artist and
        track_artists.id_track = track.id_track;
    """
    return query


def get_track_info():
    """получить информацию о всех треках"""
    query = """
        select track.title, album.album_title, artists.name 
        from track, album, album_track, artists, track_artists
        where 
        track.id_track = album_track.id_track and
        album.id_album = album_track.id_album and
        artists.id_artist = track_artists.id_artist and
        track_artists.id_track = track.id_track;       
    """
    return query


def get_track_info_by_user(user_email: str):
    """получить информацию о треках находящихся в избранном у пользователя _user_email_"""
    query = f"""
        select track.title, album.album_title, artists.name 
        from track, album, album_track, artists, track_artists, favorite
        where 
        favorite.user_email = '{user_email}' and
        track.id_track = favorite.id_track and
        track.id_track = album_track.id_track and
        album.id_album = album_track.id_album and
        artists.id_artist = track_artists.id_artist and
        track_artists.id_track = track.id_track;
    """
    return query


def get_track_information_by_arist_name(artist_name: str):
    """получить информацию о треке по названию артиста"""
    query = f"""select track.title, album.album_title, artists.name 
        from track, album, album_track, artists, track_artists
        where 
        artists.name like '{artist_name}' and
        track.id_track = album_track.id_track and
        album.id_album = album_track.id_album and
        artists.id_artist = track_artists.id_artist and
        track_artists.id_track = track.id_track;
    """
    return query


def get_album_info_by_artist_name(artist_name: str):
    """получить информацию о альбоме по названию артиста"""
    query = f"""
        select album_title from album, artist_album, artists
        where
        artists.name like '{artist_name}' and
        artist_album.id_album = album.id_album and
        artist_album.id_artist = artists.id_artist;
    """
    return query


def get_user_data_by_email(email: str):
    """получить информацию о пользователе по email"""
    query = f"""
            select email, password from user
            where
            email='{email}';
        """
    return query
