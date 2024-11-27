import os
from dotenv import load_dotenv
from flask import Flask, render_template,   session
from werkzeug.security import check_password_hash, generate_password_hash
from graficos import create_bar_chart, create_memory_chart 
from barr import gerar_barra_progresso


# Carregar as variáveis do .env
load_dotenv()

app = Flask(__name__)
percentual_memoria = 5
@app.route('/')
def home():
    return render_template('index.html')


    
# Rota do gráfico 1 (Desempenho de Processadores)
@app.route('/index7')
def grafico1():
    graph_html = create_bar_chart()  # Gera o gráfico de barras do desempenho do processador
    return render_template('index7.html', graph_html=graph_html)
@app.route('/index6')
def grafico2():
    global percentual_memoria

    if percentual_memoria < 100:
        percentual_memoria += 5  # Aumenta 5% a cada recarregamento da página

    # Gerar o gráfico de memória
    graph_html = create_memory_chart()  # Função que gera o gráfico de velocidade de memória
    
    # Retornar a página com o gráfico de memória e a barra de progresso
    return render_template('index6.html', graph_html=graph_html, percentual=percentual_memoria)

# Outras rotas para páginas adicionais
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
    return render_template('proccomp.html')


if __name__ == '__main__':
    app.run(debug=True)