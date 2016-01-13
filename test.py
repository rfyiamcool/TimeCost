from timecost import TimeCost
import logging

def init_logger(logfile):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fmt = '%(asctime)s - %(process)s - %(levelname)s: - %(message)s'
    formatter = logging.Formatter(fmt)
    handler = logging.FileHandler(logfile)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = init_logger('debug')

@TimeCost('s',0,logger)
def test():
    pass

if __name__ == "__main__":
    with TimeCost('s',0) as t:
        resutl = sum(range(100))
    print t.total
    test()

    
