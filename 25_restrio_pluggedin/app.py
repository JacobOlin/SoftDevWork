from flask import Flask, render_template
#from urllib.request import Request, urlopen
import random, urllib, json
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def hi():
    return "hi"


@app.route("/nhl")
def nhl():
    rng = random.randrange(1,29)
    if rng > 10:
        rng += 1
    u = urllib.request.urlopen(
    'https://statsapi.web.nhl.com/api/v1/teams/' + str(rng))

    response = u.read()
    data = json.loads(response)

    return render_template("nhl.html",
                            name = data['teams'][0]['name'],
                            loc = data['teams'][0]['locationName'],
                            conf = data['teams'][0]['conference']['name'],
                            div = data['teams'][0]['division']['name'])

@app.route("/RickAndMorty")
def randm():
    rng = random.randrange(0,19)

    u = urllib.request.urlopen(
    "https://rickandmortyapi.com/api/character/" + str(rng)
    )

    response = u.read()
    data = json.loads(response)

    return render_template("rick.html",
                            name = data["name"],
                            alive = data["status"],
                            species = data["species"],
                            pic = data["image"],
                            eps = len(data["episode"]))
@app.route("/superheroes")
def super():
    rng = random.randrange(1,732)
    url  =  "https://superheroapi.com/api/2503373653110667/" + str(rng)

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    req = urllib.request.Request(url, headers=hdr)
    data = json.loads( urllib.request.urlopen(req).read())

    return render_template("super.html",
                            name = data["name"],
                            pic = data["image"]["url"],
                            birth = data['biography']['place-of-birth'],
                            publish = data['biography']['publisher'],
                            connecs = data['connections']['group-affiliation']
                            )



if __name__ == "__main__":
    app.debug = True
    app.run()
