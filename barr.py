# barr.py
def gerar_barra_progresso(percentual):
    """
    Gera a barra de progresso com bordas arredondadas usando HTML.
    :param percentual: Valor de 0 a 100 indicando o percentual de uso.
    :return: HTML para renderizar a barra de progresso.
    """
    barra_html = f"""
    <div class="progresso-container">
        <div class="progresso-bar" style="width: {percentual}%;"></div>
    </div>
    """
    return barra_html
