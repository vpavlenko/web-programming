def my_lru_cache(wrapped_function):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = wrapped_function(*args)
        return cache[args]

    return wrapper


@my_lru_cache
def fib(n):
    if n < 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


for i in range(10):
    print(fib(i))

print(fib(40))
