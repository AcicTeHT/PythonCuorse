
import string

letters = input('Enter your letters: ')
alist = list(string.ascii_letters)

start = alist.index(letters[0])
end = alist.index(letters[-1])
blist = alist[start:end+1]

result = ''
for i in blist:
    result += i

print(result)





