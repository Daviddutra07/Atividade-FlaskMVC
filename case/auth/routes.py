from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from models.user import User
from database import obter_sessao

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='views/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)


        user = User(email=email, password=senha_hash)
        sucesso = user.save()

        if sucesso:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("E-mail já cadastrado.", "error")
            return redirect(url_for('register'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        session = obter_sessao()
        user = session.query(User).filter_by(email=email).first()
        session.close()

        if user and check_password_hash(user.password, senha):
            login_user(user)
            return redirect(url_for('cardapio'))
        else:
            flash("Usuário ou senha incorretos. Tente novamente.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@auth_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))