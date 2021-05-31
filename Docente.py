from Personal import Personal
class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''
    def __init__(self, cuil, apellido, nombre, sb, antiguedad, carrera, cargo , catedra, area = 'x', tipo = 'x'):
        super().__init__(cuil, apellido, nombre, sb, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def getBasico(self):
        return super().getBasico()
    def getAntig(self):
        return super().getAntig()
    def getCargo(self):
        return self.__cargo
    def __str__(self):
        return "Nombre: %s, Apellido: %s, %s, Sueldo: %f" % (super().getNombre(), super().getApellido(), 'Docente', self.Sueldo())
    def getCarrera(self):
        return self.__carrera
    def getCatedra(self):
        return self.__catedra
    def Sueldo(self):
        sueldo = self.getBasico()
        if self.__cargo == "Simple":
            sueldo += sueldo*0.1
        elif self.__cargo == "Semiexclusivo":
            sueldo += sueldo*0.2
        else:
            sueldo += sueldo*0.5
        sueldo += self.getBasico()*(0.01*self.getAntig())
        return sueldo
    def toJSON(self):
        d = dict(
                __class__ = self.__class__.__name__, 
                __atributos__ = dict(
                            carrera = self.__carrera,
                            cargo = self.__cargo, 
                            catedra = self.__catedra
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d