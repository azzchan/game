from flask import render_template, request
from app import app
from app.game.menu import Menu

@app.route('/', methods=['GET', 'POST'])
def index():
    menu = Menu.mostrar_menu()
    if request.method == 'POST':
        input_user = request.form['texto']
        print(input_user)
    return render_template('index.html', menu=menu, input_user=input_user)


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
