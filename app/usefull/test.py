import re
from youtube_playlist_downloader.usefull.functions import without_feat, artist_splitter_runtime, feat_finder


def normalizer_of_title(raw_title: str):
    res = re.sub(r'[(][^(]+?[)]', '', raw_title)
    while raw_title != res:
        raw_title = res
        res = re.sub(r'[(][^(]+?[)]', '', raw_title)

    res = re.sub(r'[$]', 's', res)
    res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
    return res

title = 'GIANTS (feat. SOYEON of (G)I-DLE, DUCKWRTH, Thutmose & League of Legends)'
artists = 'True Damage, Becky G, Keke Palmer'
# print(without_feat(title))
# print(normalizer_of_title(title))
print(feat_finder(title))
print(feat_finder(title).replace('feat.', '')[1:-1])
print(artist_splitter_runtime([artists, feat_finder(title).replace('feat.', '')[1:-1]]))
