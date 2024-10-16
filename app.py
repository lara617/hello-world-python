<<<<<<< HEAD
from flask import Flask, render_template
=======
<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify
>>>>>>> ac757cfa81408159cb76c60d13d09be688ce3bea

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(debug=True)
=======
@app.route(' /<form_id>', methods=['GET'])
def mostrar_formulario(form_id):
    global carrinho
    
    forms = ['formVenderProduto', 'formAdicionarProduto', 'formRemoverProduto']
    for form in forms:
        if form == form_id:
            continue
        carrinho = []
        
    return jsonify({'message': f'Formulário {form_id} mostrado com sucesso.'}), 200
>>>>>>> 5b69252083495e1891c48439447960f1aed389e6
>>>>>>> ac757cfa81408159cb76c60d13d09be688ce3bea
