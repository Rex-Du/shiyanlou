"""
decorators:
"""
# author: rexdu
# create: 2020/7/22 21:32
import functools

import redis


def mock_func(*, value):
    """
    # 装饰一个函数，使函数不执行，直接返回指定的值
    example:
    @mock_func(value=100)
    def add(x, y):
        return x + y

    :param value:
    :return:
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return value

        return wrapper

    return decorator


@mock_func(value=100)
def add(x, y):
    return x + y


add(10, 20)


def consumer_lock(*, time_limit):
    """
    锁，限制某个函数的执行频率
    example:
    @consumer_lock(time_limit=10)
    def task():
        return 100
    :param time_limit:
    :return:
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            conn = redis.Redis(host='localhost', port=6379, password='rootroot')
            if conn.set(f'lock: {func.__name__}', 1, ex=time_limit, nx=True):
                return func(*args, **kwargs)

        return wrapper

    return decorator
