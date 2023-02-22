from flask import Flask, render_template, redirect, url_for, request, session, flash
from database import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])

def login(): 
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        table = db.usuarios.find_one({'usuario': usuario, 'password': password})
        if table:
            session['table'] = table['password']
            return redirect(url_for('perfil'))
        flash('usuario o clave incorrecto')

    return render_template('login.html')

@app.route('/perfil')
def perfil():
    if 'table' not in session:
        return redirect(url_for('login'))
    return render_template('perfil.html')
