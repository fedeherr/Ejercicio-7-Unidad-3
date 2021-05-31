from Apoyo import Apoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador

def crearAgente():
        op = 0
        aux = None
        while op == 0:
            op = int(input(" 1. Personal de apoyo \n 2. Docente \n 3. Investigador \n 4. Docente Invetigador \nIngrese opcion: "))
            if op == 1:
                cuil=int(input("Ingrese Cuil: "))
                apellido=input("Ingrese Apellido: ")
                nombre=input("Ingrese nombre: ")
                sb= int(input("Ingrese Basico: "))
                antiguedad=int(input("Ingrese antiguedad: "))
                cat=int(input("Ingrese categoria: "))
                aux = Apoyo(cuil, apellido, nombre,sb, antiguedad, cat)
            elif op == 2:
                cuil=int(input("Ingrese Cuil: "))
                apellido=input("Ingrese Apellido: ")
                nombre=input("Ingrese nombre: ")
                sb= int(input("Ingrese Basico: "))
                antiguedad=int(input("Ingrese antiguedad: "))
                carrera=input("Ingrese carrera: ")
                cargo = input("Ingrese cargo: ")
                cargo.lower()
                catedra = input("Ingrese catedra")
                aux = Docente(cuil, apellido, nombre, sb, antiguedad, carrera, cargo, catedra)
            elif op == 3:
                cuil=int(input("Ingrese Cuil: "))
                apellido=input("Ingrese Apellido: ")
                nombre=input("Ingrese nombre: ")
                sb= int(input("Ingrese Basico: "))
                antiguedad=int(input("Ingrese antiguedad: "))
                area=input("Ingrese area: ")
                tipo=input("Ingrese tipo: ")
                aux = Investigador(cuil, apellido, nombre,sb, antiguedad, 'x', 'x', 'x', area, tipo)
            elif op == 4:
                cuil=int(input("Ingrese Cuil: "))
                apellido=input("Ingrese Apellido: ")
                nombre=input("Ingrese nombre: ")
                sb= int(input("Ingrese Basico: "))
                antiguedad=int(input("Ingrese antiguedad: "))
                carrera=input("Ingrese Carrera: ")
                catedra=input("Ingrese Catedra: ")
                cargo=input("Ingrese Cargo: ")
                area= input("Ingrese area de Investigacion: ")
                tipoinv= input("Ingrese tipo de investigacion: ")
                catinc=(input("Ingrese categoria de incentivos: "))
                extra=int(input("Ingrese extra: "))
                aux = DocenteInvestigador(cuil, apellido, nombre, sb, antiguedad, carrera, cargo, catedra, area, tipoinv, catinc, extra)
            else:
                op = 0
        return aux