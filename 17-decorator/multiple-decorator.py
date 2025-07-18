import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('before execute decorator1')
        func(*args, **kwargs)
        print('after execute decorator1')
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('before execute decorator2')
        func(*args, **kwargs)
        print('after execute decorator2')
    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')

