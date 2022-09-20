from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/usuarios')
def menu_user():
    return render_template('usuarios.html')

@app.route('/materias')
def menu_materias():
    return render_template('materias.html')


@app.route('/cursos')
def menu_cursos():
    return render_template('cursos.html')


@app.route('/matriculas')
def menu_matriculas():
    return render_template('matriculas.html')



@app.route('/actividades')
def menu_actividades():
    return render_template('actividades.html')



@app.route('/calificaciones')
def menu_calificaciones():
    return render_template('calificaciones.html')

if  __name__=='__main__':
     app.run(debug=True)  