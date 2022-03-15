from flask import Blueprint, render_template, redirect, url_for, request, session
from pathlib import Path
from datetime import datetime


class Logs(object):

    def __init__(self, tipo="", message=""):
        self.info = {}
        self.tipo = tipo
        self.message = message

        self.fileName = r"c:\users\userscc\desktop\log.txt"

    def CriaArqCasoNaoExista(self):

        file = Path(self.fileName)
        isFile = file.is_file()

        if isFile == True:
            return
        else:
            arquivo = open(self.fileName, 'w')
            arquivo.close()

    def logadorErro(self, message):

        self.message = message

        self.CriaArqCasoNaoExista()

        now = datetime.now()
        now = now.strftime("%d/%m/%Y (%H:%M:%S.%f)")
        user = " Sem Usuário Logado"
        if 'usuario' in session:
            user = session['usuario']


        arq = open(self.fileName, "r")
        conteudo = arq.readlines()

        conteudo.append("\n" + now + " - [ERRO] - " + self.message + " - Usuario: " + user)

        arq = open(self.fileName, "w")

        arq.writelines(conteudo)
        arq.close()

    def logadorInfo(self, message):

        self.message = message

        self.CriaArqCasoNaoExista()

        now = datetime.now()
        now = now.strftime("%d/%m/%Y (%H:%M:%S.%f)")
        user = " Sem Usuário Logado"
        if 'usuario' in session:
            user = session['usuario']
            grupo = session['grupo']
            nome = session['nome']

        arq = open(self.fileName, "r")
        conteudo = arq.readlines()
        conteudo.append("\n" + now + " - [INFO] - " + self.message + " - Usuario: " + user + " - Grupo: " + grupo + " - Nome: " + nome)

        arq = open(self.fileName, "w")

        arq.writelines(conteudo)
        arq.close()