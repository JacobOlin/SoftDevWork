from flask import Flask, render_template, request, session
app = Flask(__name__)


@app.route("/")
def input():
    #print (request.args["username"])
    return render_template('template.html')

@app.route("/login")
def login():
    print(request.args)
    secret_key = "hi"
    session["hi"] = request.args["username"]
    #print (request.cookies.get(user))
    return render_template('welcome.html')





if __name__ == "__main__":
    app.debug = True
    app.run()
