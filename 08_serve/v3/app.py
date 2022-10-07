# Karen Shekyan
# SoftDev
# Oct 6, 2022
'''
runs hello_world upon loading page in browser
will print "about to print __name__..." and __main__ in terminal when page loads
will print a line about debug mode
shows "No hablo queso!" on page

in debug mode, changes made to the code take effect upon reloading the page
everytime a change is saved, the terminal says
detected change in <pathtofile>
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 139-862-512
'''
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? #This prints to the terminal
    return "No hablo queso!"

app.debug = True
app.run()
