from functools import lru_cache

@lru_cache()
def fib(n):
    if n < 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

for i in range(10):
    print(fib(i))

print(fib(40))
