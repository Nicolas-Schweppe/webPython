from controllers.controllers import IndexController ,AdminController,MensajesContactos

routes = {
    "index_route":"/","IndexController":IndexController.as_view("index"),
    "admin_login":"/admin/login","AdminController":AdminController.as_view("admin_login"),
    "mensajes_contactos":"/sitio/contacto/mensaje","MensajesContactos":MensajesContactos.as_view("mensajes_contactos"),
}