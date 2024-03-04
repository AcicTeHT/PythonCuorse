import string
import keyword

name = input("your wariable name:")
pnkt = string.punctuation
lm_list = keyword.kwlist

# print(pnkt)
print(lm_list)

# if name[0].isdigit() or name.isdigit():
#     print("False")
if keyword.iskeyword(name):
    print(name)
if name.istitle():
    print(name)