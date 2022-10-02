import random
"""
Ian Jiang, Kevin Li
06_py-csv
2022-9-28
time spent: .5 hours
DISCO: 
    - .update() is the method of adding things into a dicitonary
    - you can create an empty dictionary by just putting nothing inside the curly brackets
    - (from piazza) random has built-in weighted random functionality
    - .rsplit() allows you to split, starting from the right side of a string, as opposed .split(), which starts from the left
    - the second parameter of .rsplit() and .split() specifies how many times to split
QCC: 
    - when viewed on github, csv files look like they have a dictionary-like structure. Is there a way to take advantage of that instead of reading and splitting?
ALGO
    1. Read the file and split by line
    2. Remove the heading as well as anything else that shouldn't be in the dictionary
    3. Separate the jobs from their percentage and place them as pairs in a dictionary
    4. Get lists of the jobs and values
    5. Generate a random number between 0 and 99.8(the total percentage)
    6. Iterate through the list of values and while the random number is greater than 0, subtract each value from the random number and add 1 to a counter each time a value is subtracted
        note: because there will always be at least 1 subtraction (random number can't be less than 0), the counter starts at -1 so that the smallest number it can end at is 0
    7. Once the random number is 0 or less, return the job at the index specified by the counter
"""


def choice():
    occupations_file = open("occupations.csv", "r")
    occupations_file = occupations_file.read()
    occupations_file = occupations_file.split("\n")
    occupations_file.remove("Job Class,Percentage")
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