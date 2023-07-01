from controllers.controllers import *


routes = {
    #CLIENTE
    "index_route":"/","IndexController":IndexController.as_view("index"),
    "mensajes_contactos":"/sitio/contacto/mensaje","MensajesContactosController":MensajesContactosController.as_view("mensajes_contactos"),
    #ADMIN
    "index_admin":"/admin/","IndexAdminController":IndexAdminController.as_view("index_admin"),
    "ver_mensajes":"/admin/verMensajes","VerMensajesController":VerMensajesController.as_view("ver_mensajes"),
    "admin_login":"/admin/login","AdminController":AdminController.as_view("admin_login"),
}