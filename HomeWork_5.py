# first_list = []
# first_list = [1, 2, 3, 4, 5, 6, 7]
# first_list = [1, 2, 3, 4, 5, 6]
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
l = []
r = []
my_list = []


if len(first_list) % 2 == 0:
    step = len(first_list) // 2
    step_finish = len(first_list)+1
    r = first_list[step:step_finish]
    l = first_list[:step]
    my_list.append(l)
    my_list.append(r)
    print(my_list)
elif len(first_list) % 2 == 1:
    step_2 = (round(len(first_list) / 2 + 0.5))
    r = first_list[step_2:99]
    l = first_list[:step_2]
    my_list.append(l)
    my_list.append(r)
    print(my_list)

