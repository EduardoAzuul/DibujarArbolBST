from funciones_de_Trabajo import *
import pygame
import sys


l = [45, 25, 67, 12, 32, 50, 90, 27, 35, 45, 60, 80, 99, 2, 4]

abb = BST()
for v in l:
    abb.insertar(v)

# Obtener recorrido inorden
lista_in_orden = abb.inorden(abb.raiz)
lista_niveles = []
valores_nodos = []
lista_padres = []

# Recolectar información de los nodos
for v in lista_in_orden:
    lista_niveles.append(profundidad(v))
    valores_nodos.append(v.valor)
    if v.padre:
        lista_padres.append(v.padre.valor)
    else:
        lista_padres.append(None)

maximo_nivel = max(lista_niveles) + 1
numero_nodos = len(lista_in_orden)

# Inicialización de Pygame
pygame.init()
wscreen, hscreen = 800, 600
sscreen = (wscreen, hscreen)
pantalla = pygame.display.set_mode(sscreen, pygame.DOUBLEBUF)
pygame.display.set_caption("Visualización Árbol Binario")

def dibujar(numNodos, numNiveles, listaOrdenada, lista_niveles):
    pantalla.fill((255, 255, 255))  # Fondo blanco
    wrect = wscreen / (numNodos + 1)  # Ajuste para mejor distribución
    hrect = hscreen / numNiveles

    # Dibujar conexiones
    for i in range(len(listaOrdenada) - 1):
        start_pos = (wscreen - ((wrect) * (i + 1)), ((hrect) * (lista_niveles[i] + 1)))
        end_pos = (wscreen - ((wrect) * (i + 2)), (hrect * (lista_niveles[i + 1] + 1)))
        pygame.draw.line(pantalla, (100, 100, 100), start_pos, end_pos, 2)

    # Dibujar nodos
    for i in range(len(listaOrdenada)):
        pos = (wscreen - ((wrect) * (i + 1)), ((hrect) * (lista_niveles[i] + 1)))
        pygame.draw.circle(pantalla, (100, 50, 50), pos, 20)
        
        # Añadir valores de los nodos
        font = pygame.font.Font(None, 24)
        text = font.render(str(valores_nodos[i]), True, (255, 255, 255))
        text_rect = text.get_rect(center=pos)
        pantalla.blit(text, text_rect)

    pygame.display.update()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles)
    pygame.time.wait(100)  # Pequeña pausa para reducir uso de CPU

pygame.quit()
sys.exit()