import os
from dotenv import load_dotenv
from flask import Flask, render_template

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Acessa a variável de ambiente
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

if __name__ == '__main__':
    print(f"dreambuilder-5a4ea-firebase-adminsdk-ek7ia-1d448da923.json")  # Apenas para verificar se a variável foi carregada corretamente
    app.run(debug=True)
