from flask import Flask
from config import configuracion
from routes.routes import routes


app=Flask(__name__)


#Routes
app.add_url_rule(routes["index_route"],view_func=routes["IndexController"])
app.add_url_rule(routes["admin_login"],view_func=routes["AdminController"])
app.add_url_rule(routes["mensajes_contactos"],view_func=routes["MensajesContactos"])


if __name__ == '__main__':
    app.run(debug=True)
#if __name__== '__main__':
    app.config.from_object(configuracion['development'])
    app.run()