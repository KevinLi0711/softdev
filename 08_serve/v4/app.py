# Karen Shekyan
# SoftDev
# Oct 6, 2022
'''
runs hello_world upon loading page in browser
will print "about to print __name__..." and __main__ in terminal when page loads
will print lines about debug mode
nothing new will happen because __name__ appears to be __main__ so line 22 won't stop us in this case
shows "No hablo queso!" on page

Didn't notice a change
How would you import this file to get different results?
'''
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
