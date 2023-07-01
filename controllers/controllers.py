from flask.views import MethodView
from flask import Flask , render_template ,request,redirect
from db import obtenerConexion
import datetime



class IndexController(MethodView):

    def get(self):
        return render_template('sitio/index.html')

class IndexAdminController(MethodView):

    def get(self):
        return render_template('admin/index.html')


class AdminController(MethodView):

    def get(self):
        return render_template('admin/login.html')


class MensajesContactosController(MethodView):

    def post(self):
        _nombre = request.form['nombre']
        _email = request.form['email']
        _telefono= request.form['telefono']
        _mensaje= request.form['mensaje']
        _hora_actual = datetime.datetime.now()
        hora_formateada = _hora_actual.strftime('%d-%m-%Y-%H:%M')

        sql="INSERT INTO `mensajes`(`nombre`, `correo`, `telefono`, `mensaje`, `fecha`) VALUES (%s,%s,%s,%s,%s);"
        datos=(_nombre,_email,_telefono,_mensaje,hora_formateada)
        conexion = obtenerConexion()
        cursor=conexion.cursor()
        cursor.execute(sql,datos)
        conexion.commit()
        return redirect('/')
class VerMensajesController(MethodView):

    def get(self):

        conexion = obtenerConexion()
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM `mensajes`;")
        mensajes =cursor.fetchall()
        conexion.commit()
        return render_template('admin/index.html',mensajes=mensajes)