import re


def calc_duration(duration: str):
    dur = duration.split(':')
    dur.reverse()
    k = [1, 60, 3600]
    res = 0
    for i, elem in enumerate(dur[:3]):
        res += int(elem) * k[i]
    return res


def feat_finder(string: str):
    """
    ->"abra (feat. (q)art1, art2) cadabra (123)"

    <-"(feat. (q)art1, art2)"

    :param string: строка из которой нужно достать feat
    :return: Optional[str]
    """
    try:
        beg = re.search(r'\(feat\..*?\)', string).start()
        count = 0
        length = 0
        for char in string[beg:]:
            if char == '(':
                count += 1
            if char == ')':
                count -= 1
            length += 1
            if count == 0:
                break

        return string[beg:beg + length].strip()
    except AttributeError:
        return ''


def without_feat(raw_str: str):
    feat = feat_finder(raw_str)
    if feat != '':
        return raw_str.replace(feat, '').strip()
    return raw_str


def artist_splitter(artists: list):
    res_artists = []
    if artists:
        for artist in artists:
            for art in re.sub(' feat.', ',', artist).split(','):
                art = re.sub(" +", ' ', art).strip()
                if art not in res_artists and art != '':
                    res_artists.append(art)
        return res_artists
    else:
        return []


def artist_splitter_runtime(artists: list):
    res_artists = []
    if artists:
        for artist in artists:
            for art in re.split('[,&]', re.sub(' feat.', ',', artist)):
                art = re.sub(" +", ' ', art).replace('$', 's').lower().strip()
                if art not in res_artists and art != '':
                    res_artists.append(art)
        return res_artists
    else:
        return []


def artist_fixer(artists: list):
    res = []
    for artist in artists:
        artist = re.sub('The Black Eyed Peas', 'Black Eyed Peas', artist)
        artist = re.sub('[Гг]руппа', '', artist)
        artist = re.sub('30 Seconds To Mars', 'Thirty Seconds to Mars', artist)
        artist = artist.replace('"', '').strip()
        if artist not in res:
            res.append(artist)
    return res


def normalized(raw_string: str) -> str:
    raw_string = raw_string.replace('[', '(').replace(']', ')')
    res = re.sub(r'[(][^(]+?[)]', '', raw_string)
    while raw_string != res:
        raw_string = res
        res = re.sub(r'[(][^(]+?[)]', '', raw_string)
    res = re.sub(" +", ' ', re.sub(r'[Ёё]', 'е', re.sub(r'[\W]', "", res))).lower().strip()
    return res


def soft_normalized(raw_str: str):
    res = re.sub(r'[(][^(]*?[)]', '', raw_str)
    while raw_str != res:
        raw_str = res
        res = re.sub(r'[(][^(]*?[)]', '', raw_str)
    return res.strip()
