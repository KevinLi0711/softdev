#Adorable Didactic Elephants: Anjini Katari, Kevin Li
#SoftDev
#K20 -- API keys
#2022-11-21
#time spent: <elapsed time in hours, rounded to nearest tenth>

from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    print(request.url)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()