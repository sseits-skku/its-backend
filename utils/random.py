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
            retval.append(f'{i} {j}')
    for i in COLOR_PARTIAL:
        for j in OPTIONS:
            if j != 'accent-2':
                retval.append(f'{i} {j}')
    return retval


def color_gen(num):
    return np.random.shuffle(_get_color_palette())[:num]
