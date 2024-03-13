

num = int(input("Enter your number: "))
my_str = ""

if num >= 0 and num < 8640000:
    name = ""
    seconds = num%60
    minutes = (num // 60) % 60
    hours = (num//60//60)%24
    days = (num//60//60//24)
    if days == 1 or (days > 21 and (days % 10) == 1):
        name = "день"
    elif ((days >= 2) and (days < 5)) or (days > 20 and ((days % 10 >= 2) and (days % 10 < 5))):
        name = "дні"
    elif ((days >= 5 and days <= 20) or (days % 10) >= 5) or days == 0:
        name = "днів"

    if seconds < 10:
        seconds = str(seconds).zfill(2)
    if minutes < 10:
        minutes = str(minutes).zfill(2)
    if hours < 10:
        hours = str(hours).zfill(2)

    my_str = "{d} {n}, {h}:{m}:{s}".format(n=name, d=days, h=hours, m=minutes, s=seconds)
    print(my_str)
else:
    print('Incorrect number')



