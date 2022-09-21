#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  counter = 0
  for x in range(0, len(a)-1):
    if a[x:x+2] == b[x:x+2]:
      counter = counter + 1
  return counter

  print(string_match('xxcaazz', 'xxbaaz'))
  print(string_match('abc', 'abc'))
  print(string_match('abc', 'axc'))