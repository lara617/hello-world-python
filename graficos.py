from flask import Flask, render_template
import plotly.graph_objects as go

app = Flask(__name__)

# Função que gera o gráfico de barras (Desempenho dos Processadores)
def create_bar_chart():
    categories = [
        'Jogos de Alto Desempenho', 'Edição de Vídeo', 'Tarefas Cotidianas',
        'Design Gráfico', 'Portabilidade e Bateria', 'Aplicações em Nuvem', 
        'Computação de Baixa Potência'
    ]
    performance_scores = [90, 80, 70, 75, 60, 85, 55]
    
    fig = go.Figure(data=[go.Bar(
        x=categories, 
        y=performance_scores, 
        marker=dict(
            color=['rgba(0, 86, 179, 0.6)', 'rgba(255, 87, 34, 0.6)', 'rgba(76, 175, 80, 0.6)', 
                   'rgba(156, 39, 176, 0.6)', 'rgba(255, 152, 0, 0.6)', 'rgba(33, 150, 243, 0.6)', 
                   'rgba(96, 125, 139, 0.6)'],
            line=dict(color='rgba(0, 0, 0, 0.1)', width=1)
        )
    )])

    fig.update_layout(
        title="Desempenho dos Processadores em Diferentes Tarefas",
        xaxis_title="Categorias",
        yaxis_title="Pontuação de Desempenho",
        yaxis=dict(range=[0, 100]),
        template="plotly_dark"
    )
    
    return fig.to_html(full_html=False)

# Função que gera o gráfico de memória (Velocidade de Memória por Tipo)
def create_memory_chart():
    memory_types = ['RAM', 'ROM', 'Cache', 'Memória Flash', 'HDD', 'SSD']
    speeds = [3200, 150, 8000, 500, 120, 3000]

    fig = go.Figure(data=[go.Bar(
        x=memory_types, 
        y=speeds, 
        marker=dict(
            color=['rgba(75, 192, 192, 0.6)', 'rgba(255, 99, 132, 0.6)', 'rgba(255, 205, 86, 0.6)', 
                   'rgba(54, 162, 235, 0.6)', 'rgba(255, 159, 64, 0.6)', 'rgba(153, 102, 255, 0.6)'],

            color=['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)', 
                   'rgba(54, 162, 235, 0.2)', 'rgba(255, 159, 64, 0.2)', 'rgba(153, 102, 255, 0.2)'],
            line=dict(color=['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)', 
                             'rgba(54, 162, 235, 1)', 'rgba(255, 159, 64, 1)', 'rgba(153, 102, 255, 1)'], width=1)
        )
    )])

    fig.update_layout(
        title="Velocidade de Memória por Tipo (em MB/s)",
        xaxis_title="Tipo de Memória",
        yaxis_title="Velocidade (em MB/s)",
        template="plotly_dark"
    )
    
    return fig.to_html(full_html=False)

# Rota para o gráfico de desempenho dos processadores
@app.route("/index6")
def grafico1():
    graph_html = create_bar_chart()  # Função que gera o gráfico de desempenho
    return render_template("index6.html", graph_html=graph_html)

# Rota para o gráfico de velocidade de memória
@app.route("/index7")
def grafico2():
    graph_html = create_memory_chart()  # Função que gera o gráfico de memória
    return render_template("index7.html", graph_html=graph_html)

# Função principal para rodar o app
if __name__ == "__main__":
