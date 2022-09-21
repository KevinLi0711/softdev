#Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) == 1:
    return str
  if len(str) == 2:
    first = str[:1]
    last = str[len(str)-1:len(str)]
    return last+first
  else:
    first = str[:1]
    last = str[len(str)-1:len(str)]
    middle = str[1:len(str)-1]
    return last + middle + first

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
