import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
import firebase_admin
from firebase_admin import credentials, firestore

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Adicione uma chave secreta
# Inicializa o Firebase Admin SDK
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)
db = firestore.client()

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
        
        user_ref = db.collection('Users').where('Email', '==', email).limit(1).get()
        if user_ref:
            user = user_ref[0].to_dict()
            if user and check_password_hash(user['pass'], password):
                session['user_id'] = user_ref[0].id
                return redirect(url_for('dashboard'))
        
        flash('Email ou senha incorretos.')
    
    return render_template('login.html')

# Rota para a página de cadastro
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Para este exemplo, não há persistência de dados
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))
    return render_template('signup.html')

# Rota para o painel de controle
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', user_id=session['user_id'])
    return redirect(url_for('login'))

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove o usuário da sessão
    return redirect(url_for('home'))

# Rota para a página index2
@app.route('/index2')
def index2():
    return render_template('index2.html')

# Rota para a página index3
@app.route('/index3')
def index3():
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(debug=True)
