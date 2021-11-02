# def search_artist(tr):
#     # spotify issue (can't use keyword match if there's "'" in query)
#     title = tr.title.replace("'", "")
#
#     artist_idx = 0
#     for artist in tr.artists:
#         artist_idx += 1
#
#         artist = artist.replace("'", "")
#         q = f'artist:"{artist}" track:"{title}"'
#
#         idx = 0
#         if tr.albums:
#             for album in tr.albums:
#                 idx += 1
#
#                 album = album.replace("'", "")
#                 result = spotify.search(q + f' album:{album}', limit=1, type='artist')
#                 items = result["tracks"]["items"]
#
#                 if len(items) > 0:
#                     track = SpotifyTrack(items[0])
#                     if idx > 1:
#                         print(f'using album {idx} for track ({track.album}): {tr.title} - {tr.artist}')
#
#                     # track is found for album, as expected
#                     return track
#
#         # album search unsuccessful, try without
#         result = spotify.search(q, limit=1, type='artist')
#         items = result["artists"]["items"]
#
#         if len(items) > 0:
#             track = SpotifyTrack(items[0])
#
#             if tr.albums and len(tr.albums) > 0:
#                 print(f'no albums for track ({track.album} not in {tr.albums}): {tr.title} - {tr.artist}')
#
#             if artist_idx > 1:
#                 print(f'using artist {artist_idx} for track ({track.artist}): {tr.title} - {tr.artist}')
#
#             return track
#     return


# def search_album(music_track: MusicTrack):
#     for artist in music_track.artists:
#         result = spotify.search(q=f"'{artist}' '{music_track.album}'", limit=5, type='album')
#         if len(result['albums']['items']) == 0:
#             result = spotify.search(q=f"{music_track.title} {artist}", limit=5, type='album')
#             if len(result['albums']['items']) != 0:
#                 items = result['albums']['items']
#                 for item in items:
#                     print(item)
#                 return items


# if __name__ == "__main__":
    #  We own it -|- 2 Chainz -|- How many chainz ?
    # Break Your Heart -|- Taio Cruz -|- Break Your Heart (Deluxe)
    # Go To Hell, For Heaven's Sake", 'Bring Me The Horizon', '2004 - 2013
    # t = MusicTrack(title="Break Your Heart", artists=["Taio Cruz", 'Ludacris'], album="Break Your Heart (Deluxe)")
    # tracks = search_track(t)
    # t = search_artist(t)
    # for t in tracks:
    #     if t:
    #         print()
    #         print(t.sp_url)
    #         print(t.title)
    #         print(t.album)
    #         print(t.alb_url)
    #         print(t.alb_type)
    #         print(t.release_year)
    #         print(t.track_number, 'of', t.total_tracks)
    #         print(t.artists)
    #         print(t.cover_art)
    #         # print(t.spotify_url)
    #     else:
    #         print(f'track not found')
    # search_album(t)
