import sys
import random


# print(list(range(10)))

# lst = [4, 6, 8, 7]
# for i in range(len(lst)):
#     print(i)
#     lst[i] = lst[i] + 5
# print(lst)

# print(sys.getsizeof(list(range(10_000_000))))

# print(list(range(3, 10, 2)))

# num = (random.randint(0,100))
# lst = []
# i = 0
# while i < num:
#     lst.append(random.randint(0,50))
#     print(i)
#     i += 1
# print(lst)



# my_list = []
#
# for i in range(random.randint(6,15)):
#     my_list.append(random.randint(1,1000))
# print(my_list)
#
# summa = 0
# for elment in my_list:
#     summa += elment
# print(summa)


# lst = list(range(1, 11))
# print([i * i for i in lst])

matrix = []
for i in range(5):
    col = []
    for j in range(4):
        col.append(random.randint(0, 100))
    matrix.append(col)
print(matrix)