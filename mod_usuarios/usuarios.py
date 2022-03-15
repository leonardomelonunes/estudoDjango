#coding: utf-8
from flask import Flask, render_template, request, redirect, Blueprint
from mod_usuarios.UsuariosBD import Usuarios
from mod_login.login import validaSessao
from BancoDB import Banco
import pymysql


usuarios_db = Blueprint('usuarios_db', __name__, url_prefix='/usuarios', template_folder='templates')


@usuarios_db.route('/')
@validaSessao
def listaUsuarios():
    
    user=Usuarios()
    
    res = user.selectUserALL()
    
    return render_template('formListaTeste.html', result=res, content_type='application/json')


@usuarios_db.route('/addUser', methods=['POST'])
@validaSessao
def addUser():
    
    user=Usuarios()
    
    #user.id_usuario = request.form['id_usuario']
    user.nome  = request.form['nome']
    user.login = request.form['login']
    user.senha = request.form['senha']
    user.grupo = request.form['grupo']

    executou = user.insertUser()
    print(executou)

    return redirect('/usuarios')


@usuarios_db.route('/formEditUsuario', methods=['POST'])
def formEditUser():

    user=Usuarios()
    
    #realiza a busca pelo usuario e armazena o resultado no objeto
    executou = user.selectUser( request.form['id_usuario'] )
    print(executou)
    
    return render_template('formTeste.html', user=user, content_type='application/json')


@usuarios_db.route('/editUser', methods=['POST'])
def editUser():
    
    user=Usuarios()
    
    user.id_usuario = request.form['id_usuario']
    user.nome  = request.form['nome']
    user.login = request.form['login']
    user.senha = request.form['senha']
    user.grupo = request.form['grupo']

    if 'salvaEditaClienteDB' in request.form:
        user.updateUser()
    elif 'excluiClienteDB' in request.form:
        user.deleteUser()

    return redirect('/usuarios')


if __name__ == "__main__":
    app.run()