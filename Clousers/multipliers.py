# Multipliers

def multiplier(num):
    def times(x):
        return x * num
    return times

print(multiplier(3)(4))