import sqlite3
import os

class   ProgramBd:
    def __init__(self):
        self.conect = sqlite3.connect('lib/info.sql')
        self.createTableIfNotExists()

    def createTableIfNotExists(self):
        with self.conect:
            self.conect.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    senha TEXT,
                    nome TEXT,
                    idade INTEGER
                )
            ''')

    def clear(self):
        return os.system("cls")

    def save(self):
        self.conect.commit()

    def createUser(self):
        self.clear()
        print(f"+{'-' *30}+")
        print(f"|{'Adicione suas Informações':^{30}}|")
        print(f"+{'-' *30}+")
        login = input("Digite Seu Login: ")
        senha = input("Digite Sua Senha: ")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        
        with self.conect:
            self.conect.execute("INSERT INTO usuarios (login, senha, nome, idade) VALUES (?, ?, ?, ?)",
                                (login, senha, nome, idade))
            print(f"+{'-' *30}+")
            self.save()

    def userInfo(self):
        with self.conect:
            cursor = self.conect.execute("SELECT * FROM usuarios")
            return cursor.fetchall()

    def checkUser(self, username: str):
        with self.conect:
            cursor = self.conect.execute("SELECT * FROM usuarios WHERE login = ?", (username,))
            return cursor.fetchone()
