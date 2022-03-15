#coding: utf-8
from flask import Blueprint, render_template, request, url_for, redirect
from mod_login.login import validaSessao
from mod_produto.produtoDB import Produtos
import base64
from logs import Logs


bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaProdutos():
    prod= Produtos()
    res= prod.selectProdALL()

    return render_template("formListaProdutos.html", result=res, content_type='application/json')

@bp_produto.route("/formProduto", methods=['POST'])
@validaSessao
def formProduto():
    prod=Produtos()
    return render_template("formProduto.html", prod=prod)

@bp_produto.route("/cadProduto", methods=['POST'])
def insertProduto():
    
    prod=Produtos()

    
    
    prod.id_produto = request.form['id_produto']
    prod.descricao = request.form['descricao']
    prod.valor = request.form['valor']
    prod.imagem =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")
    


    logs = Logs()
    logs.logadorInfo("Novo Produto cadastrado.")

    return redirect('/produto')

@bp_produto.route('/formEditProduto', methods=['POST'])
def formEditProduto():

    prod=Produtos()
    
    
   #realiza a busca pelo produto e armazena o resultado no objeto
    executou = prod.selectProd( request.form['id_produtos'] )

    logs = Logs()
    logs.logadorInfo("Editou um Produto.")
    
    
    return render_template('formEditProdutos.html', prod=prod, content_type='application/json')

@bp_produto.route("/editProduto", methods=['POST'])
def editProduto():
    
    prod=Produtos()

    prod.id_produto = request.form['id_produto']  
    prod.descricao  = request.form['descricao']
    prod.valor = request.form['valor']
    prod.imagem =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")
    

    if 'editProdutoDB' in request.form:
        prod.updateProd()
    elif 'excluiProdutoDB' in request.form:
        prod.deleteProd()

        logs = Logs()
        logs.logadorInfo("Deletou um produto.")
    
    
    return redirect('/produto')

