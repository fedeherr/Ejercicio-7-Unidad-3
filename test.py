import operator
class A():
    __x = 0
    __z = 0
    def __init__(self, x, z):
        self.__x = x
        self.__z = z
    def __str__(self):
        return "x: %d z: %d" % (self.__x, self.__z)
    def getX(self):
        return self.__x
def test(e):
    return e['x']

lista = []
b = A(0, 0)
for i in range(5):
    x = A(i, i+1)
    lista.append(x)
lista[2] = b
for i in range(5):
    print (lista[i])
lista.sort(key=operator.methodcaller('getX'))
for i in range(5):
    print (lista[i])