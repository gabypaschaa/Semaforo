import pygame
import sys
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de Semáforo")

# Colores
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)
GRIS = (50, 50, 50)

# Variables del semáforo
semaforo_estado = 'rojo'
tiempo_cambio = time.time()

# Variables del carro
carro_x = 0
carro_y = 500

# FPS
clock = pygame.time.Clock()

def dibujar_carretera():
    pygame.draw.rect(ventana, GRIS, (0, 450, ANCHO, 150))  # Carretera
    # Líneas amarillas centrales
    for i in range(0, ANCHO, 40):
        pygame.draw.rect(ventana, AMARILLO, (i, 525, 20, 5))
    # Paso peatonal
    for i in range(0, 100, 20):
        pygame.draw.rect(ventana, BLANCO, (350, 460 + i, 20, 10))

def dibujar_semaforo():
    pygame.draw.rect(ventana, NEGRO, (700, 100, 30, 100))  # Poste
    color_rojo = ROJO if semaforo_estado == 'rojo' else GRIS
    color_amarillo = AMARILLO if semaforo_estado == 'amarillo' else GRIS
    color_verde = VERDE if semaforo_estado == 'verde' else GRIS
    pygame.draw.circle(ventana, color_rojo, (715, 115), 10)
    pygame.draw.circle(ventana, color_amarillo, (715, 145), 10)
    pygame.draw.circle(ventana, color_verde, (715, 175), 10)

def dibujar_carro():
    pygame.draw.rect(ventana, AZUL, (carro_x, carro_y, 50, 30))

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fondo
    ventana.fill((135, 206, 235))  # Color de cielo

    # Dibujar elementos
    dibujar_carretera()
    dibujar_semaforo()
    dibujar_carro()

    # Cambiar semáforo cada 3 segundos
    if time.time() - tiempo_cambio > 3:
        if semaforo_estado == 'rojo':
            semaforo_estado = 'verde'
        elif semaforo_estado == 'verde':
            semaforo_estado = 'amarillo'
        else:
            semaforo_estado = 'rojo'
        tiempo_cambio = time.time()

    # Movimiento del carro según el semáforo
    if semaforo_estado == 'verde':
        carro_x += 5
    elif semaforo_estado == 'amarillo':
        carro_x += 2
    elif semaforo_estado == 'rojo':
        if carro_x + 50 < 350 or carro_x > 400:  # Si no está en el paso peatonal
            carro_x += 5

    # Reset carro si sale de la pantalla
    if carro_x > ANCHO:
        carro_x = -50

    pygame.display.update()
    clock.tick(60)  # 60 FPS
