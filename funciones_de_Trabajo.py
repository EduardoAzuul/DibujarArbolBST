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
    for i in range (len(l)) :
       l[i].y=profundidad(i)
       l[i].x=i
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
      regresar=[self.raiz]
      actual = self.raiz
      while True:
        if actual.valor == valor:
          return regresar  # No insertamos duplicados
        elif valor < actual.valor:  # Vamos a la izquierda
          if not actual.izq:
            return None
          actual = actual.izq
          regresar.append(actual)
        else:  # Vamos a la derecha
          if not actual.der:
            return None
          actual = actual.der
          regresar.append(actual)

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
  

###################################
  def rotar(self, nodo):
    if nodo ==self.raiz:
       return None
    
    if nodo.der:
      auxder=nodo.der

    padre = nodo.padre
    abuelo = padre.padre

    if not padre:  # Verificación adicional de seguridad
        return None

    
    # Si el padre es raíz
    if padre == self.raiz:
        self.raiz = nodo
        nodo.padre = None

        
    else:     #le asignamos el hijo correspondiente al abuelo
        if abuelo:
          nodo.padre = abuelo
          if abuelo.izq == padre:
              abuelo.izq = nodo
          else:
              abuelo.der = nodo

    # El antiguo subárbol izquierdo del nodo se convierte en subárbol derecho del padre
        aux = nodo.izq  #aux es el subarbol
        padre.der = aux

    #Si fue en el nodo derecho
    if padre.der == nodo:

        # El nodo adopta a su padre como hijo izquierdo
        nodo.izq = padre
        padre.padre = nodo
        
        
        
        if aux: #si hay un subarbol
            padre.der = aux
            aux.padre = padre

    # Rotación cuando el nodo es hijo izquierdo
    elif padre.izq == nodo:
        # Guardamos el subárbol
        axu = nodo.der
        
        # El nodo adopta a su padre como hijo derecho
        nodo.der = padre
        padre.padre = nodo
        
        # El antiguo subárbol derecho del nodo se convierte en subárbol izquierdo del padre
        padre.izq = aux
        if aux:
            aux.padre = padre

    nodo.der
    return None
     
    



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
          
