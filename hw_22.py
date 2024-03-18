
def difference(*nums):
    lst = tuple(nums)

    if len(lst) == 0:
        return 0

    min_num = min(lst)
    max_num = max(lst)
    res = round(max_num, 2) - round(min_num, 2)

    if max_num != "int":
        return round(res, 2)
    return res


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')