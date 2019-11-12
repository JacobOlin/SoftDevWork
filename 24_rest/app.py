from flask import Flask, render_template
import urllib3, json
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def root():
    u = urllib3.urlopen(
    "https://api.nasa.gov/planetary/apod?api_key=Ed3mcpv2KwzF7cfx3ShUHdhsv49LJJQUGHCZzKGy")

    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            pic = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
