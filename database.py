import sqlite3

def conectar():
    conexion = sqlite3.connect("prompts_db.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL
        )
    """)
    conexion.commit()
    
    return conexion

# Prueba de conexión al ejecutar este archivo
if __name__ == '__main__':
    try:
        con = conectar()
        print("Conexión exitosa a SQLite y tabla 'card' verificada.")
        con.close()
    except Exception as e:
        print(f"Error en la base de datos: {e}")