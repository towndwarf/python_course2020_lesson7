# returns the sum of the first n prime integers; (similiar to the factorial function!)


# ==============================
# A prime number is a natural number greater than 1 and
# it does not have any divisor other than 1 and itself.
def is_prime(num: int) -> bool:
    if num == 0 or num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True


def sum_primes(n: int) -> int:
    if n < 1:
        print('DBG: stack = stopper reached: 2')
        return 0
    else:
        # print(f'DBG: stack = {n}')
        if is_prime(n):
            print(f'PRIME:{n}')
            return n + sum_primes(n - 1)
        else:
            return sum_primes(n - 1)


sum_with_no_recursion = 0
str_ret = ''
for prn in filter(is_prime, range(1, 21)):
    sum_with_no_recursion += prn
    str_ret += str(prn) + ' + '
if len(str_ret) > 3:
    str_ret = str_ret[:-3]
print(f'No recursion used:{str_ret} = {sum_with_no_recursion}')

print(f'Sum of 20 primes = {sum_primes(20)}')