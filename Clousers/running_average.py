# Create a closure that keeps track of numbers and returns the running average.

def running_average():
    num = []
    def avg(num_):
        num.append(num_)
        return sum(num) // len(num)
    return avg

def running_average():
    total, count = 0, 0
    def avg(num):
        nonlocal total, count
        total += num
        count += 1
        return total // count
    return avg

avg = running_average()

print(avg(10))  # 10
print(avg(20))  # 15
print(avg(30))  # 20


