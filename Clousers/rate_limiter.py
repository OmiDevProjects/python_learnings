# Create a closure that allows a function to be called only N times.

def API_limit_call(limit):
    count = 0
    def call():
        nonlocal count
        if count >= limit:
            return "Blocked"
        count += 1
        return "Received"
    return call

api_call = API_limit_call(3)

print(api_call())
print(api_call())
print(api_call())
print(api_call())
        
