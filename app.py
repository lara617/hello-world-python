from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Inicializando o carrinho
carrinho = []

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/<form_id>', methods=['GET'])
def mostrar_formulario(form_id):
    global carrinho
    
    forms = ['formVenderProduto', 'formAdicionarProduto', 'formRemoverProduto']
    if form_id in forms:
        carrinho = []  # Limpa o carrinho se o formulário correspondente for mostrado
        return jsonify({'message': f'Formulário {form_id} mostrado com sucesso.'}), 200
    else:
        return jsonify({'error': 'Formulário não encontrado.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
