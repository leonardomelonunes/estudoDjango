#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, make_response
from mod_login.login import validaSessao
from mod_cliente.ClienteBD import Clientes
from mod_produto.produtoDB import Produtos
from mod_pedido.pedidosDB import Pedidos
from mod_pedido.produtos_pedidoDB import ProdutosPedido
from base64 import b64encode
import pdfkit

bp_pedido = Blueprint('pedido', __name__, url_prefix='/pedido', template_folder='templates')
itensped = []

@bp_pedido.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaPedidos():
    ped= Pedidos()
    res= ped.getAll()
    print(res)

    return render_template("formListaPedidos.html", result=res, content_type='application/json')

@bp_pedido.route("/formPedido", methods=['GET','POST'])
@validaSessao
def formPedido():
     
    cliente = Clientes()
    clientes = cliente.selectClientesALL()


    if request.form:
        pedido=Pedidos( request.form['observacoes'], request.form['code'])
        
        retorno = pedido.insert()
        if retorno=='Pedido cadastrado com sucesso!':
            return redirect(url_for('pedido.formProdutosPed', id=pedido.id))
        
    return render_template("formPedido.html", clientes=clientes)

@bp_pedido.route("/formProdutosPed/<int:id>", methods=['GET','POST'])
def formProdutosPed(id):

    produto = Produtos()
    produtos = produto.selectProdALL()

    cliente = Clientes()
    clientes = cliente.selectClientesALL()

    itemped = ProdutosPedido()
    itenspedidos = itemped.getByOrderId(id)

    pedido = Pedidos()
    pedido.get(id)
    print(pedido)


    if 'addProdutoDB' in request.form:
        itenspedidos = ProdutosPedido(
            id,
            request.form['idprod'],
            request.form['quantidade'],
            request.form['valor'],
            request.form['observacoes']
        )
        itenspedidos.insert()
        return redirect(url_for("pedido.formProdutosPed", id= id))
        # itemped.produtos_id = request.form['idprod']
        # itemped.quantidade = request.form['quantidade']
        # itemped.observacao = request.form['observacoes']
        # itemped.valor = request.form['valor']
        # itemped.pedidos_id = id

        # itensped.append(itemped)

    # if 'excluiProdutoDB' in request.form:
    #     print('entrou')
    #     for ip in itensped:
    #         ip.insert()
    #     itensped.clear()
    #     return redirect(url_for("pedido.formProdutosPed", id= id))

    if 'salvarpedido' in request.form:
        for ip in itensped:
            print(ip.produtos_id)
            print(id)
            print(ip.observacao)
            print(ip.quantidade)
            print(ip.valor)
            

    return render_template("formEditaPedido.html", produtos=produtos, clientes=clientes, pedido=pedido, itensped=itenspedidos)


@bp_pedido.route("/UpPed/<int:id>", methods=['GET','POST'])
def UpPed(id):
    
    if request.form:
        pedido=Pedidos( request.form['observacoes'], request.form['code'])
        
        pedido.id=id
        retorno = pedido.update()
        
            
    return redirect(url_for('pedido.formProdutosPed', id=id))

@bp_pedido.route("/DeleteProdutoPed", methods=['GET','POST'])
def DeleteProdutoPed():

    if request.form:
        produtosped = ProdutosPedido()
        produtosped.pedidos_id= request.form['idPedido']
        produtosped.produtos_id= request.form['idProdutoP']
        produtosped.delete()

    return redirect(url_for('pedido.formProdutosPed', id= request.form['idPedido']))

@bp_pedido.route("/DeletePed/<int:id>", methods=['GET','POST'])
def DeletePed(id):

    
    pedidos = Pedidos()
    pedidos.delete(id)

    return redirect(url_for('pedido.formListaPedidos'))


@bp_pedido.route('/report/<int:id>')
def report(id):

    order = Pedidos()
    ret = order.get(id)
    if not order.id:
        flash(ret, 'info')
        return redirect(url_for('pedido.formListaPedidos'))

    order_p = ProdutosPedido()
    products = order_p.getByOrderId(order.id)
    images = []
    for product in products:
        images.append(product[7])

    ren = render_template('gerarPDF.html', products=products, images=images, order=order)
    pdf = pdfkit.from_string(ren, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachement; filename=relatorio-pedido.pdf'
    return response
    


    
   


   
