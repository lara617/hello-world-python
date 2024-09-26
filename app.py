from flask import Flask, request, jsonify


carrinho = []

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
