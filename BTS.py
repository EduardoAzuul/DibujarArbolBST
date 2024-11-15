from funciones_de_Trabajo import *
import pygame
import sys
import math

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
l = [45, 25, 67, 12, 32, 50,100,30, 90, 27, 35, 45, 60, 80, 99, 2, 4]
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
        
    wrect = wscreen / (numNodos+1)  # Ajuste para mejor distribución
    hrect = hscreen / (numNiveles+1)

    for i in range(len(listaOrdenada)):
        pos = (((wrect) * (i + 1)), ((hrect) * (lista_niveles[i] + 1)))
        pygame.draw.circle(pantalla, (100, 50, 50), pos, wrect/1.2)
        lista_in_orden[i].x=(i + 1)
        lista_in_orden[i].y=lista_niveles[i] + 1
        # Añadir valores de los nodos
        font = pygame.font.Font(None, 24)
        text = font.render(str(valores_nodos[i]), True, (255, 255, 255))
        text_rect = text.get_rect(center=pos)
        pantalla.blit(text, text_rect)

    # Dibujar conexiones
    for i in range(len(listaOrdenada) ):
        if lista_in_orden[i].padre:
            start_pos = ( ((wrect) * lista_in_orden[i].padre.x), ((hrect) * lista_in_orden[i].padre.y))
            end_pos = ( ((wrect) * lista_in_orden[i].x), (hrect * lista_in_orden[i].y))
            pygame.draw.line(pantalla, (100, 100, 100), start_pos, end_pos, 2)

    # Dibujar nodos


    pygame.display.update()

def dibujar_rango(numNodos, numNiveles,lista):
        
    wrect = wscreen / (numNodos+1)  # Ajuste para mejor distribución
    hrect = hscreen / (numNiveles+1)

    for i in range(len(lista)):
        pos = (((wrect) * (lista[i].x)), ((hrect) * (lista[i].y)))
        pygame.draw.circle(pantalla, (0, 150, 0), pos, wrect/1.2)

        # Añadir valores de los nodos
        font = pygame.font.Font(None, 24)
        text = font.render(str(lista[i].valor), True, (255, 255, 255))
        text_rect = text.get_rect(center=pos)
        pantalla.blit(text, text_rect)

    # Dibujar nodos

    pygame.display.update()

# Loop principal
running = True
mostrar_original = True
input_text = ""
input_active = False  
input_rect = pygame.Rect(50, 100, 200, 32)
input_rect_erase = pygame.Rect(55, 105, 195, 25)
font = pygame.font.Font(None, 24)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


            ####CLICKKKK
        left=1
        right=3
        if event.type == pygame.MOUSEBUTTONUP:
            posMouse = pygame.mouse.get_pos()
            wrect = wscreen / (numero_nodos+1)
            hrect = hscreen / (maximo_nivel+1)
            x_alt = round(posMouse[0]/wrect)
            y_alt = round(posMouse[1]/hrect)

            if(event.button==left):
                for i in lista_in_orden:
                    if i.x == x_alt:
                        abb.eliminar_nodo(i)
                        break 
            elif(event.button==right):
                for i in lista_in_orden:
                    if i.x == x_alt:
                        abb.rotar(i)
                        break 
            lista_in_orden, lista_niveles, valores_nodos, lista_padres, maximo_nivel, numero_nodos = actualizar_listas(abb)
            mostrar_original = True  # Mantener como True para redibujar
            # Forzar el redibujo inmediatamente
            dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles, valores_nodos)


        if event.type == pygame.KEYUP:
            if event.key==pygame.K_r:
                indicaciones = font.render("Datos a ingresar: numero menor, numero mayor", True, (0,0,0))
                pantalla.blit(indicaciones, (input_rect.x , input_rect.y - 50))
                indicaciones2 = font.render("Ejemplo:40,50", True, (0,0,0))
                pantalla.blit(indicaciones2, (input_rect.x , input_rect.y - 25))

                text_surface = font.render(input_text, True, (255,255,255))
                pantalla.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                pygame.draw.rect(pantalla, (50, 50, 50), input_rect, 2)  # Dibujar el rectángulo de la caja de texto
                input_active = True
                pygame.display.update()
            
                while input_active:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key==pygame.K_RETURN:
                                pantalla.fill((0,0,0))
                                dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles, valores_nodos)

                                input_text = input_text[:-1]
                                input_active = False
                                datos=input_text.split(',')
                                
                                lista_a_dibujar=abb.rango(int(datos[0]),int(datos[1]))
                                mostrar_original=False
                                dibujar_rango(numero_nodos,maximo_nivel,lista_a_dibujar)
                                input_text = ""
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                input_text = input_text[:-1]
                                pygame.draw.rect(pantalla, (255,255,255), input_rect_erase)
                                pygame.display.update()
                            else:
                                input_text += event.unicode
                        elif event.type == pygame.QUIT:
                            input_active=False
                            running = False
                    
                    text_surface = font.render(input_text, True, (0,0,0))
                    pantalla.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                    input_rect.w = max(140, text_surface.get_width() + 10)
                        
                    pygame.display.update()
            if event.key==pygame.K_i:
                indicaciones = font.render("Ingrese un numero:", True, (0,0,0))
                pantalla.blit(indicaciones, (input_rect.x , input_rect.y - 50))

                text_surface = font.render(input_text, True, (255,255,255))
                pantalla.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                pygame.draw.rect(pantalla, (50, 50, 50), input_rect, 2)  # Dibujar el rectángulo de la caja de texto
                input_active = True
                pygame.display.update()
                while input_active:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key==pygame.K_RETURN:
                                pantalla.fill((0,0,0))
                                dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles, valores_nodos)

                                input_text = input_text[:-1]
                                input_active = False
                                
                                
                                print("ahaia")
                                abb.insertar(int(input_text))
                                lista_in_orden, lista_niveles, valores_nodos, lista_padres, maximo_nivel, numero_nodos = actualizar_listas(abb)
                                mostrar_original=True
                                input_text = ""
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                input_text = input_text[:-1]
                                pygame.draw.rect(pantalla, (255,255,255), input_rect_erase)
                                pygame.display.update()
                            else:
                                input_text += event.unicode
                        elif event.type == pygame.QUIT:
                            input_active=False
                            running = False
                    
                    text_surface = font.render(input_text, True, (0,0,0))
                    pantalla.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                    input_rect.w = max(140, text_surface.get_width() + 10)
                        
                    pygame.display.update()
            if event.key==pygame.K_b:   
                busqueda=abb.buscar(100) 
                print("busc:",busqueda)



    if mostrar_original:
        # Mostrar árbol original
        
        dibujar(numero_nodos, maximo_nivel, lista_in_orden, lista_niveles, valores_nodos)
        pygame.time.wait(500)


pygame.quit()
sys.exit()