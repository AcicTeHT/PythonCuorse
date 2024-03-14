
num = input("Enter your number: ")
mod = ([int(i) for i in num])
mod = tuple(mod)

while mod:
    if len(mod) == 4:
        res = mod[0] * mod[1] * mod[2] * mod[3]
        res = str(res)
        mod = tuple(res)
        mod = ([int(i) for i in mod])
        # print(res)
    elif len(mod) == 3:
        res = mod[0] * mod[1] * mod[2]
        res = str(res)
        mod = tuple(res)
        mod = ([int(i) for i in mod])
        # print(res)
    elif len(mod) == 2:
        res = mod[0] * mod[1]
        res = str(res)
        mod = tuple(res)
        mod = ([int(i) for i in mod])
        # print(res)
    elif len(mod) == 1:
        print(mod[0])
        break


