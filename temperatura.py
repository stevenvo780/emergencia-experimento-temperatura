import random
import statistics


class Particle:
    def __init__(self):
        self.speed = random.uniform(0, 10)  # Velocidad inicial aleatoria

    def collide(self, other):
        # Simulación simplificada de una colisión
        avg_speed = (self.speed + other.speed) / 2
        fluctuation = random.uniform(-2, 2)

        self.speed = avg_speed + fluctuation
        other.speed = avg_speed - fluctuation


def calculate_temperature(particles):
    # La "temperatura" se calcula como la desviación estándar de las velocidades
    speeds = [p.speed for p in particles]
    return statistics.stdev(speeds)


# Crear un sistema de 100 partículas
particles = [Particle() for _ in range(100)]

# Estado inicial del sistema
initial_temperature = calculate_temperature(particles)
print(f"Temperatura inicial: {initial_temperature}")

# Simulación de colisiones
for _ in range(1000):
    p1, p2 = random.sample(particles, 2)
    p1.collide(p2)

# Estado final del sistema
final_temperature = calculate_temperature(particles)
print(f"Temperatura final: {final_temperature}")

# La temperatura final del sistema emerge de las interacciones entre las partículas
# y no puede preverse simplemente observando las propiedades individuales de cada partícula.
