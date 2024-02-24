
# homeWork_2

# num =int(input('enter a four-digit number:'))
# last = num % 10
# first = int(num/1000)
# third = int((num - last)%100/10)
# second = int(((num-last)-(third*10) - (first * 1000))/100)
# print(first)
# print(second)
# print(third)
# print(last)



# homeWork_3


num =int(input('enter a five-digit number:'))
last = num % 10
first = num // 10000
second = ((num - (first * 10000)) // 1000)
third = (((num - (first * 10000)) - second * 1000) // 100)
fourth = ((num % 100) //10)
print((last * 10000) + (fourth * 1000)+(third*100)+(second*10)+first)


