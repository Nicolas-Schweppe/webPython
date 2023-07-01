from flask import Flask , render_template ,request , redirect
from datetime import date
from flaskext.mysql import MySQL
from config import configuracion
from routes.routes import routes


app=Flask(__name__)
#Routes
#USER
app.add_url_rule(routes["index_route"],view_func=routes["IndexController"])
app.add_url_rule(routes["mensajes_contactos"],view_func=routes["MensajesContactosController"])
#ADMIN
app.add_url_rule(routes["admin_login"],view_func=routes["AdminController"])
app.add_url_rule(routes["index_admin"],view_func=routes["IndexAdminController"])
app.add_url_rule(routes["ver_mensajes"],view_func=routes["VerMensajesController"])

if __name__ == '__main__':
    app.run(debug=True)
#if __name__== '__main__':
    app.config.from_object(configuracion['development'])
    app.run()