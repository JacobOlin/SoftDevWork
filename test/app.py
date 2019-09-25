from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route("/")
def occupation():
    print(app)
    print(request)
    print(request.args)

    return render_template("/test.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
