my_list = [1, 2, 3, 4,]
# my_list = [1]
# my_list = []

new_list = []
if len(my_list) > 0:
    lastElement = my_list.pop()
    new_list.append(lastElement)
    new_list.extend(my_list)
    print(new_list)
else:
    print(my_list)
