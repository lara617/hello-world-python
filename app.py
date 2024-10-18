from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)


# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Verifica se o usuário existe e a senha está correta
        if email in users and users[email] == password:
            session['user'] = email  # Armazena o usuário na sessão
            return redirect(url_for('dashboard'))
        else:
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
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('login'))

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove o usuário da sessão
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
