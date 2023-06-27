from controllers.controllers import IndexController ,AdminController

routes = {
    "index_route":"/","IndexController":IndexController.as_view("index"),
    "admin_login":"/admin/login","AdminController":AdminController.as_view("admin_login"),
}