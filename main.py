from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    edad= 18
    #return '<h1>Bienvenido a Flask</>'
    return render_template('index.html', edad=edad)

@app.route('/proyectos/')
@app.route('/proyectos/<string:nombre>/<int:edad>')
def proyectos(nombre = None, edad = None):
    if (nombre == None):
        return render_template('proyectos.html')
    else:
        return render_template('proyectos.html', nombre=nombre, edad=edad)
    
@app.route('/loops/')
def loops():
    lista= ['Python', 'Java', 'C++', 'PHP']
    return render_template('loops.html', lista=lista)

@app.route('/mapa/<string:lat>/<string:long>/<string:pop>/<string:zoom>/<string:sizeMap>/<string:sizeMap2>')
def mapa(lat, long, pop, zoom, sizeMap, sizeMap2):
    return render_template('mapa.html', lat=lat, long=long, pop = pop, zoom = zoom, sizeMap = sizeMap, sizeMap2 = sizeMap2)