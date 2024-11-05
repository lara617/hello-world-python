import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import firebase_admin
#from firebase_admin import credentials, firestore

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['1d448da9230a198fc08a16401cdceb83b094b1d6'] = os.getenv('1d448da9230a198fc08a16401cdceb83b094b1d6')

# Obtenha o diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construa o caminho para o arquivo de credenciais
cred_path = os.path.join(current_dir, 'serviceAccountKey.json')

# Use o caminho construído para o seu arquivo JSON de credenciais
cred = credentials.Certificate('dreambuilder-5a4ea-firebase-adminsdk-ek7ia-1d448da923.json')
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
                session['user_role'] = user.get('role', 'user')
                user_ref[0].reference.update({'lastLogin': firestore.SERVER_TIMESTAMP})
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
        
        # Verifica se o usuário já existe
        existing_user = db.collection('Users').where('Email', '==', email).limit(1).get()
        if existing_user:
            flash('Email já cadastrado.')
            return render_template('signup.html')
        
        # Cria novo usuário
        new_user = {
            'Email': email,
            'pass': generate_password_hash(password),
            'Nome': name,
            'role': 'user',
            'CreatedAt': firestore.SERVER_TIMESTAMP,
            'lastLogin': firestore.SERVER_TIMESTAMP,
            'Foto perfil': ''  # Pode ser atualizado posteriormente
        }
        
        db.collection('Users').add(new_user)
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('login'))
    
   # rever return render_template('signup.html')

# Rota para o painel de controle
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
      return redirect(url_for('login'))
    
    user_ref = db.collection('Users').document(session['user_id']).get()
    if user_ref.exists:
        user_data = user_ref.to_dict()
        return render_template('dashboard.html', user=user_data)
    
    return redirect(url_for('login'))

# Rota para logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Rota para a página index2
@app.route('/index2')
def index2():
    return render_template('index2.html')

# Rota para a página index3
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

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    if not dados or 'email' not in dados or 'password' not in dados or 'nome' not in dados:
        return jsonify({"erro": "Dados incompletos"}), 400
    
    # Verifica se o usuário já existe
    existing_user = db.collection('Users').where('Email', '==', dados['email']).limit(1).get()
    if len(existing_user) > 0:
        return jsonify({"erro": "Email já cadastrado"}), 409
    
    # Cria novo usuário
    new_user = {
        'Email': dados['email'],
        'pass': generate_password_hash(dados['password']),
        'Nome': dados['nome'],
        'role': 'user',
        'CreatedAt': firestore.SERVER_TIMESTAMP,
        'lastLogin': firestore.SERVER_TIMESTAMP,
        'Foto perfil': dados.get('foto_perfil', '')
    }
    
    doc_ref = db.collection('Users').document()
    doc_ref.set(new_user)
    return jsonify({"mensagem": "Usuário criado com sucesso", "id": doc_ref.id}), 201

@app.route('/usuarios/<id>', methods=['GET'])
def obter_usuario(id):
    doc_ref = db.collection('Users').document(id)
    doc = doc_ref.get()
    if doc.exists:
        user_data = doc.to_dict()
        # Remove a senha hash dos dados retornados por segurança
        user_data.pop('pass', None)
        return jsonify(user_data), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
