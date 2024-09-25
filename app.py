from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore

from teste_firebase import init_firebase

app = Flask(__name__)
CORS(app)

carrinho = []

if not firebase_admin._apps: 
    init_firebase()

# Conecta ao Firestore
db = firestore.client()

@app.route('/')
def index():
    return "API está online."

@app.route(' /<form_id>', methods=['GET'])
def mostrar_formulario(form_id):
    global carrinho
    
    forms = ['formVenderProduto', 'formAdicionarProduto', 'formRemoverProduto']
    for form in forms:
        if form == form_id:
            continue
        carrinho = []
        
    return jsonify({'message': f'Formulário {form_id} mostrado com sucesso.'}), 200
