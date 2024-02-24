
homeWork_2

num =int(input('enter a four-digit number:'))
last = num % 10
first = int(num/1000)
third = int((num - last)%100/10)
second = int(((num-last)-(third*10) - (first * 1000))/100)
print(first)
print(second)
print(third)
print(last)






