'''
JKL: Jeremy Kwok, Kevin Li, Lauren Lee
SoftDev
Dictionaries and randomly accessing values
2022-10-03
time spent: 0.2
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. java
1. "/" is used in setting apart directories in file paths. "/" may tell the app where to look to run the code. A single "/" may represent the current directory.
2. every time reloaded, whatever is in the print function is printed in the terminal
3. __main__
4. prints on webpage because it is being returned rather than printed
5. java
...

INVESTIGATIVE APPROACH:
- we related the knowledge we knew from other languages to make inferences
- thought about the significance in the difference between print and return
'''
