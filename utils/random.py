import numpy as np


COLOR_FULL = [
    'red', 'pink', 'purple',
    'deep-purple', 'indigo',
    'blue', 'light-blue', 'cyan',
    'teal', 'green', 'light-green',
    'lime', 'yellow', 'amber',
    'orange', 'deep-orange',
]
COLOR_PARTIAL = ['brown', 'blue-grey']
OPTIONS = [
    '',  # 원색
    'lighten-2',
    'darken-2',
    'accent-2',  # 채도 상승.
    # 근데 이거는 brown이랑 blue-grey에는 없으니깐 제외시킴
]


def _get_color_palette():
    retval = []
    for i in COLOR_FULL:
        for j in OPTIONS:
            retval.append(f'{i} {j}'.rstrip())
    for i in COLOR_PARTIAL:
        for j in OPTIONS:
            if j != 'accent-2':
                retval.append(f'{i} {j}'.rstrip())
    return retval


def color_gen(num):
    pal = _get_color_palette()
    np.random.shuffle(pal)
    return pal[:num]
