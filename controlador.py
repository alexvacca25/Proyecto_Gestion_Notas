from dataclasses import replace
from datetime import datetime
import sqlite3

from flask import flash
import envioemail

DB_NAME='bdgestion.s3db'

def conectar_db():
    conn=sqlite3.connect(DB_NAME)
    return conn

def insertar_usuarios(nombre,apellido,usuario,passwd):
    cod_ver=str(datetime.now())
    cod_ver=cod_ver.replace("-","")
    cod_ver=cod_ver.replace(" ","")
    cod_ver=cod_ver.replace(":","")
    cod_ver=cod_ver.replace(".","")
    
    #flash(cod_ver)   
    try:
        db=conectar_db()
        cursor=db.cursor()
        sql="INSERT INTO usuarios(nombre,apellido,usuario,passw,cod_verificacion,verificado,id_rol) VALUES(?,?,?,?,?,?,?)"
        cursor.execute(sql,[nombre,apellido,usuario,passwd,cod_ver,False,1])
        db.commit()
        envioemail.enviar_email(usuario,cod_ver)
        return True
    except:
        return False