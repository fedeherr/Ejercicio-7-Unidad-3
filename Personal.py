class Personal(object):
    __cuil = 0
    __apellido = ''
    __nombre = ''
    __sb = 0
    __antiguedad = 0
    def __init__(self, cuil, apellido, nombre, sb, antiguedad, carrera = 'x', cargo = 'x', catedra = 'x', area = 'x', tipo = 'x'):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sb = sb
        self.__antiguedad = antiguedad
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getBasico(self):
        return self.__sb
    def getAntig(self):
        return self.__antiguedad
    def getCuil(self):
        return self.__cuil
    def toJSON(self):
        return dict(
            __atributos__ = dict(
                            cuil = self.__cuil,
                            apellido = self.__apellido, 
                            nombre = self.__nombre,
                            sb = self.__sb,
                            antiguedad = self.__antiguedad
                            )
                )