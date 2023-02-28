def fibonacci(n):
    if 0 == n:
        return 0
    elif 1 == n:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)