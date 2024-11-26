import sqlite3

# Função para conectar ao banco de dados e criar tabela se ela não existir
def conectar():
    # Conectar ao banco de dados
    conexao = sqlite3.connect('produto.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    curso.execute('''
                            CREATE TABLE IF NOT EXISTS produto(
                             id INTEGER PRIMARY KEY,   
                             nome TEXT NOT NULL,
                             quantidade INTEGER,
                             preco REAL
                           )
                          ''')
# Confirma as mudanças no banco de dados
    conexao.commit()
    conexao.close()

# Função para inserir um novo produto no banco de dados
def inserir_produto(nome, quantidade, preco):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('produto.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    # Inserindo uma nova linha na tabela 'produto' com os valores fornecidas para nome, quantidade, preco
    curso.execute('INSERT INTO produto(nome, quantidade, preco) VALUES (?, ?, ?)', (nome, quantidade, preco))

    # Confirma as mudanças no banco de Dados
    conexao.commit()
    # Fecha a Conexão com o banco de Dados.
    conexao.close()

# Função para atualizar as informações do produto no banco de dados
def atualizar_produto(id_produto, nome, quantidade, preco):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('produto.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    curso.execute('UPDATE produto SET nome = ?, quantidade = ?, preco = ? WHERE id = ?' , (nome, quantidade, preco, id_produto))
    # confirma as mudanças no banco de dados
    conexao.commit()
# Fecha a Conexão com o banco de dados
    conexao.close()

# Função para deletar um produto do banco de dados

def deletar_produto(id_produto):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('produto.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    curso.execute('DELETE FROM produto WHERE id = ?' , (id_produto,))
    # confirma as mudanças no banco de dados
    conexao.commit()
    # fecha a conexão com o banco de dados
    conexao.close()

# Função para pesquisar produto no banco de dados pelo nome

def pesquisar_produto(nome):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('produto.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    curso.execute('SELECT * FROM produto WHERE nome = ?' , (nome,))
    linhas = curso.fetchall()
    # fecha a conexão com o banco de dados
    conexao.close()
    return linhas

    # Função para listar todos os produto no banco de dados 

def lista_os_produtos():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('produto.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()

    # Selecione todas as linhas da tabela "produto"
    curso.execute('SELECT * FROM produto')
    #busca todas as linhas e armazena na variavel linhas
    linhas = curso.fetchall()
    #fecha a conexão com o banco de dados
    conexao.close()
    # Retorna a lista de todos os produtos
    return linhas

