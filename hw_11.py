


i = 0
while i < 1:
    question = input("Do you want to perform another calculation? y  " )
    if question == "y":
        num1 = int(input("Please enter first number: "))
        num2 = int(input("Please enter second number:: "))
        sign = input("your sign")

        if sign == "*":
            print(num1 * num2)
        elif sign == "+":
            print(num1 + num2)
        elif sign == "-":
            print(num1 - num2)
        elif sign == "/" and num2 != 0:
            print(num1 // num2)
        else:
            print("You can't divide by 0")
    else:
        i = 1





