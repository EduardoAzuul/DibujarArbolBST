from funciones_de_Trabajo import *
import pygame
import sys

def actualizar_listas(arbol):
    """Función para actualizar las listas después de modificar el árbol"""
    lista_in_orden = arbol.inorden(arbol.raiz)
    print(lista_in_orden)
    lista_niveles = []
    valores_nodos = []
    
    lista_padres = []
    
    for v in lista_in_orden:
        lista_niveles.append(profundidad(v))
        valores_nodos.append(v.valor)
        if v.padre:
            lista_padres.append(v.padre.valor)
        else:
            lista_padres.append(None)

    print(valores_nodos)     
    maximo_nivel = max(lista_niveles) + 1 if lista_niveles else 1
    numero_nodos = len(lista_in_orden)
    
    return lista_in_orden, lista_niveles, valores_nodos, lista_padres, maximo_nivel, numero_nodos

# Inicialización del árbol
l = [45, 25, 67, 12, 32, 50, 90, 27, 35, 45, 60, 80, 99, 2, 4]
abb = BST()
for v in l:
    abb.insertar(v)

# Obtener información inicial del árbol
lista_in_orden, lista_niveles, valores_nodos, lista_padres, maximo_nivel, numero_nodos = actualizar_listas(abb)

# Inicialización de Pygame
pygame.init()
wscreen, hscreen = 800, 600
sscreen = (wscreen, hscreen)
pantalla = pygame.display.set_mode(sscreen, pygame.DOUBLEBUF)
pygame.display.set_caption("Visualización Árbol Binario")

def dibujar(numNodos, numNiveles, listaOrdenada, lista_niveles, valores_nodos):
    pantalla.fill((255, 255, 255))  # Fondo blanco
    if numNodos == 0:  # Si no hay nodos, no dibujamos nada
        pygame.display.update()
        return
        
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
mostrar_original = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if mostrar_original:
        # Mostrar árbol original
        dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles, valores_nodos)
        pygame.time.wait(2000)
        
        # Eliminar nodo y actualizar información
        nodo_a_eliminar = abb.buscar(12)
        if nodo_a_eliminar:
            abb.eliminar_nodo(nodo_a_eliminar)
            # Actualizar todas las listas después de la eliminación
            lista_in_orden, lista_niveles, valores_nodos, lista_padres, maximo_nivel, numero_nodos = actualizar_listas(abb)
        mostrar_original = False
    else:
        dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles, valores_nodos)
        pygame.time.wait(200)

pygame.quit()
sys.exit()