class Nodo:
  def __init__(self, valor):
    self.valor=valor
    self.padre=None
    self.izq=None
    self.der=None
  def hijos(self):
    r=[]
    if self.izq:
      r.append(self.izq)
    if self.der:
      r.append(self.der)
    return r
  def __repr__(self):
    return f"Nodo {self.valor}"
  
  def mayor(self, nodo):
    while nodo.der:  # Recorre a la derecha mientras haya nodos
        nodo = nodo.der
    return nodo
  
def limpiar(nodo):
  nodo.valor= None
  nodo.der= None
  nodo.izq=None
  nodo.padre=None

def eliminar_nodo(nodo):
    if(nodo.izq == None and nodo.der == None):
        nodo.valor= None
        if(nodo.padre.izq== nodo):
            nodo.padre.izq = None
        else:
            nodo.padre.der= None
    if(nodo.izq and not nodo.der):
      nodo.izq.padre=nodo.padre
      nodo.valor=None

    if(nodo.der and not nodo.izq):
      nodo.der.padre=nodo.padre
      nodo.valor=None
    
    if(nodo.izq and nodo.der):
      nodo= mayor(nodo.izq)
      nodo.valor=None


def profundidad(nodo): #Si se puede evitar la recursividad, mejor
  explorador = nodo
  suma=0
  while explorador.padre:
    explorador=explorador.padre
    suma+=1
  return suma

def descendientestotales(nodo):
  explorador=nodo
  suma=1
  for i in range (len(explorador.hijos)):
    suma+=descendientestotales(explorador.hijos[i])
  return suma

def megapadre(nodo):
  explorador = nodo
  while explorador.padre:
    explorador=explorador.padre
  return explorador

def sumatotal(nodo):
  explorador=megapadre(nodo)
  suma=descendientestotales(explorador)
  return suma

def altura(nodo): 
  profizq=0
  profder=0
  if nodo.izq:
    profizq+=altura(nodo.izq)+1
  if nodo.der:
    profder+=altura(nodo.der)+1
  if profizq>profder:
    return profizq
  return profder

'''Este es el árbol que lo acomoda (se supone que esta probado)'''
class BST:
  def __init__(self):
    self.raiz=None

  def insertar(self, valor):
    if not self.raiz:
      nuevo = Nodo(valor)
      self.raiz = nuevo
      return nuevo
    else:
      actual = self.raiz
      while True:
        if actual.valor == valor:
          return actual  # No insertamos duplicados
        elif valor < actual.valor:  # Vamos a la izquierda
          if not actual.izq:
            nuevo = Nodo(valor)
            nuevo.padre = actual
            actual.izq = nuevo
            return nuevo
          actual = actual.izq
        else:  # Vamos a la derecha
          if not actual.der:
            nuevo = Nodo(valor)
            nuevo.padre = actual
            actual.der = nuevo
            return nuevo
          actual = actual.der

  def ancestros(self,nodo):
    actual=nodo
    l=[nodo]
    while actual.padre:
      actual=actual.padre
      l.append(actual)
    return l

  def inorden(self, nodo):
    l=[]
    if nodo.izq : l.extend(self.inorden(nodo.izq))
    l.append(nodo)
    if nodo.der : l.extend(self.inorden(nodo.der))
    return l

  def mayor(self, nodo):
    while nodo.der:  # Recorre a la derecha mientras haya nodos
        nodo = nodo.der
    return nodo

  def menor(self, nodo):
      while nodo.izq:  # Recorre a la izquierda mientras haya nodos
          nodo = nodo.izq
      return nodo

  def buscar(self, valor):
      actual = self.raiz
      while True:
        if actual.valor == valor:
          return actual  # No insertamos duplicados
        elif valor < actual.valor:  # Vamos a la izquierda
          if not actual.izq:
            return None
          actual = actual.izq
        else:  # Vamos a la derecha
          if not actual.der:
            return None
          actual = actual.der


A=Nodo("A")
B=Nodo("B")
C=Nodo("C")
D=Nodo("D")
E=Nodo("E")
F=Nodo("F")
G=Nodo("G")
H=Nodo("H")
I=Nodo("I")


