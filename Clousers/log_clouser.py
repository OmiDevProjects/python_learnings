# Write a function logger(message) that returns another function.

def logger(message):
    def log():
        return f'Log: {message}'
    return log

error_log = logger('File not found!')
success_log = logger('Operation Successful')

print(error_log())
print(success_log())