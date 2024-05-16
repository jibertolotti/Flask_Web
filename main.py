from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Bienvenido!</h1>', "<h1>En esta página hablaremos sobre Asistente, un bot de Discord</h1>"
    

#@app.route("/info")

app.run(debug=True)