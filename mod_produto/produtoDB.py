from BancoDB import Banco

class Produtos(object):

    def __init__(self, id_produto=0, descricao="", valor=0, imagem=""):
        self.info = {}
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor = valor
        self.imagem = imagem
       


    def selectProdALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id_produto, descricao, valor, CONVERT(imagem USING utf8) from tb_produtos")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do produto"


    def selectProd(self, id_produto):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id_produto, descricao, valor, CONVERT(imagem USING utf8) from tb_produtos where id_produto = %s" , (id_produto))
            
            for linha in c:
                
                self.id_produto = linha[0]
                self.descricao = linha[1]
                self.valor = linha[2]
                self.imagem = linha[3]
                
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca de um produto"


    def insertProd(self):

        banco = Banco()
        try:
            print(self.imagem)
            c = banco.conexao.cursor()
            c.execute("insert into tb_produtos(descricao, valor, imagem) values (%s, %s, %s)" ,
             (self.descricao, self.valor, self.imagem))
            banco.conexao.commit()
            c.close()

            return "Produto cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do produto"


    def updateProd(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update tb_produtos set descricao = %s, valor = %s, imagem = %s where id_produto = %s" , 
            (self.descricao, self.valor, self.imagem, self.id_produto))
            banco.conexao.commit()
            c.close()

            return "Produto atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Produto"


    def deleteProd(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("delete from tb_produtos where id_produto = %s" , (self.id_produto))
            banco.conexao.commit()
            c.close()

            return "Produto excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do Produto"