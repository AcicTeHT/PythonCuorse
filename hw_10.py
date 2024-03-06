import string
import keyword

name = input("your wariable name:")
pnkt = string.punctuation
lm_list = keyword.kwlist

i = 0
while i < len(name):
    if name[i].isspace():
        print("False")
    i += 1
for i in pnkt:
    for j in name:
        if j == "_":
            # print("True")
            continue
        elif i == j:
            print('a')
            # print("False")

if name[0].isdigit() or name.isdigit():
    print("False_1")
elif not name.islower() or keyword.iskeyword(name):
    print("False_2")
else:
    print("True")

