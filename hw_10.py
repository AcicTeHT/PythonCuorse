import string
import keyword

name = input("Your variables:")
pnkt = string.punctuation
lm_list = keyword.kwlist

if name == "_":
    print("True")
elif not name.islower() or keyword.iskeyword(name):
    print("False")
elif name.isalpha():
    print("true")
elif len(name.split()) > 1:
    print("False")
elif name[0].isdigit() or name.isdigit():
    print("False")
elif name.isalnum():
    print("True")
elif not name.isalpha():
    for i in pnkt:
        for j in name:
            if j == i:
                if j == "_":
                    print("True")
                    continue
                print("False")
