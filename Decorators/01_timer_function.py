# Timer for function execution
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time_taken = end_time - start_time

        print(f'{func.__name__} ran in {total_time_taken} time.')
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)


example(2)