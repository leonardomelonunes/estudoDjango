#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
from mod_usuarios.UsuariosBD import Usuarios

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')


@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")


@bp_login.route("/login", methods=['POST'])
def validaLogin():
    _name = request.form.get('usuario')
    _pass = request.form.get('senha')

    ValidaUserBanco = Usuarios()
    userBanco = ValidaUserBanco.validaUsuario( _name , _pass )

    userNameDB=0
    passwordDB=0
    grupoDB=0
     
    for row in userBanco:
          id = row[0]
          userNameDB=row[1]
          passwordDB=row[2]
          grupoDB=row[3]
          nomeDB=row[4]

       # verifica se foi informado usuario e senha
    if _name and _pass and request.method == 'POST' and _name == userNameDB and _pass == passwordDB:
        #limpa a sessão
        session.clear()
        #registra usuario na sessão, armazenando o login do usuário
        session['usuario'] = _name
        session['grupo'] = grupoDB
        session['nome'] = nomeDB
        #abre a aplicação na tela home
        return redirect(url_for('home.home'))
    else:
        #retorna para a tela de login
        return redirect(url_for('login.login',falhaLogin=1))


@bp_login.route("/logoff", methods=['GET'])
def validaLogoff():
    #remove um item individual da sessão
    session.pop('usuario',None)
    #limpa a sessão
    session.clear()

    #retorna para a tela de login
    return redirect(url_for('login.login'))
    

# valida se o usuário esta ativo na sessão 
# from functools import wraps
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login',falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)
    #retorna o resultado do if acima
    return decorated_function
