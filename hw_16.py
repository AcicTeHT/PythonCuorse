
def say_hi(name, age):

    res = "Hi. My name is {name} and I'm {age} years old".format(name=name,age=str(age))
    return res


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
