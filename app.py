import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from graficos import create_bar_chart, create_memory_chart  # Corrigido para importar ambas as funções

# Carregar as variáveis do .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Por favor, preencha todos os campos.')
            return render_template('login.html')
        
        # Aqui você pode adicionar lógica de autenticação sem Firebase
        flash('Email ou senha incorretos.')
    
    return render_template('login.html')

# Rota de cadastro
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        
        # Aqui você pode adicionar lógica de cadastro sem Firebase
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Rota do painel de controle
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Aqui você pode adicionar lógica para o painel de controle sem Firebase
    return redirect(url_for('login'))

# Rota de logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Rota do gráfico 1 (Desempenho de Processadores)
@app.route('/index7')
def grafico1():
    graph_html = create_bar_chart()  # Gera o gráfico de barras do desempenho do processador
    return render_template('index7.html', graph_html=graph_html)

# Rota do gráfico 2 (Velocidade de Memória)
@app.route('/index6')
def grafico2():
    graph_html = create_memory_chart()  # Gera o gráfico de velocidade de memória
    return render_template('index6.html', graph_html=graph_html)

# Outras rotas para páginas adicionais
@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

@app.route('/index4')
def index4():
    return render_template('index4.html')

@app.route('/index5')
def index5():
    return render_template('index5.html')

@app.route('/index6')
def index6():
    return render_template('index6.html')

@app.route('/index7')
def index7():
    return render_template('index7.html')

@app.route('/index8')
def index8():
    return render_template('index8.html')

@app.route('/proccomp')
def proccomp():
    return render_template('proccomp.html')

# Endpoint para criação de usuários (POST)
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    if not dados or 'email' not in dados or 'password' not in dados or 'nome' not in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    
    # Aqui você pode adicionar lógica para criar usuários sem Firebase
    new_user = {
        'Email': dados['email'],
        'pass': generate_password_hash(dados['password']),
        'Nome': dados['nome'],
        'role': 'user',
        'CreatedAt': 'dummy_timestamp',  # Substitua por lógica de timestamp se necessário
        'lastLogin': 'dummy_timestamp',   # Substitua por lógica de timestamp se necessário
        'Foto perfil': dados.get('foto_perfil', '')
    }
    
    return jsonify({"mensagem": "Usuário criado com sucesso", "id": "dummy_id"}), 201

# Endpoint para obter um usuário por ID (GET)
@app.route('/usuarios/<id>', methods=['GET'])
def obter_usuario(id):
    # Aqui você pode adicionar lógica para obter usuários sem Firebase
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':

