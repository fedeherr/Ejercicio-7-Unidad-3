from zope.interface import implementer, implements
from Nodo import Nodo
from Interface import elementos
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
import operator
@implementer(elementos)
class Lista(object):
    __comienzo = None
    __actual = None
    __indice = int
    __tope = int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def agregarElemento(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope +=1
    def insertarElemento(self, elemento, pos):
        if ((pos >= self.__tope) or (pos < 0)): raise IndexError('Indice de la lista fuera de rango')
        aux = self.__comienzo
        encontrado = False
        i = 0
        c = 0
        if (i == pos):
            self.agregarElemento(elemento)
        else:
            ant = aux
            aux = aux.getSiguiente()
            i += 1
            while ((not encontrado)&(aux != None)):
                if i == pos:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
                    i +=1
            if ((encontrado)&(aux.getSiguiente() != None)):
                viejo = aux.getDato()
                aux.setDato(elemento)
                aux = aux.getSiguiente()
                viejo2 = aux.getDato()
                aux.setDato(viejo)
                while(aux.getSiguiente() != None):
                        print(viejo2)
                        aux = aux.getSiguiente()
                        viejo = aux.getDato()
                        aux.setDato(viejo2)
                        c = 1
                        if (aux.getSiguiente() != None):
                            print(viejo)
                            aux = aux.getSiguiente()
                            viejo2 = aux.getDato()
                            aux.setDato(viejo)
                            c = 0
                if (c == 0):
                    final = Nodo(aux.getDato())
                    aux.setDato(viejo)
                    final.setDato(viejo2)
                else:
                    final = Nodo(aux.getDato())
                    aux.setDato(viejo2)
                    final.setDato(viejo)
                self.__tope+=1
                aux.setSiguiente(final)
            else:
                if(aux.getSiguiente() == None):
                    final = Nodo(aux.getDato())
                    aux.setDato(elemento)
                    aux.setSiguiente(final)
                    self.__tope+=1
    def mostrarElemento(self, pos):
        aux = self.__comienzo
        i = 0
        while i<pos and aux != None:
            aux = aux.getSiguiente()
            i +=1
        if aux == None:
            raise IndexError
        else:
            return aux.getDato()
    def listadoDocInv(self, car):
        xd = []
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            if (type(ant.getDato()) == DocenteInvestigador):
                if(ant.getDato().getCarrera() == car):
                    xd.append(ant.getDato())
        xd.sort(key=operator.methodcaller('getNombre'))
        for i in range(len(xd)):
            print (xd[i].mostrarTodo())
    def AgentArea(self, area):
        aux = self.__comienzo
        i = 0
        c = 0
        for p in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            if (type(ant.getDato()) == DocenteInvestigador):
                if (ant.getDato().getArea() == area):
                    c +=1
            if (type(ant.getDato()) == Investigador):
                if (ant.getDato().getArea() == area):
                    i +=1
        print ("Hay un total de %d investigadores, y %d docentes investigadores" % (i, c))
    def listAgent(self):
        xd = []
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            xd.append(ant.getDato())
        xd.sort(key=operator.methodcaller('getApellido'))
        for i in range(len(xd)):
            print (xd[i])
    def catInvest(self, cat):
        cat = cat.upper()
        lista = []
        total = 0
        aux = self.__actual
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            if (type(ant.getDato()) == DocenteInvestigador):
                if(ant.getDato().getCatInc() == cat):
                    lista.append(ant.getDato())
        for docinv in lista:
            print(docinv.mostrar())
            total += docinv.getImp()
            print ("El total a pagar es: ", total)

    def toJSON(self):
        dato = self.__actual.getDato()
        datolis = []
        aux = self.__comienzo
        for i in range(self.__tope):
            ant = aux
            aux = aux.getSiguiente()
            datolis.append(ant.getDato().toJSON())
        d = dict(
                __class__=self.__class__.__name__,
                datos=datolis
                )
        return d