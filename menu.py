# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:49:24 2020
@author: morte
"""
class Menu(object):
    def mostrarMenu(self):
        print('Menú de Opciones: ')
        print('-----------------')
        print('1 - Insertar un Agente')
        print('2 - Agregar un Agente')
        print('3 - Ver Agente de una posición.')
        print('4 - Docentes Investigadores de una carrera')
        print('5 - Ver Agentes de Investigación')
        print('6 - Ver Sueldos')
        print('7 - Buscar una categoria de investigacion')
        print('8 - Almacenar los datos de la lista en un el archivo')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione un número del 1 al 6: '))
            if opcion in [1,2,3,4,5,6,7,8,9]:
                opcionCorrecta=True
        return opcion        