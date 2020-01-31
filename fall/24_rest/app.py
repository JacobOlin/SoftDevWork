from flask import Flask, render_template
from urllib.request import urlopen
import json
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def root():
    u = urlopen(
    "https://api.nasa.gov/planetary/apod?api_key=Ed3mcpv2KwzF7cfx3ShUHdhsv49LJJQUGHCZzKGy")

    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            pic = data['url'],
                            expln = data['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
