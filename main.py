import math

def fun(n):

    if n == 0:
        return 6
    elif n == 1:
        return 6
    else:
        return (math.sin(fun(n - 1)) - math.tan(fun(n - 2)))


print(f"{fun(6):.2e}")

