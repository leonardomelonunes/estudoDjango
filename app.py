#coding: utf-8
import os
from flask import Flask, session
from datetime import timedelta

from mod_login.login import bp_login
from mod_home.home import bp_home
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_pedido.pedido import bp_pedido
from mod_erro.erro import bp_erro
from mod_usuarios.usuarios import usuarios_db

app = Flask(__name__)

# gerando uma chave randomica para secret_key
app.secret_key = os.urandom(12).hex()

#before_first_request

# metodo para renovar o tempo da sessão
@app.before_request
def before_request():
    session.permanent = True
    #o padrão é 31 dias...
    app.permanent_session_lifetime = timedelta(minutes=60)

app.register_blueprint(bp_login)
app.register_blueprint(bp_home)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_pedido)
app.register_blueprint(bp_erro)
app.register_blueprint(usuarios_db)

if __name__ == "__main__":
    app.run()
