function navigateTo(page) {
    window.location.href = page;
}

// Exemplo de interatividade adicional
document.querySelectorAll('.meu-botao').forEach(button => {
    button.addEventListener('click', () => {
        alert(`Você clicou no botão: ${button.textContent}`);
    });
});
