

num = int(input("Enter your number: "))
my_str = ""

if num >= 0 or num < 8640000:
    name = ""
    seconds = num%60
    minutes = (num // 60) % 60
    hours = (num//60//60)%24
    days = (num//60//60//24)
    if days == 1 or (days > 10 and (days % 10) == 1):
        name = "день"
    elif days >= 2 or days < 5 :
        name = "дні"
    elif (days >= 5 or (days % 10) >= 5) or (days <=  or days == 0) or (days == 0 or (days % 10) == 1):
        name = "днів"
    # elif (days % 10) >= 5 and days <= 20 or days == 0:
    #     name = "днів"

    my_str = "{d}:{n}, {h}:{m}:{s}".format(n=name, d=days, h=hours, m=minutes, s=seconds)
    print(my_str)
    print(days % 10)
else:
    print('Incorrect number')



