from BancoDB import Banco

class Clientes(object):

    def __init__ (self, id_cliente=0, nome="", telefone="", cep="", endereco="", numero="", bairro="", cidade="", estado="", observacao="", email=""):
        self.info = {}
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.observacao = observacao
        self.email = email

    def selectClientesALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id_cliente, nome, telefone, cep, endereco, numero, bairro, cidade, estado, observacao, email from tb_clientes")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca dos clientes"

    def selectCliente(self, id_cliente):
            banco=Banco()
            try:
                c=banco.conexao.cursor()
                c.execute("select id_cliente, nome, telefone, cep, endereco, numero, bairro, cidade, estado, observacao, email from tb_clientes where id_cliente = %s" , (id_cliente))

                for linha in c:
                    self.id_cliente=linha[0]
                    self.nome=linha[1]
                    self.telefone=linha[2]
                    self.cep=linha[3]
                    self.endereco=linha[4]
                    self.numero=linha[5]
                    self.bairro=linha[6]
                    self.cidade=linha[7]
                    self.estado=linha[8]
                    self.observacao=linha[9]
                    self.email=linha[10]
                c.close()

                return "Busca feita com sucesso!"
            except:
                return "Ocorreu um erro na busca do Cliente"

    def insertCliente(self):
                banco = Banco()
                try:
                    c = banco.conexao.cursor()
                    c.execute("insert into tb_clientes(nome, telefone, cep, endereco, numero, bairro, cidade, estado, observacao, email) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" , (self.nome, self.telefone, self.cep, self.endereco, self.numero, self.bairro, self.cidade, self.estado, self.observacao, self.email ))
                    banco.conexao.commit()
                    c.close()

                    return "Cliente Cadastrado com sucesso!"
                except:
                    return "Ocorreu um erro na inserção do Cliente" 

                
    def updateCliente(self):

                banco=Banco()
                try:

                    c=banco.conexao.cursor()
                    c.execute("update tb_clientes set nome = %s , telefone = %s , cep = %s , endereco = %s , numero = %s , bairro = %s , cidade = %s , estado = %s , observacao = %s , email = %s where id_cliente = %s" , (self.nome, self.telefone, self.cep, self.endereco, self.numero, self.bairro, self.cidade, self.estado, self.observacao, self.email, self.id_cliente))
                    banco.conexao.commit()
                    c.close()

                    return "Cliente atualizado com sucesso"
                except:
                    return "Ocorreu um erro na alteração do Cliente"

                
    def deleteCliente(self):

                banco=Banco()
                try:

                    c=banco.conexao.cursor()
                    c.execute("delete from tb_clientes where id_cliente = %s" , (self.id_cliente))
                    banco.conexao.commit()
                    c.close()

                    return "Cliente excluido com sucesso!"
                except:
                    return "Ocorreu um erro na exclusão do cliente"