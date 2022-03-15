from BancoDB import Banco

class Usuarios(object):

    def __init__(self, id_usuario=0, nome="", login="", senha="", grupo=""):
        self.info = {}
        self.id_usuario = id_usuario
        self.nome = nome
        self.login = login
        self.senha = senha
        self.grupo = grupo


    def selectUserALL(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id_usuario, nome, login, senha, grupo from tb_usuarios")
            result = c.fetchall()
            c.close()
            return result
        except:
            return "Ocorreu um erro na busca do usuário"


    def selectUser(self, id_usuario):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("select id_usuario, nome, login, senha, grupo from tb_usuarios where id_usuario = %s" , (id_usuario))
            
            for linha in c:
                self.id_usuario=linha[0]
                self.nome=linha[1]
                self.login=linha[2]
                self.senha=linha[3]
                self.grupo=linha[4]
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


    def insertUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tb_usuarios(nome, login, senha, grupo) values (%s, %s, %s, %s)" , (self.nome, self.login, self.senha, self.grupo ))
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"


    def updateUser(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("update tb_usuarios set nome = %s , login  = %s , senha = %s, grupo = %s where id_usuario = %s" , (self.nome , self.login , self.senha, self.grupo, self.id_usuario))
            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"


    def deleteUser(self):

        banco=Banco()
        try:

            c=banco.conexao.cursor()
            c.execute("delete from tb_usuarios where id_usuario = %s" , (self.id_usuario))
            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"


    def validaUsuario(self, login, senha ):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT id_usuario, login, senha, grupo, nome  FROM tb_usuarios where login = %s and senha = %s", (login , senha))
            result = c.fetchall()
            c.close()
            return result 
        except:
            return "Ocorreu um erro na busca do usuário"      