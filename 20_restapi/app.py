#Adorable Didactic Elephants: Anjini Katari, Kevin Li
#SoftDev
#K20 -- API keys
#2022-11-21
#time spent: <elapsed time in hours, rounded to nearest tenth>

from flask import Flask
from flask import request
from flask import render_template
import requests
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    file = open("key_nasa.txt", 'r')
    file = file.read()
    print(file)

    x = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + file)
    print(x)
    print(x.request)
    print(x.json())
    #print(x.content)
    json = x.json()
    image_url = json["url"]
    print(image_url)

    return render_template("main.html", image = image_url)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()