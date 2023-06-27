from flask.views import MethodView
from flask import Flask , render_template ,request , redirect

class IndexController(MethodView):

    def get(self):
        return render_template('sitio/index.html')
        

class AdminController(MethodView):
    
    def get(self):
        return render_template('admin/login.html')
