# n = set(range(10))
# n.add(11)
#
# print(n)

def histogram(s):
    d = dict()
    for i in s:
        if i not in d:
            # print(i)
            d[i] = 1
        else:
            d[i] = d[i] + 1 # або d[c] += 1
    return d
n = ([2, 5, 6, 5, 4, 4, 4, 4, 3, 2, 2, 2, 2, 3])
# n = ("ywte3475eryt3478e477477474")
print(histogram(n))
# variable = {key: value for key in iterable if something}



