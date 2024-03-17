import string

my_string = input("Your string: ")

def is_palindrome(text):
    pnkt = set(string.punctuation)
    res = ''.join(i for i in text if (i not in pnkt and i != " ")).lower()
    mod = tuple(res[::-1])
    res = tuple(res)
    return(mod == res)

i = is_palindrome(my_string)
print(i)