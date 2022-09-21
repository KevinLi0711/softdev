# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
    retval = ""
    for x in range(len(str)):
        if (x % 2 == 0):
            retval = retval + str[x]
    return retval

print(string_bits("hello"))