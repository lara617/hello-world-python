import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
import firebase_admin
from firebase_admin import credentials, firestore

# Carrega as variáveis do arquivo .env
load_dotenv()

# Verifique se a variável de ambiente está carregada corretamente
print(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))  # Para depuração

app = Flask(__name__)
app.config['SECRET_KEY'] = '  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCr2U/WKd5YdVIH\ndpa3BuGPLkO4Hdnr8HrheQ89cq2HLk7g1aGWxtGTdQnriBk3IkZb5zYJXek/qC+w\n1wDUECuMtwpnMpy6rV4EPPyCq2gWYyQG1k0i1Au5sRUKLJPNQMyKExzvN2eAJ6OW\nAVFOlhLiEUeI3o3WyMBD6bpiuS/dx3yermSiBzqTMhTxvuQqgN4R9KzrNAaCGfNp\nJfu8m1pnhfaYkP8WSEe/qkbdwXRZC/2BntSvsj5PcMYnLnpFZeOH91yMGrmmW6NB\nyXXNRjjTW+wwP9qzR+xi+N8nGFdLaoEV2R+8eV+vEki548WGqciNAKcnWGpHIa1h\nHBQOiWYfAgMBAAECggEADHYCCC1aCOpc69tJW3UyxuSbwXkx/kieSG+JpN2GFV7M\nwRiMko0me5L0M1ws4+a8Lll/fWy4sfElSs/pqKGRiYRo9d8MJqx/5ukbMEhzOuhZ\nH5Z2L8KAz9K2Nq97z4Qq22TpEgmKRkHZkVIqzfrWMgapvBQojydYawmYMSTCLUp1\nhqq15qxRkKgLMDjs680KrIMdA6XbcZdP5DUBWaL452HyX3nFbjDiNV0mOehNKAhS\ncd+qxxi97nPuRbymQ/t9xh3PVuo/9XmFukXhucXOBjK6NEPBMdT9IfokJWl8XUm8\n5TtZbcN6WnNOXvKLTncmDhK49yU7CTRiONJxOAPCHQKBgQDcDObmwltQf1QFB0EH\nmQdWGzXgDuzhV82LNQ7ST/EIEEEIQ1AMLkAQBx4cCy+L20q3mKLSY1r3cy2M1LQ1\npZ/Wn5vdh5CB/A1/72JDCk2mUNefx+nudYK6r51FEZt/+wAZSbNtXTYKJW/jjJa5\nFXhuLn/iLmnXA6kPVCBSWoeBFQKBgQDH7H4rtcRE0HO4yyj2pa2UfFrTI+VwDng/\n06aGc1rTNxJp+B9Ud5/ChaFC9ljkY1nMd5vOgXuXvrRLUuB6Q0F4mzOrp65O6oT8\nH9lbtB5/tYAVencVBC6jTj8pKQR4o/jD8/ZKlc14CU6Zz/m5hsd4WE1NqoNq764x\n+eCqr1lPYwKBgQDWqityv/WOwLf5M8tnmwyCHodfLZA+gIY+oCL2XhAXuquGYQws\n5c2PFTJ1TyAyAlqQYnGsZkpujUjJUxL+JrWYDRpjcQUzGO0eeivUlK+NaN4AvGhk\nPPSsI/d7UqLspbLB+Jj2PnEiUsUlKZg7tEtIyUnuHzMXEzYQgxQI4tG/xQKBgFfm\nzGbNiZk0Cd1zPfSMTfCeaJSzELsfMZHmri4pZALAERGUrbnGyvCNLqUxiU4JvL7g\nzBmU5tGGYOFJdDdtgMjVfHd5x3MdPBFas4fVfx9pnwJSkS8lYpgc3DpttXCRr9wA\nVQbgLLIdbXjFb6g58VQhhwOh+Bw5e96vXi/N3ze/AoGAC02vuu+UXw0sakLqLTOJ\nm2acBQo8Gjc17sxRJm8NBtOWhp3gHWAkpczGTuflptZwZ4hhvWLt5xUYR1fRF34J\nFRZRhQOn9X3+PO6BC8mTsq2WLDTcNO80BiodFHsIEiAleB0p0ODYpv9Oy3Ez+B+B\nf8TG+ToxtMkWt1LrDYpwGNI=\n-----END PRIVATE KEY-----\n"'  # Adicione uma chave secreta

# Defina o caminho do arquivo JSON diretamente
cred = credentials.Certificate("C:/Users/Abdaisy Conaição/Desktop/PI1/salvação/programacao-avancada-com-python-10794/dreambuilder-5a4ea-firebase-adminsdk-ek7ia-1d448da923.json")
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
