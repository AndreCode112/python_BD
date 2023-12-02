import sqlite3

# Conectar ou criar o banco de dados
conn = sqlite3.connect('exemplo.sql')
print(f"{'opções':^20}")
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela (opcional)
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    idade INTEGER
                )''')

# Inserir dados na tabela
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('João', 30))
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ('Maria', 25))

# Salvar (commit) as mudanças no banco de dados
conn.commit()

# Consulta para obter informações sobre as colunas da tabela 'usuarios'
cursor.execute("PRAGMA table_info(usuarios)")
colunas = cursor.fetchall()

# Exibir informações sobre as colunas
print("Colunas da tabela 'usuarios':")
for coluna in colunas:
    print(f"Nome: {coluna[1]}, Tipo: {coluna[2]}")

print("\nValores na tabela 'usuarios':")
# Consulta para recuperar os valores da tabela 'usuarios'
cursor.execute("SELECT * FROM usuarios")
valores = cursor.fetchall()


def verificar_usuario(username):
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (username,))
    resultado = cursor.fetchone()
    return resultado  # Retorna a linha correspondente ao usuário ou None se não encontrado

def realizar_login():
    username = input("Digite seu nome de usuário: ")
    usuario = verificar_usuario(username)

    if usuario:
        senha = input("Digite sua senha: ")
        if senha == usuario[2]:  # Supondo que a senha esteja na terceira coluna (índice 2)
            print("Login bem-sucedido!")
            # Aqui você pode adicionar o código para continuar com a sessão do usuário
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")

realizar_login()

# Exibir os valores na tabela
for valor in valores:
    print(valor)

# Fechar a conexão com o banco de dados
conn.close()
