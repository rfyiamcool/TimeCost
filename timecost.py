import time
import functools

class TimeCost(object):
    def __init__(self, unit='s', precision=4, logger=None):
        self.start = None
        self.end = None
        self.total = 0
        self.unit = unit
        self.precision = precision
        self.__unitfactor = {'s': 1,
                    'ms': 1000,
                    'us': 1000000}
        self.logger = logger

    def __call__(self, f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        return wrapped

    def __enter__(self):
        if self.unit not in self.__unitfactor:
            raise KeyError('Unsupported time unit.')
        if self.precision < 0:
            raise KeyError('must gte 0')
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.total = (self.end - self.start) * self.__unitfactor[self.unit]
        if self.precision != 0:
            self.total = round(self.total, self.precision)
        else:
            self.total = int(self.total)
        if self.logger:
            self.logger.info('this cost {0}{1}'.format(self.total, self.unit))

    def __str__(self):
        return 'this cost {0}{1}'.format(self.total, self.unit)

