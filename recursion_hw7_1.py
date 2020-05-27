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

print(mult_3(7))

"""
mult_3(7)
 => mult_3(6) + 3 
    => mult_3(5) + 3
       => mult_3(4) + 3
          => mult_3(3) +3 = 9 + 3
             => mult_3(2) + 3 = 9
                => mult_3(1) + 3 = 6
                   => 3
"""
