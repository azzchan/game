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

# @app.route('/', methods=['GET', 'POST'])
# def guardar_texto():
#     if request.method == 'POST':
#         texto_usuario = request.form.getlist('anime_input')
#     # datos = request.json
#     # texto = datos.get('texto', '')
    
#     # with open('texto_guardado.txt', 'a') as archivo:
#     #     archivo.write(texto + '\n')
    
#     return jsonify({'mensaje': 'Texto recibido correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
