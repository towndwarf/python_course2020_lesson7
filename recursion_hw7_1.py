# f (n) = 3 * n
# =>
# f(1) = 3,
# f(n+1) = f(n) + 3

def mult_3(n: int) -> int:
    if n == 1:
        print('DBG: stack = stopper reached')
        return 3
    else:
        print(f'DBG: stack = {n}')
        return mult_3(n - 1) + 3


print(mult_3(10))
