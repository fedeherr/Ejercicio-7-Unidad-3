from Personal import Personal
class Investigador(Personal):
    __area = ''
    __tipo = ''
    def __init__(self, cuil, apellido, nombre, sb, antiguedad, carrera = "x", cargo = "x", catedra = "x", area = "x", tipo = "x"):
        super().__init__(cuil, apellido, nombre, sb, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__area = area
        self.__tipo = tipo
    def getArea(self):
        return self.__area
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def getTipo(self):
        return self.__tipo
    def Sueldo(self):
        return super().getBasico()*(0.1*super().getAntig())
    def __str__(self):
        return "Nombre: %s, Apellido: %s, %s, Sueldo: %f" % (super().getNombre(), super().getApellido(), 'Investigador', self.Sueldo())
 
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            area = self.__area,
                            tipo = self.__tipo
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d