
from functools import wraps


def without_wraps(func):
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper

def with_wraps(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper


@without_wraps
def my_func_a():
    """Here is my_func_a doc string text."""
    pass

@with_wraps
def my_func_b():
    """Here is my_func_b doc string text."""
    pass


print my_func_a.__doc__
print my_func_a.__name__

print my_func_b.__doc__
print my_func_b.__name__
