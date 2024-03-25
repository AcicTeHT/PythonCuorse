

# log_file = ["error", "type_error", "my_error", "no"]
#
# err_gen = (st for st in log_file if "error" in st)
# print(err_gen)
# for item in err_gen:
#     print(item)

def f_gen(m):
    s = 1
    for n in range(1,m):
        yield n**2 + s
        s += 1
a = f_gen(5)
print(a)
for i in a:
    print(i)


