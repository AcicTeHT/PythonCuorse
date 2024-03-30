def is_even(number):

    # variant____1

    # l = str(number)
    # l = int(l[-1])
    # if l != 1 and l != 3 and l != 5 and l != 7 and l != 9:
    #     return True
    # return False


    # variant___2

    # if number & 1 == 0:
    #     return True
    # return False


    # variant____3

    if int(bin(number)[-1]) == 0:
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("ok")
