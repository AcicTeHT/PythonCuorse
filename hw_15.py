

num = int(input("Enter your number: "))
my_str = ""

if num >= 0 and num < 8640000:
    minutes = num // 60
    if minutes > 59:
        hourse = minutes % 60
        print(hourse)
    print(minutes)
    print('ok')
else:
    print('Incorrect number')

