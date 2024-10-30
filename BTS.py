from funciones_de_Trabajo import *

l = [45, 25, 67, 12, 32, 50, 90, 27, 35, 45, 60, 80, 99, 2, 4]

abb = BST()
for v in l:
    abb.insertar(v)

# Imprimir el recorrido en inorden desde la raíz

lista_in_orden = abb.inorden(abb.raiz)
lista_niveles =[]
valores_nodos=[]
cantidad_nodo= len(lista_in_orden)



for v in lista_in_orden:

    nodo_aux= v
    lista_niveles.append(profundidad(nodo_aux))
    valores_nodos.append( nodo_aux.valor)

maximo_nivel = max(lista_niveles)+1
numero_nodos = len(lista_in_orden)


print(lista_in_orden)
print(valores_nodos)
print(lista_niveles)
print(f"Tenemos {maximo_nivel} niveles")
print(f"Tenemos {numero_nodos} nodos")