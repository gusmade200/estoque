from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('estoque.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn

# Página principal (lista os produtos)
@app.route('/')
def index():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

# Página para adicionar um produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        categoria = request.form['categoria']

        conn = get_db_connection()
        conn.execute('INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)', 
                     (nome, preco, categoria))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('adicionar.html')

# Remover um produto
@app.route('/remover/<int:id>', methods=['GET'])
def remover(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
