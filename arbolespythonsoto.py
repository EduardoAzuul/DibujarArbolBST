class Nodo:
  def __init__(self, valor):
    self.valor=valor
    self.padre=None
    self.hijos=[]
  def __repr__(self):
    return f"Nodo {self.valor}"

def relacionar(nodoPadre, nodoHijo):
  nodoPadre.hijos.append(nodoHijo)
  nodoHijo.padre=nodoPadre

def ancestros(nodo): #Si se puede evitar la recursividad, mejor
  explorador = nodo
  lista=[nodo]
  while explorador.padre:
    explorador=explorador.padre
    lista.append(explorador)
  return lista

def ancestros2(nodo):
  if not nodo.padre: return [nodo]
  return[nodo]+ancestros2(nodo.padre)

def profundidad(nodo): #Si se puede evitar la recursividad, mejor
  explorador = nodo
  suma=0
  while explorador.padre:
    explorador=explorador.padre
    suma+=1
  return suma

def descendientes(nodo):
  explorador = nodo
  lista=[nodo]
  for i in range (len(explorador.hijos)):
    lista+=descendientes(explorador.hijos[i])
  return lista

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


A=Nodo("A")
B=Nodo("B")
C=Nodo("C")
D=Nodo("D")
E=Nodo("E")
F=Nodo("F")
G=Nodo("G")
H=Nodo("H")
I=Nodo("I")

relacionar(nodoPadre=A, nodoHijo=B)
relacionar(A,C)
relacionar(A,D)
relacionar(B,E)
relacionar(B,F)
relacionar(C,G)
relacionar(G,H)
relacionar(G,I)


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


def relizq(nodoPadre, nodoHijo):
    nodoHijo.padre = nodoPadre
    nodoPadre.izq = nodoHijo

def relder(nodoPadre, nodoHijo):
    nodoHijo.padre = nodoPadre
    nodoPadre.der = nodoHijo

def descendientes(nodo):
  lista=[nodo]
  if nodo.izq:
    lista+=descendientes(nodo.izq)
  if nodo.der:
    lista+=descendientes(nodo.der)
  return lista

def sumaabajo(nodo):
  suma=1
  if nodo.izq:
    suma+=sumaabajo(nodo.izq)
  if nodo.der:
    suma+=sumaabajo(nodo.der)
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

def megapadre(nodo):
  explorador = nodo
  while explorador.padre:
    explorador=explorador.padre
  return explorador

def dfs(nodo,n):
  lista=[]
  if n==1: lista.append(nodo)
  if nodo.izq:
    lista.extend(dfs(nodo.izq,n))
  if n==2: lista.append(nodo)
  if nodo.der:
    lista.extend(dfs(nodo.der,n))
  if n==3: lista.append(nodo)
  return lista

def dfsno(nodo):
  lista=[]
  lista.append(nodo)
  if nodo.izq:
    lista.extend(dfs(nodo.izq))
    lista.append(nodo)
  if nodo.der:
    lista.extend(dfs(nodo.der))
    lista.append(nodo)
  return lista

def bfs(nodo):
  from collections import deque
  fila=deque()
  fila.append(nodo)
  resultado=[]
  while fila:
    activo=fila.popleft()
    resultado.append(activo)
    if activo.izq:
      fila.append(activo.izq)
    if activo.der:
      fila.append(activo.der)
  return resultado

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