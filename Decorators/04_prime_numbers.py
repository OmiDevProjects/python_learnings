# prime numbers
import time

num = 78203

def is_prime_time_calc(func):
    def wrapper(*args, **kwargs):
        
        attempts = 1000
        
        start = time.perf_counter()
        for _ in range(attempts):
            result = func(*args, **kwargs)
        end = time.perf_counter()
        
        elapsed = end - start
        avg_time = elapsed / attempts
        
        print(f'Time Taken by {func.__name__} is {avg_time:.8f}.')
        return result
    return wrapper

@is_prime_time_calc
def is_prime_optimized(num: int) -> bool:
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return True
        
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
    
@is_prime_time_calc
def is_prime(num: int) -> bool:
    if num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
print('is Prime: ', is_prime(num))
print('is Prime Optimized: ', is_prime_optimized(num))

