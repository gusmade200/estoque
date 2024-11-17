import sqlite3

# Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criar a tabela de produtos, caso ela não exista
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
)
''')

# Inserir alguns dados de exemplo
cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES ('Produto A', 10.0, 'Categoria 1')")
cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES ('Produto B', 20.0, 'Categoria 2')")
cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES ('Produto C', 30.0, 'Categoria 1')")

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Tabela 'produtos' criada e dados inseridos com sucesso!")
