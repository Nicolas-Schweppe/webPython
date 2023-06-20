from flask import Flask , render_template ,request , redirect
from flaskext.mysql import MySQL
from datetime import date


app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='portafolio'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

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
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)