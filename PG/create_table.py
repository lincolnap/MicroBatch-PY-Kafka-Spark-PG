import psycopg2
from psycopg2 import sql
import os

db_config = {
    "dbname": "streaming",  
    "user": "postgres",       
    "password": "postgres", 
    "host": "localhost",         
    "port": "5432"               
}


create_table_query = """
CREATE TABLE IF NOT EXISTS clients (
    id serial PRIMARY KEY,
    name VARCHAR(200),
    location VARCHAR(10000),
    phone VARCHAR
);
"""

# Conexión y ejecución de la sentencia
try:
    # Conectar a la base de datos
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Ejecutar la sentencia SQL
    cursor.execute(create_table_query)
    conn.commit()

    print("Tabla 'clients' creada exitosamente.")

except Exception as e:
    print(f"Error al crear la tabla: {e}")

finally:
    # Cerrar conexión
    if cursor:
        cursor.close()
    if conn:
        conn.close()
