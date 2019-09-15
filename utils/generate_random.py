import random
from numpy.random import default_rng
from datetime import datetime as dt

from lorem import sentence, paragraph
from names import get_first_name


def get_bulk(num, func):
    return [*map(lambda x: func(), [None] * num)]


class RandomGenerator:
    def __init__(self, num, numpy=False):
        self.num = num
        self.numpy = numpy
        if numpy:
            r = default_rng()
            self.randint = r.integers
            self.choice = r.choice
        else:
            def randint(*args, **kwargs):
                size = kwargs.get('size')
                if size:
                    retval = []
                    for i in range(size):
                        retval.append(random.randrange(*args))
                    return retval
                else:
                    return random.randrange(*args)

            def choice(*args, **kwargs):
                size = kwargs.get('size')
                if size:
                    retval = []
                    for i in range(size):
                        retval.append(random.choice(*args))
                    return retval
                else:
                    return random.randint(*args)

            self.randint = randint
            self.choice = choice

    def email(self):
        name = get_bulk(self.num, get_first_name)
        company = self.choice(
            ['google', 'daum', 'naver', 'hotmail'],
            size=self.num
        )
        domain = self.choice(
            ['org', 'net', 'com', 'edu', 'gov'],
            size=self.num
        )
        ret = [f'{a}@{b}.{c}' for a, b, c in zip(name, company, domain)]

        return ret

    def boolean(self):
        return self.choice((True, False), size=self.num)

    def datetime(self):
        return get_bulk(
            self.num,
            lambda: dt(
                self.randint(2000, 2100), self.randint(1, 13),
                self.randint(1, 28), self.randint(0, 23),
                self.randint(0, 59), self.randint(0, 59)
            )
        )

    def enum(self, e):
        return self.choice(e, size=self.num)

    def content(self):
        return get_bulk(
            self.num,
            paragraph
        )

    def title(self):
        return get_bulk(
            self.num,
            sentence
        )

    def passwd(self):
        return get_bulk(
            self.num,
            sentence
        )

    def phone_num(self):
        return [*map(lambda a: f'010{a:0<8}',
                     self.randint(0, 100000000, size=self.num))]

    def ip_addr(self):
        if not self.numpy:
            raise NotImplementedError('Sorry...T.T')
        else:
            return [*map(lambda a: f'{0}.{1}.{2}.{3}'.format(*a),
                         self.randint(0, 256, size=(self.num, 4)))]

    def skku_id(self):
        return self.randint(2000000000, 2100000000, size=self.num)

    def nickname(self):
        return get_bulk(
            self.num,
            get_first_name
        )
