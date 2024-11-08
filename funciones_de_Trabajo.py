class Nodo:
  def __init__(self, valor):
    self.valor=valor
    self.padre=None
    self.izq=None
    self.der=None
    self.x=None
    self.y=None
  def hijos(self):
    r=[]
    if self.izq:
      r.append(self.izq)
    if self.der:
      r.append(self.der)
    return r
  def __repr__(self):
    return f"Nodo {self.valor}"
  

  
def mayor(nodo):
    while nodo.der:  # Recorre a la derecha mientras haya nodos
        nodo = nodo.der
    return nodo  


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

def menor(nodo):
      while nodo.izq:  # Recorre a la izquierda mientras haya nodos
          nodo = nodo.izq
      return nodo

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

  def rango(self,valormin,valormax):
    lista_in_orden = self.inorden(self.raiz)
    lista_rango=[]
    for nodo in lista_in_orden:
       if nodo.valor>=valormin and nodo.valor<=valormax:
          lista_rango.append(nodo)
    return lista_rango

  def eliminar(self, valor):  # Añadido método eliminar al BST
          nodo = self.buscar(valor)
          if nodo:
              self.eliminar_nodo(nodo)
          return None
  
  ##############################
  def rotar(self,nodo):
     if nodo == self.raiz:  #si es raiz sale de la funcion
        return None 
     padre=nodo.padre

     if padre.der==nodo:  #si es el nodo de la derecha
        if nodo.izq:
          if (padre.padre): #si tiene abuelo
            abuelo=padre.padre
            nodo.padre= abuelo
            if(abuelo.der == padre):  #si es el nodo de la derecha del abuelo
                abuelo.der= nodo
            else:
                abuelo.izq=nodo  
                  
          padre.der=nodo.izq
          if nodo.izq:
            nodo.izq.padre=padre
            nodo.izq=padre
        if nodo.der:
          if (padre.padre): #si tiene abuelo
            abuelo=padre.padre
            nodo.padre= abuelo
            if(abuelo.der == padre):  #si es el nodo de la derecha del abuelo
                abuelo.der= nodo
            else:
                abuelo.izq=nodo  
                  
          padre.izq=nodo.der
          if(nodo.der):
            nodo.der.padre=padre
            nodo.der=padre
          


     if padre== self.raiz:  #si es el nodo raiz
        self.raiz=nodo
    



  def eliminar_nodo(self,nodo):

    # Caso 1: Nodo hoja
    if not nodo.izq and not nodo.der:
      if nodo == nodo.padre:
          self.raiz = None
      else:
          padre = nodo.padre
          if padre.izq == nodo:
              padre.izq = None
          else:
              padre.der = None
          nodo.padre = None

   # Caso 2: Nodo con un hijo
    elif nodo.izq and not nodo.der:
      if nodo == self.raiz:
          self.raiz = nodo.izq
          nodo.izq.padre = None
      else:
          padre = nodo.padre
          if padre.izq == nodo:
              padre.izq = nodo.izq
          else:
              padre.der = nodo.izq
          nodo.izq.padre = padre
    
    elif nodo.der and not nodo.izq:
      if nodo == self.raiz:
          self.raiz = nodo.der
          nodo.der.padre = None
      else:
          padre = nodo.padre
          if padre.izq == nodo:
              padre.izq = nodo.der
          else:
              padre.der = nodo.der
          nodo.der.padre = padre

    # Caso 3: Nodo con dos hijos
    else:
      sucesor = self.mayor(nodo.izq)
      nodo.valor = sucesor.valor
      self.eliminar_nodo(sucesor)
      print(sucesor)

  def inorden(self, nodo):
      l=[]
      if nodo.izq : l.extend(self.inorden(nodo.izq))
      l.append(nodo)
      if nodo.der : l.extend(self.inorden(nodo.der))
      return l

def _reemplazar_nodo(self, nodo, nuevo_nodo):
    
    if nodo.padre == None:  # Es la raíz
        self.raiz = nuevo_nodo
        nuevo_nodo.padre = None
    else:
        padre = nodo.padre
        if padre.izq == nodo:
            padre.izq = nuevo_nodo
        else:
            padre.der = nuevo_nodo
        if nuevo_nodo:
            nuevo_nodo.padre = padre
    
    if nodo.der:
       nuevo_nodo.der=nodo.der
       nodo.der.padre=nuevo_nodo

    if nodo.izq:
       nuevo_nodo.der=nodo.izq
       nodo.izq.padre=nuevo_nodo
    
    limpiar(nodo)  # Limpiamos el nodo original, no el nuevo
    nodo.valor=nuevo_nodo.valor

    limpiar(nuevo_nodo)

def limpiar(nodo):
    nodo.valor= None
    nodo.der= None
    nodo.izq=None
    nodo.padre=None

    if not nodo.padre == None:  ##Si no es su raiz
          padre = nodo.padre
          if  padre.izq == nodo:
            padre.izq = None
          else:
              padre.der = None
          
