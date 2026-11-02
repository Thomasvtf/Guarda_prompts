import os

from flask import Flask, render_template, request, redirect, url_for

from database import conectar

app = Flask(__name__)

@app.route('/')
def inicio():

    conexion = conectar()
    
    cursor = conexion.cursor()

    cursor.execute("SELECT prompt FROM card")

    prompts = cursor.fetchall()

    conexion.close()

    return render_template ('index.html', prompts = prompts) 

@app.route('/guardar_prompt', methods = ['POST'])
def guardar_prompt():
    prompt = request.form.get('prompt')

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute ("INSERT INTO card (prompt) VALUES (?)", (prompt,))

    conexion.commit()
    cursor.close()
    conexion.close()

    return redirect(url_for('inicio'))

if __name__ == '__main__':
# Lee el puerto asignado por Render o usa el 5000 por defecto localmente
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)