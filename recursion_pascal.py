def pascal_triangle(n: int) -> []:
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n - 1)
        last_row = result[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)
    return result


stopper = 8
res = pascal_triangle(stopper)
for idx, line in enumerate(res):
    indent = (stopper - idx + 1)
    indent = " " * indent
    print(indent + ' '.join(str(x) for x in line))


# ####E ENUMERATE LIST #########
L = ['apples', 'bananas', 'oranges']
for idx, val in enumerate(L):
    print("index is %d and value is %s" % (idx, val))
# #############################


# #############################
# COUNT DIGITS IN A NUMBER
def digits_count(n: int) -> int:
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count


# #############################
def count_digits_in_list_row(row: []) -> int:
    cnt = 0
    for r in row:
        cnt = cnt + digits_count(r) + 1
    return cnt - 1



adj = 0
if len(res) > 0:
    adj = count_digits_in_list_row(res[-1])