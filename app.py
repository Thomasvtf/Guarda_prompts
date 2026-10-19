from flask import Flask, render_template, request

from database import conectar

app = Flask(__name__)

@app.route('/')
def inicio():

    prompt = conectar()

    return render_template ('index.html', prompt = prompt) 

@app.route('/guardar_prompt', methods = ['POST'])
def guardar_prompt():
    prompt = request.form.get('prompt')

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute ("INSERT INTO card (prompt) VALUES (%s)", (prompt,))

    conexion.commit()
    cursor.close()
    conexion.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)