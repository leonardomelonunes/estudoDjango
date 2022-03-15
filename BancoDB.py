import pymysql

class Banco():

    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "db_abc_bolinhas"
        self.conexao = pymysql.connect(host, user, password, db)
        
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS tb_usuarios (
                    id_usuario INT NOT NULL primary key AUTO_INCREMENT,
                    nome VARCHAR(255) NOT NULL,
                    login VARCHAR(45) NOT NULL,
                    senha VARCHAR(255) NOT NULL,
                    grupo CHAR(5) NOT NULL DEFAULT 'admin')""")
        self.conexao.commit()
        c.close()