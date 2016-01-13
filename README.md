# TimeCost
计算函数的时间消耗

#Usage:

使用with关键词和装饰器
```
from timecost import TimeCost

@TimeCost('s',0)
def test():
    print 123

if __name__ == "__main__":
    with TimeCost('s',0) as t:
        resutl = sum(range(100))
    print t.total
    print test()
```    
另外装饰器统计时间的方法支持传递logger对象的.
```
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
```
