'''
JKL: Jeremy Kwok, Kevin Li, Lauren Lee
SoftDev
Dictionaries and randomly accessing values
2022-09-22
time spent: .75 hours (in-class time)
DISCO
    - Typecasting something into an int is done by int(<thing you want to typecast>)
    - list() can take a dictionary parameter and return a list of keys
    - .choice() takes a list parameter and returns a random value in the list
    - .keys and .values return a view object, and you can't access the values in a view object using an index (ex: krewes.keys()[0] doesn't work)
QCC
    - Dictionaries are kinda like 2d arrays except the other dimension can have variables of another data type
OPS SUMMARY
    Randint:
    - Get a list of the keys in krewes
    - Take the value at a random index from 0 to 2 of the list of keys
    - Use that key to access the corresponding list and then return the devo at a random index from 0 to 1 less than the length of the list
    Random:
    - Same as above but using .random and typecasting instead of randint
    Choice:
    - use .choice on the list of keys
    - use .choice on the list corresponding to that key

'''
import random as rng
krewes = {2:['a','b','c'], 7:['y','z'], 8:['j', 'k', 'l']}

def choose():
    #using randint
    '''
    period = list(krewes)[rng.randint(0,2)]
    listofdevos = krewes[period]
    devo = listofdevos[rng.randint(0,len(listofdevos) - 1)]
    '''

    #using random
    '''
    period = list(krewes)[int(rng.random() * 3)]
    listofdevos = krewes[period]
    devo = listofdevos[int(rng.random() * len(listofdevos))]
    '''
    
    #using choice

    period = rng.choice(list(krewes)) #choose a random key
    devo = rng.choice(krewes[period]) #choose a random index of the list that corresponds with the chosen key
    

    return devo
    #return rng.choice(krewes[rng.choice([2,7,8])])

print(choose())