import random
lst = []
n = random.randint(3,10)
i = 0
while i < n:
    lst.append(random.randint(3,10))
    i += 1
# print(lst)

r = lst.pop(-2)
res = lst[0:3:2]
res.append(r)
print(res)

