import random

def common_elements():
    x = random.randint(3, 150)
    number_set = {x for x in range(x) if x % 3 == 0}
    number_set_2 = {x for x in range(x) if x % 5 == 0}
    res = number_set.intersection(number_set_2)
    return res

i = common_elements()
print(i)


