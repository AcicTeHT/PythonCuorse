num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number:: "))
sign = input("your sign")

if sign == "*":
    print(num1*num2)
elif sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "/" and num2 != 0:
    print(num1//num2)
else:
    print("You can't divide by 0")


# Alternative option
# elif sign == "/":
#     if num2 == 0:
#         print("You can't divide by 0")
#     else:
#         print(num1//num2)
