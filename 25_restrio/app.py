from flask import Flask, render_template
from urllib.request import urlopen
import json
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def hi():
    print ("hi")

@app.route("/card")
def card():
    u = urlopen(
    "https://deckofcardsapi.com/api/deck/new/")

    response = u.read()
    data = json.loads(response)
    id = data['deck_id']

    u = urlopen(
    "https://deckofcardsapi.com/api/deck/" + id + "/shuffle/"
    )

    u = urlopen(
    "https://deckofcardsapi.com/api/deck/" +id+ "/draw/?count=2"
    )
    data = json.loads(response)
    return render_template("index.html",
                            pic = data['image'],
                            suit = data['suit'],
                            value = data['value'])

if __name__ == "__main__":
    app.debug = True
    app.run()
