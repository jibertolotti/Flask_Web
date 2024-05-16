from flask import Flask

app = Flask(__name__)

@app.route("/")
def beggining():
    return "<h1>Bienvenido!</h1>"\
           "<h1>En esta página hablaremos sobre Asistente, un bot de Discord</h1>"

@app.route("/info")
def description():
    return "<h1> El bot posee muchas funciones, entre ellas traducir texto y generar códigos QR </h1>"
    
@app.route("/access")
def access():
    return "<h1>¡Accede al bot ya!</h1>" \
           "<a href='https://discord.com/oauth2/authorize?client_id=1207304722395168788&permissions=8&scope=bot'>Click aquí para acceder</a>"


app.run(debug=True)