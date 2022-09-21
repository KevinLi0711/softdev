#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  counter = 0
  last = str[len(str)-2: len(str)]
  for x in range(len(str)-2):
      if str[x:x+2] == last:
        counter = counter + 1
  return counter

print(last2("hixxhi"))
print(last2("xaxxaxaxx"))
print(last2("axxxaaxx"))