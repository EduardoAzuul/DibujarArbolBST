from funciones_de_Trabajo import *
import pygame
import sys
l = [45, 25, 67, 12, 32, 50, 90, 27, 35, 45, 60, 80, 99, 2, 4]

abb = BST()
for v in l:
    abb.insertar(v)

# Imprimir el recorrido en inorden desde la raíz

lista_in_orden = abb.inorden(abb.raiz)
lista_niveles =[]
valores_nodos=[]
cantidad_nodo= len(lista_in_orden)
lista_padres=[]



for v in lista_in_orden:
    aux_padre=v.padre
    nodo_aux= v
    lista_niveles.append(profundidad(nodo_aux))
    valores_nodos.append( nodo_aux.valor)
    print(aux_padre)

maximo_nivel = max(lista_niveles)+1
numero_nodos = len(lista_in_orden)

wscreen, hscreen =800,600
sscreen=(wscreen,hscreen)
pygame.init()
pantalla = pygame.display.set_mode(sscreen,pygame.DOUBLEBUF)
def dibujar(numNodos,numNiveles,listaOrdenada,lista_niveles):
  #Dibuja un árbol binario de n niveles con n nodos en
  global wscreen,hscreen,pantalla
  wrect=wscreen/int(numNodos)
  hrect=hscreen/int(numNiveles)
  anterior_pos=(0,0)
  for i in range(len(listaOrdenada)):
    pygame.draw.line(pantalla, (100,100,100), (wscreen-((wrect/1.2)*(i+1)), ((hrect/1.2)*(lista_niveles[i]+1))),(wscreen-((wrect/1.2)*(i+2)),(lista_niveles[i+1]*(hrect/1.2))))
    #print("bloque:",bloque)
    #print("fila:",fila)
  pygame.display.update()

  for i in range(len(listaOrdenada)):
    pygame.draw.circle(pantalla, (100,50,50), (wscreen-((wrect/1.2)*(i+1)), ((hrect/1.2)*(lista_niveles[i+1]))), wrect/2)


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        sys.exit()
    dibujar(numero_nodos,maximo_nivel,lista_in_orden,lista_niveles)
print(lista_in_orden)
print(valores_nodos)
print(lista_niveles)
print(f"Tenemos {maximo_nivel} niveles")
print(f"Tenemos {numero_nodos} nodos")