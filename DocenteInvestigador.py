from Docente import Docente
from Investigador import Investigador
class DocenteInvestigador(Docente, Investigador):
    __catinc = ''
    __imp = 0
    def __init__(self, cuil, apellido, nombre, sb, antiguedad, carrera, cargo, catedra, area, tipo, catinc, imp):
        super().__init__(cuil, apellido, nombre, sb, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__catinc = catinc
        self.__imp = imp 
    def getArea(self):
        return super().getArea()
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def Sueldo(self):
        return  Docente.Sueldo(self) + self.__imp
    def getCatInc(self):
        return self.__catinc
    def getCarrera(self):
        return super().getCarrera()
    def mostrar(self):
        return "Apellido: %s Nombre: %s Importe extra %f" % (super().getApellido(), super().getNombre(), self.__imp)
    def mostrarTodo(self):
        return "Nombre: %s, Apellido: %s, Sueldo basico: %f, Cuil: %d, Antiguedad: %d, Carrera: %s, Cargo: %s, Catedra: %s, Area: %s, Tipo: %s, Categoria incentivos: %s, Importe extra: %d" % (super().getNombre(), super().getApellido(), super().getBasico(), super().getCuil(), super().getAntig(),super().getCarrera(),super().getCargo(),super().getCatedra(),super().getArea(),super().getTipo(),self.__catinc,self.__imp)
    def getImp(self):
        return self.__imp
    def __str__(self):
        return "Nombre: %s, Apellido: %s, Docente Investigador, Sueldo: %f" % (super().getNombre(), super().getApellido(), self.Sueldo())
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                            imp = self.__imp,
                            catinc = self.__catinc, 
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d
