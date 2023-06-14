from flask import Flask , render_template , url_for

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/contacto')
def nosotros():
    return render_template('sitio/contacto.html')

if __name__ == '__main__':
    app.run(debug=True)