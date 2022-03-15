#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from mod_login.login import validaSessao
from mod_cliente.ClienteBD import Clientes
from BancoDB import Banco
import pymysql

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder='templates')

@bp_cliente.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaClientes():

    cliente=Clientes()

    res = cliente.selectClientesALL()
    
    return render_template("formListaClientes.html" , result=res, content_type='application/json')

@bp_cliente.route("/addCliente", methods=['POST'])
@validaSessao
def addCliente():

    cliente=Clientes()

    cliente.nome = request.form['nome']
    cliente.telefone = request.form['telefone']
    cliente.cep = request.form['cep']
    cliente.endereco = request.form['endereco']
    cliente.numero = request.form['numero']
    cliente.bairro = request.form['bairro']
    cliente.cidade = request.form['cidade']
    cliente.estado = request.form['estado']
    cliente.observacao = request.form['observacao']
    cliente.email = request.form['email']

    executou = cliente.insertCliente()
    print(executou)

    return redirect('/cliente')

  
@bp_cliente.route("/formCliente", methods=['POST'])
@validaSessao
def formCliente():
    return render_template('formCliente.html')


@bp_cliente.route('/formEditCliente' , methods=['POST'])
def formEditCliente():

    cliente=Clientes()

    executou = cliente.selectCliente( request.form['id_cliente'] )
    print(executou)

    return render_template('formEditaCliente.html', cliente=cliente, content_type='application/json')


@bp_cliente.route('/editCliente', methods=['POST'])
def editCliente():

    cliente=Clientes()

    cliente.id_cliente = request.form['idCliente']
    cliente.nome = request.form['nome']
    cliente.telefone = request.form['telefone']
    cliente.cep = request.form['cep']
    cliente.endereco = request.form['endereco']
    cliente.numero = request.form['numero']
    cliente.bairro = request.form['bairro']
    cliente.cidade = request.form['cidade']
    cliente.estado = request.form['estado']
    cliente.observacao = request.form['observacao']
    cliente.email = request.form['email']

    if 'editClienteDB' in request.form:
        cliente.updateCliente()
    elif 'excluiClienteDB' in request.form:
        cliente.deleteCliente()

    return redirect('/cliente')
        

