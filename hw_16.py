name = input("Your name: ")
age = int(input("Your age: "))

name = name.capitalize()

def sey_hi():
    if age > 0:
        res = "Hi. My name is {name} and I'm {age} years old ".format(name=name,age=age)
        print(res)
    else:
        print("Age is not positive")
sey_hi()