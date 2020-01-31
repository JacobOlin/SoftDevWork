from flask import Flask

app = Flask(__name__) #create instance of class Flask



@app.route("/") #assign following fxn to run when root route requested

def hola_mundo():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/English")

def hello_world():
    print(__name__)
    return "I don't speak cheese!"

@app.route("/PigLatin")

def EllohayOrldway():
    print(__name__)
    return "Iyay on'tday eakspay essecha!"

@app.route("/Mandarin")

def nihaoshijie():
    print(__name__)
    return "wo bu hui shuo qi si!"



if __name__ == "__main__":

    app.debug = True

    app.run()
