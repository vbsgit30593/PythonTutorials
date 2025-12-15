from clock_decorator import clock


@clock
def factorial(n):
    return 2 if n < 2 else n * factorial(n - 1)

factorial(5)