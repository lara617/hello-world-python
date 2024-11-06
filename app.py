import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from botoes import gerar_botoes

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Por favor, preencha todos os campos.')
            return render_template('login.html')
        
        # Lógica para autenticar o usuário aqui
        # Substitua isso pelo seu método de autenticação atual
        user = {'email': 'exemplo@email.com', 'pass': generate_password_hash('senha')} # Exemplo de usuário
        if user and check_password_hash(user['pass'], password):
            session['user_id'] = 1  # Exemplo de ID de usuário
            session['user_role'] = 'user'
            return redirect(url_for('dashboard'))
        
        flash('Email ou senha incorretos.')
    
    return render_template('login.html')

# Rota para a página de cadastro
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        
        # Lógica para verificar e criar um novo usuário aqui
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

# Rota para o painel de controle
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')

# Rota para logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Rotas para as outras páginas
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
    botoes_html = gerar_botoes()
    return render_template('proccomp.html', botoes_html=botoes_html)


# Rota para criação de usuário (exemplo de rota de API)
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    if not dados or 'email' not in dados or 'password' not in dados or 'nome' not in dados:
        return jsonify({"erro": "Dados incompletos"}), 400

    # Lógica para criar um novo usuário aqui
    return jsonify({"mensagem": "Usuário criado com sucesso", "id": 1}), 201  # ID fictício

# Rota para obtenção de usuário (exemplo de rota de API)
@app.route('/usuarios/<id>', methods=['GET'])
def obter_usuario(id):
    # Lógica para obter dados do usuário aqui
    user_data = {"id": id, "nome": "Exemplo", "email": "exemplo@email.com"}
    return jsonify(user_data), 200

if __name__ == '__main__':
    app.run(debug=True)