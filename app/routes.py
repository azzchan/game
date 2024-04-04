from flask import render_template, request, jsonify
from app import app
from app.game.menu import Menu
from app.game.test import mensaje as mensaje_respuesta

@app.route('/', methods=['GET', 'POST'])
def index():
    menu = Menu.mostrar_menu()
    respuesta = None
    if request.method == 'POST':
        texto = request.form.get('texto')
        mensaje = mensaje_respuesta(texto)

    return render_template('index.html')

@app.route('/mensaje', methods=['POST'])
def obtener_mensaje():
    texto = request.form.get('texto')
    mensaje = mensaje_respuesta(texto)
    return jsonify({"mensaje": mensaje})

if __name__ == '__main__':
    app.run(debug=True)
