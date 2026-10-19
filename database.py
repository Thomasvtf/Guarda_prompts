import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "prompts_bd"
    )

    if conexion.is_connected():
        print("Conexion exitosa")
    else:
        print("Conexion fallida")

    return conexion

conectar()