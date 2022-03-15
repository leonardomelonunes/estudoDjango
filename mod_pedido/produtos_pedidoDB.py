from BancoDB import Banco

class ProdutosPedido():

    def __init__(self, pedidos_id=None, produtos_id=None, quantidade=None, valor=None, observacao=''):
        self.id = None
        self.pedidos_id = pedidos_id
        self.produtos_id = produtos_id
        self.quantidade = quantidade
        self.valor = valor
        self.observacao = observacao


    def getByOrderId(self, id_pedido):
        banco=Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT tb_pedido_produtos.id_pedido, tb_pedido_produtos.id_produto, tb_pedido_produtos.quantidade, tb_pedido_produtos.valor, tb_pedido_produtos.observacao, tb_produtos.descricao, tb_produtos.valor, CONVERT(tb_produtos.imagem USING utf8) FROM tb_pedido_produtos LEFT JOIN tb_produtos ON tb_pedido_produtos.id_produto = tb_produtos.id_produto WHERE tb_pedido_produtos.id_pedido = %s' , (id_pedido))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None

    
    def getByOrderIdAndProductId(self, id_pedido, id_produto):
        banco=Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT id_pedido, id_produto, quantidade, valor, observacao FROM tb_pedido_produtos WHERE id_pedido = %s AND id_produto = %s' , (id_pedido, id_produto))
            for linha in c:
                self.pedidos_id=linha[0]
                self.produtos_id=linha[1]
                self.quantidade=linha[2]
                self.valor=linha[3]
                self.observacao=linha[4]
                return True
            c.close()
            return False
        except:
            return False


    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO tb_pedido_produtos(id_pedido, id_produto, quantidade, observacao, valor) VALUES (%s, %s, %s, %s, %s)' , (self.pedidos_id, self.produtos_id, self.quantidade, self.observacao, self.valor))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()
            return 'Produto do pedido cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do produto do pedido'


    def update(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE tb_pedido_produtos SET  quantidade = %s, valor = %s, observacao = %s WHERE id_pedido = %s AND id_produto = %s' , (self.quantidade, self.valor, self.observacao, self.pedidos_id, self.produtos_id))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do produto do pedido'


    def delete(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM tb_pedido_produtos WHERE id_pedido = %s AND id_produto = %s' , (self.pedidos_id, self.produtos_id))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do produto do pedido'

    
    def deleteByPedido(self, order_id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM tb_pedido_produtos WHERE id_pedido = %s' , (order_id))
            banco.conexao.commit()
            c.close()
            return True
        except:
            return False


    def hasByProduct(self, product_id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT COUNT(id_pedido) FROM tb_pedido_produtos WHERE tb_pedido_produtos.id_produto = %s', (product_id))
            result = c.fetchall()
            c.close()
            if result[0][0] > 0:
                return True
            return False
        except:
            return False