from flask import redirect, url_for

def acao_botao_1():
    # Lógica para o botão 1
    print("Botão 1 foi pressionado!")
    return redirect(url_for('index3'))

def acao_botao_2():
    # Lógica para o botão 2
    print("Botão 2 foi pressionado!")
    return redirect(url_for('index2'))

def gerar_botoes():
    # Lógica para gerar botões
    return ["Botão 1", "Botão 2"]


