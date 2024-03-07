import string
import keyword

name = input("your wariable name:")
pnkt = string.punctuation
lm_list = keyword.kwlist



# print("true_1")

if len(name.split()) > 1:
    print("False_1")
elif name[0].isdigit() or name.isdigit():
    print("False_3")
elif name.isalpha():
    if not name.islower() or keyword.iskeyword(name):
        print("False_2")
elif not name.isalpha():
    for i in pnkt:
        for j in name:
            if j == "_":
                continue
            elif i == j:
                print("False")
else:
    print("True_2")





# for i in pnkt:
#     for j in name:
#         if j == "_":
#             continue
#         elif i == j:
#             print("False")
# if len(name.split()) > 1:
#     print("False")
# elif name[0].isdigit() or name.isdigit():
#     print("False_1")
# elif not name.islower() or keyword.iskeyword(name):
#     print("False_2")
# else:
#     print("True")