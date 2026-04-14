# Find the max of 3 Numbers

import time

def timer(func):
    def wrapper(*args, **kwargs):
        max_attempt = 1000
        
        start = time.perf_counter()
        for _ in range(max_attempt):
            result = func(*args, **kwargs)
        end = time.perf_counter()
        
        elasped = end - start
        avgtime = elasped / max_attempt
        
        print(f'Time taken by {func.__name__} is {avgtime:.8f}.')
        return result
    return wrapper

@timer
def max_of_three_brute(num1: int, num2: int, num3: int) -> bool:
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
        
print(f'Max: {max_of_three_brute(3, 87, 850)}')

@timer
def max_of_three(num1: int, num2: int, num3: int) -> bool:
    max_val = num1 if num1 > num2 else num2
    return max_val if max_val > num3 else num3
    
print(f'Max: {max_of_three(3, 97, 581)}')

@timer
def max_of_three_n_numbers(nums):
    max_value = nums[0]
    for num in nums:
        if max_value < num:
            max_value = num
    return max_value

print(f'Max of 3: {max_of_three_n_numbers([3, 97, 581, 272])}')
print(f'Max of 4: {max_of_three_n_numbers([3, 97, 581, 272, 276])}')
