import sqlite3

DB_NAME='bdgestion.s3db'

def conectar_db():
    conn=sqlite3.connect(DB_NAME)
    return conn

def insertar_usuarios(nombre,apellido,usuario,passwd):

   
    return False