import string

name = input("your wariable name:")
pnkt = string.punctuation

name = name.title().replace(" ","")
for i in pnkt:
    for j in name:
        if i == j:
            name = name.replace(j,"")
if len(name) > 140:
    print("#" + name[:140])
else:
    print("#" + name)
