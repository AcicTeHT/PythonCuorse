# homeWork_3


num =int(input('enter a five-digit number:'))
last = num % 10
first = num // 10000
second = ((num - (first * 10000)) // 1000)
third = (((num - (first * 10000)) - second * 1000) // 100)
fourth = ((num % 100) //10)
print((last * 10000) + (fourth * 1000)+(third*100)+(second*10)+first)

# first, second, third, fourth, last = last, fourth, third, second, first
