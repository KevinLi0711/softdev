"""
Ian Jiang, Kevin Li
05_bitstream
2022-9-28
time spent:

DISCO: open(file, mode) opens a file with the specified mode.
       The file can be accessed using read(). str.strip() will get rid of
       empty spaces in str. dict.update() appends the key and value pair or
       updates the value if the key exists. list.append() adds a new value to
       a list
QCC: If we read a file containing a string, the string will contain a \n at the end
     Why is that there and is there a way to remove it without using strip()?
"""

import random

def choose():
    d = {}
    krewes = open("krewes.txt","r")
    krewes = krewes.read()
    krewes = krewes.strip()
    krewes = krewes.split("@@@")
    for i in krewes:
        i = i.split("$$$")
        period = i[0]
        name = i[1]
        ducky = i[2]
        if period not in d.keys():
            d.update({period: []})
        d[period].append([name,ducky])
    rand_key = random.choice(list(d.keys()))
    rand_val = random.choice(d[rand_key])
    print (str(rand_val[0] + ", " + rand_key + ", " + rand_val[1]))

choose()