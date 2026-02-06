import sqlite3

def inicializar_db():
    conn = sqlite3.connect("money_master.db")
    cursor = conn.cursor()
    # Creamos la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            ingreso REAL,
            gasto REAL,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_movimiento(fecha, ingreso, gasto, categoria="General"):
    conn = sqlite3.connect("money_master.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movimientos (fecha, ingreso, gasto, categoria) VALUES (?, ?, ?, ?)",
                   (fecha, ingreso, gasto, categoria))
    conn.commit()
    conn.close()

def obtener_movimientos():
    conn = sqlite3.connect("money_master.db")
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, ingreso, gasto FROM movimientos ORDER BY fecha DESC LIMIT 12")
    datos = cursor.fetchall()
    conn.close()
    # Lo devolvemos como lista de diccionarios para que sea fácil de usar
    return [{"fecha": d[0], "ingreso": d[1], "gasto": d[2]} for d in datos]