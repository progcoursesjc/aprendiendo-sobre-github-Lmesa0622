class Evaluaciones:
    def __init__(self, nombre_materia, lista_preguntas, porcentaje):
        self.nombre_materia = nombre_materia
        self.lista_preguntas = lista_preguntas
        self.porcentaje = porcentaje

lista_Evaluaciones = []
lista_materias= ["1.algebra", 
                "2.sociales", 
                "3.programacion"]


def Mostrar ():
    l=0
    while l<len(lista_Evaluaciones):
        print(lista_Evaluaciones[l].nombre_materia,"- porcentaje", lista_Evaluaciones[l].porcentaje, "%")
        for r in lista_Evaluaciones[l].lista_preguntas:
            print("pregunta:",r)
        l+=1
def crear_evaluacion():
    nombre_materia=l
    porcentaje=int(input("Ingrese el porcentaje de la evaluación:"))
    numero_preguntas=int(input("Ingrese el numero de preguntas que tendrá la evaluación:"))
    print("Ingrese las preguntas de la evaluación:")
    lista_preguntas=[]
    for n in range(numero_preguntas):
        preguntas= str(input())
        lista_preguntas.append(preguntas)

    evaluaciones=Evaluaciones(nombre_materia , lista_preguntas, porcentaje)
    lista_Evaluaciones.append(evaluaciones)
        
    print("Evaluación guardada con exito:",)
    print("A continuacion el resultado:")
    Mostrar()

print("Lista de materias:")
for i in lista_materias:
    print(i)
curso=int(input("Seleccione la materia según su número:"))
if curso==1:
    l="algebra"
    crear_evaluacion()
elif curso==2:
    l="sociales"
    crear_evaluacion()
elif curso==3:
    l="programacion"
    crear_evaluacion()
else:
    while curso < 1 or curso > 5:
        print("Opcion invalida,por favor ingrese una materia valida")
        curso= int(input("Seleccione una materia:"))
        if curso==1:
            l="algebra"
            crear_evaluacion()
        elif curso==2:
            l="sociales"
            crear_evaluacion()
        elif curso==3:
            l="programación"
            crear_evaluacion()

