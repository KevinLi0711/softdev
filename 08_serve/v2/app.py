# Karen Shekyan
# SoftDev
# Oct 6, 2022
'''
runs hello_world upon loading page in browser
will print "about to print __name__..." in terminal when page loads
shows "No hablo queso!" on page
'''
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? #This prints to the terminal
    return "No hablo queso!"

app.run()
