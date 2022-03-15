from BancoDB import Banco

class Pedidos():

    def __init__(self, observacao='', clientes_id=None):
        self.id = None
        self.data_hora = None
        self.observacao = observacao
        self.clientes_id = clientes_id
        self.cliente_name = None


    def getAll(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT tb_pedidos.id_pedido, tb_pedidos.data_hora, tb_pedidos.observacao, tb_pedidos.id_cliente, tb_clientes.nome FROM tb_pedidos LEFT JOIN tb_clientes ON tb_pedidos.id_cliente = tb_clientes.id_cliente')
            result = c.fetchall()
            c.close()
            return result
        except:
            return None

    def getByUser(self, user_id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT tb_pedidos.id_pedido, tb_pedidos.data_hora, tb_pedidos.observacao, tb_pedidos.id_cliente, tb_clientes.nome FROM tb_pedidos LEFT JOIN tb_clientes ON tb_pedidos.id_cliente = id_cliente WHERE tb_pedidos.id_cliente = %s', (user_id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


    def get(self, id_pedido):
        banco=Banco()
        #try:
        c=banco.conexao.cursor()
        c.execute('SELECT tb_pedidos.id_pedido, tb_pedidos.data_hora, tb_pedidos.observacao, tb_pedidos.id_cliente, tb_clientes.nome FROM tb_pedidos LEFT JOIN tb_clientes ON tb_pedidos.id_cliente = tb_clientes.id_cliente WHERE tb_pedidos.id_pedido = %s' , (id_pedido))
        for linha in c:
            self.id=linha[0]
            self.data_hora=linha[1]
            self.observacao=linha[2]
            self.clientes_id=linha[3]
            self.cliente_name=linha[4]
        c.close()
        if not self.id:
            return 'Pedido não encontrado!'
        return 'Busca feita com sucesso!'
       # except:
            #return 'Ocorreu um erro na busca do pedido'


    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO tb_pedidos(observacao, id_cliente) VALUES (%s, %s)' , (self.observacao, self.clientes_id))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()
            return 'Pedido cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do pedido'


    def update(self):
        banco=Banco()
        #try:
        c=banco.conexao.cursor()
        c.execute('UPDATE tb_pedidos SET observacao = %s , id_cliente = %s WHERE id_pedido = %s' , (self.observacao , self.clientes_id, self.id))
        banco.conexao.commit()
        c.close()
        return 'Pedido atualizado com sucesso!'
        #except:
            #return 'Ocorreu um erro na alteração do pedido'


    def delete(self, id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("delete from tb_pedido_produtos where id_pedido = %s" , (id))            
            c.execute('DELETE FROM tb_pedidos WHERE id_pedido = %s' , (id))            
            banco.conexao.commit()
            c.close()
            return 'Pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do pedido'


    def hasByUser(self, user_id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT COUNT(id) FROM tb_pedidos WHERE tb_pedidos.id_cliente = %s', (user_id))
            result = c.fetchall()
            c.close()
            if result[0][0] > 0:
                return True
            return False
        except:
            return False