from Personal import Personal
class Apoyo(Personal):
    __cat = ''
    def __init__(self, cuil, apellido, nombre, sb, antiguedad, cat):
        super().__init__(cuil, apellido, nombre, sb, antiguedad)
        self.__cat = cat
    def getNombre(self):
        return super().getNombre()
    def getApellido(self):
        return super().getApellido()
    def Sueldo(self):
        sueldo = super().getBasico()
        if self.__cat <= 10:
            sueldo *= 0.1
        elif self.__cat <= 20:
            sueldo *= 0.2
        else:
            sueldo *= 0.3
        sueldo += self.getBasico()*(self.getAntig()*0.1)
        return sueldo
    def __str__(self):
        return "Nombre: %s, Apellido: %s, %s, Sueldo: %f" % (super().getNombre(), super().getApellido(), 'Apoyo', self.Sueldo())
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                        cat = self.__cat
                            )
            )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d