from menu import Menu
from Lista import Lista
from crearAgente import crearAgente
from ObjectEncoder import ObjectEncoder
from Interface import elementos
if __name__=='__main__':
    jsonF=ObjectEncoder()
    docentes = Lista()
    bandera=True
    while bandera:
        menu=Menu()
        opcion=menu.mostrarMenu()
        if opcion==1:
            docente = crearAgente()
            ind = int(input("Ingrese la posicion a insertar el docente: "))
            docentes.insertarElemento(docente, ind)
        else:
            if opcion==2:
                docente = crearAgente()
                docentes.agregarElemento(docente)
            else:
                if opcion==3:
                    ind = int(input("Ingrese la posicion en la lista a buscar docente: "))
                    a = docentes.mostrarElemento(ind)
                    print(a)
                else:
                    if opcion==4:
                        car = input("Ingrese nombre de la carrera a mostar docentes investigadores: ")
                        docentes.listadoDocInv(car)
                    else:
                        if opcion==5:
                            area = input("Ingrese el area a ver la cantidad de investigadores y docentes investigadores")
                            docentes.AgentArea(area)
                        else:
                            if opcion == 6:
                                docentes.listAgent()
                            else:
                                if opcion == 7:
                                    cat = input("De la categoria de investigacion a buscar: ")
                                    docentes.catInvest(cat)
                                else:
                                    if opcion == 8:
                                        print("Guardando...")
                                        d=docentes.toJSON()
                                        jsonF.guardarJSONArchivo(d,'agentes.json')
                                    else:
                                        if opcion == 9:                  
                                            print("Leyendo...")
                                            diccionario=jsonF.leerJSONArchivo('agentes.json')
                                            docentes=jsonF.decodificarDiccionario(diccionario)

                                    