# Cache the processed data
import time

def cache(func):
    cache_value = {}
    def wrapper(*args, **kwargs):
        print(cache_value)
        if args in cache_value:
            return cache_value[args]

        result = func(*args, **kwargs)

        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_execution(a, b):
    time.sleep(4)
    return a + b

print(long_running_execution(2, 3))
print(long_running_execution(4, 5))
print(long_running_execution(2, 3))
