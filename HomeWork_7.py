# lst = [1, 2, 0, 3, 4, 0, 0, 4]
# lst = [0]
lst = []


n = lst.count(0)
i = 0
while i < n:
    lst.remove(0)
    lst.append(0)
    i += 1
print(lst)