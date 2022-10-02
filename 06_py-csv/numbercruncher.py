#from itertools import count
import random
#from traceback import print_tb
#import random as random


def choice():
    occupations_file = open("occupations.csv", "r")
    occupations_file = occupations_file.read()
    occupations_file = occupations_file.split("\n")
    occupations_file.remove("Job Class,Percentage")
    occupations_file.remove("")
    #print(occupations_file)

    dictionary = {}
    for x in occupations_file:
        #iterate from the right of the string
        #find the first comma from the right
        x = x.rsplit(",", 1)
        #print(x)

        dictionary.update({x[0]:x[1]})
    
    #generate a random number 0 and 99.8
    #subtract the value of the percents from that number until the number is <=0
    #when the number is <=0, return the current key value pair
    number = random.random() * 99.8
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    counter = -1
    for x in values:
        if number > 0:
            number = number - float(x)
            counter = counter + 1
        else:
            break
    return keys[counter] 

print(choice())