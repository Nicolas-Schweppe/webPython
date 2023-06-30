from flask.views import MethodView
from flask import Flask , render_template ,request,redirect
from db import mysql
from datetime import date
from flaskext.mysql import MySQL




class IndexController(MethodView):

    def get(self):
        return render_template('sitio/index.html')


class AdminController(MethodView):

    def get(self):
        return render_template('admin/login.html')


class MensajesContactos(MethodView):

    def post(self):
        _nombre = request.form['nombre']
        _email = request.form['email']
        _telefono= request.form['telefono']
        _mensaje= request.form['mensaje']
        _hora_actual = date.today()
        print(_nombre,_email,_telefono,_mensaje,_hora_actual)
"""
        sql="INSERT INTO `mensajes`(`nombre`, `correo`, `telefono`, `mensaje`, `fecha`) VALUES (%s,%s,%s,%s,%s);"
        datos=(_nombre,_email,_telefono,_mensaje,_hora_actual)
        conexion=mysql.connect()
        cursor=conexion.cursor()
        cursor.execute(sql,datos)
        conexion.commit()
        #with mysql.cursor() as cur:
"""        
         #   cur.execute("INSERT INTO mensajes VALUES(%s,%s,%s,%s,%s)",(_nombre,_email,_telefono,_mensaje,_hora_actual))
          #  cur.connection.commit()
    #return redirect('/')