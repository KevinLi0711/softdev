#Adorable Didactic Elephants: Anjini Katari, Kevin Li
#SoftDev
#K20 -- API keys
#2022-11-21
#time spent: <elapsed time in hours, rounded to nearest tenth>

from flask import Flask
from flask import request
from flask import render_template
import requests
import playsound
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    owen_wilson = requests.get("https://owen-wilson-wow-api.onrender.com/wows/random")
    owen_wilson = owen_wilson.json()
    wow = owen_wilson[0]['audio']
    playsound.playsound(wow)

    return "wow"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()