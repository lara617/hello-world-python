import random
from flask import Blueprint, render_template

particles_service = Blueprint('particles_service', __name__)

particles = [
    {"x": random.uniform(0, 100), "y": random.uniform(0, 100), "weight": random.uniform(0.02, 0.05)}
    for _ in range(100)
]



@particles_service.route('/particles_view')
def particles_view():
    # Atualiza a posição das partículas
    for particle in particles:
        particle['weight'] += 0.001
        particle['y'] += particle['weight']
        particle['x'] += (particle['weight'] * 0.2)
        
        # Reiniciar a posição ao sair da tela
        if particle['y'] > 100:
            particle['y'] = 0
            particle['x'] = random.uniform(0, 100)
            particle['weight'] = random.uniform(0.02, 0.05)
            
    return render_template('particles_view.html', particles=particles)

@particles_service.route('/index4', endpoint='index4')
def index4():
    particles = [{'x': random.uniform(0, 100), 'y': random.uniform(0, 100)} for _ in range(10)]  # Menos partículas para teste
    return render_template('index4.html', particles=particles)

