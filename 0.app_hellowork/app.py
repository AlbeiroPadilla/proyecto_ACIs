""" Ejercicio1: Crea una aplicación web básica con Flask que,
    al ser ejecutada. inicia un servidor local en el puerto 5000.
    Cuando visita la ruta principal (ttp://localhost:5000/),
    el servidor responderá con un mensaje HTML que dice "Hello, World Flask"
"""

#Se importa el módulo Flask desde el paquete flask
from flask import Flask
#Crea una instancia de la clase Flask
#El argumento __name__ le dice a Flask
#que utilice el nombre del archivo actual main.py
app = Flask(__name__)

#Este es un decorador que definr una ruta
#corresponde a la pagina principal del app
@app.route("/")
#Cuando alguien visite app (por ejemplo, http://localhost:5000/),
#la funcion hello() sera ejecutada.
def hello():
    return "<h1>Hello, World Flask !</h1>"

#Solo se ejecute si el archivo es ejecutado directamente
#arranca la aplicacion flask en modo de depuracion (debug=True)
if __name__ =='__main__':
    app.run(debug=True, port=5000)