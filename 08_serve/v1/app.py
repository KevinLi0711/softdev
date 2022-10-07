# Karen Shekyan
# SoftDev
# Oct 6, 2022
'''
runs hello_world upon loading page in browser
__name__ doesn't get printed but it was never shown in terminal anyways so it should worrk as normal
shows "No hablo queso!" on page
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()
