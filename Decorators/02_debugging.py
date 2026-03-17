# Debugging the parameters of the functions

def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        print(f'Function: {func.__name__} ran with arguments: {args_values} and kwargs: {kwargs_values}')
        return func(*args, **kwargs)
    return wrapper


@debug
def greet(name, greet='Hello '):
    return greet + name


greet('Mahima', greet="GoodMorning")