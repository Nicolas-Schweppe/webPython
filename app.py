from flask import Flask , render_template ,request , redirect
from datetime import date
from flaskext.mysql import MySQL
from config import configuracion
from decouple import config
from routes.routes import routes


app=Flask(__name__)


"""
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']=config('MYSQL_HOST')
app.config['MYSQL_DATABASE_USER']=config('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD']=config('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB']=config('MYSQL_DB')
mysql.init_app(app)
"""
#Routes
app.add_url_rule(routes["index_route"],view_func=routes["IndexController"])
app.add_url_rule(routes["admin_login"],view_func=routes["AdminController"])
app.add_url_rule(routes["mensajes_contactos"],view_func=routes["MensajesContactos"])

"""
@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/admin/login')
def login():
    return render_template('admin/login.html')

@app.route('/admin/mensajes')
def mensajes():
    conexion=mysql.connect()
    cursor= conexion.cursor()
    cursor.execute("SELECT * FROM `mensajes`")
    mensajes=cursor.fetchall()
    conexion.commit()
    print(mensajes)
    return render_template('admin/index.html', mensajes=mensajes)

@app.route('/sitio/contacto/mensaje',methods=['POST'])
def mensajeContacto():
    _nombre = request.form['nombre']
    _email = request.form['email']
    _telefono= request.form['telefono']
    _mensaje= request.form['mensaje']

    hora_actual = date.today()
    print(hora_actual)
    sql="INSERT INTO `mensajes`(`nombre`, `correo`, `telefono`, `mensaje`, `fecha`) VALUES (%s,%s,%s,%s,%s);"
    datos=(_nombre,_email,_telefono,_mensaje,hora_actual)
    if _email:
        conexion=mysql.connect()
        cursor=conexion.cursor()
        cursor.execute(sql,datos)
        conexion.commit()
    return redirect('/')
"""

if __name__ == '__main__':
    app.run(debug=True)
#if __name__== '__main__':
    app.config.from_object(configuracion['development'])
    app.run()