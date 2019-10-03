from flask import Flask, render_template, request, session
app = Flask(__name__)

users = {'adminUser' : 'password'}


@app.route("/")
def input():
    #print (request.args["username"])
    return render_template('template.html')

@app.route("/login")
def login():
    print(request.args)
    #secret_key = "hi"
    #session["hi"] = request.args["username"]
    #print (request.cookies.get(user))
    if users[request.args["Username"]] == request.args["Password"]:
        return render_template('welcome.html',
                                user = request.args["Username"] )
    else :
        return render_template('invalid.html')





if __name__ == "__main__":
    app.debug = True
    app.run()
