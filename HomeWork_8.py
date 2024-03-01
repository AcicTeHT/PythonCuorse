import math
# lst = [1, 2, 3, 4, 8, 9, 0, 3, 5]
lst = [1, 2, 3]
# lst = []
res = 0
if len(lst) == 0:
    res = 0
    print(res)
elif len(lst) > 0:
    l = sum(lst[::2])
    d = lst.pop()
    res = l * d

    print(res)
