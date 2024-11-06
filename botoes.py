from flask import url_for

def gerar_botoes():
    botoes = [
        {"texto": "Organização de um Computador", "rota": "index4"},
        {"texto": "Componentes do Computador", "rota": "index5"},
        {"texto": "Unidade de Memória", "rota": "index6"},
        {"texto": "Processador", "rota": "index7"}
    ]
    botoes_html = ""
    for botao in botoes:
        rota = url_for(botao["rota"])
        botoes_html += f'<a href="{rota}"><button class="modern-button">{botao["texto"]}</button></a>\n'
    return botoes_html
