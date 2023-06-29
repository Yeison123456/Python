
pasajeros = [
    ("Jaider", 12345, "Bogota"),
    ("Yeison", 123456, "Cali"),
    ("Camilo", 1234567, "Cali"),
    ("Marcela", 12345678, "Medellin")
]

ciudades = [
    ("Bogota", "Cundinamarca"),
    ("Medellin", "Valle"),
    ("Cali", "Antioquia")
]

def crear():
    for i in range(1):
        nombre=input("Nombre:")
        pasajeros[0].append(nombre)
        identificacion=int(input("Identificacion:"))
        pasajeros[1].append(identificacion)
        destino=int(input("Destino:"))
        pasajeros[2].append(destino)
    i+=1
    return pasajeros

def crearc():
    for i in range(1):
        ciudad1=input("ciudad:")
        ciudades[0].append(ciudad1)
        departamento=int(input("Departamento:"))
        ciudades[1].append(departamento)
    i+=1
    return ciudades

op=True
while op==True:
    print("1. Agregar pasajeros:")
    print("2. Agregar ciudades:")
    print("3. Buscar ciudad destino por la identificación:")
    print("4. Cantidad de pasajeros que viajan a una cuidad:")
    print("5. Buscar país destino mediante la identificación :")
    print("6. Cantidad de pasajeros que viajan a un pais:")
    print("7. Salir del programa:")
    opcion = int(input("Acción a ejecutar"))
    if opcion==1:
        print(crear())
    elif opcion==2:
        print(crearc())
    elif opcion==3:
        identificacion = int(input("Ingrese la identificación del pasajero: "))
        for pasajero in pasajeros:
            if pasajero[1] == identificacion:
                for destino in ciudades:
                    if pasajero[2] == destino[0]:
                        print("El pasajero viaja a:", destino[0])
                        break
                break
        else:
            print("No se encontró ningún pasajero con esa identificación.")
    elif opcion==4:
        ciudades = input("Ingrese el nombre de la ciudad: ")
        contador = 0
        for pasajero in pasajeros:
            if pasajero[2] == ciudades:
                contador += 1
        print("Cantidad de pasajeros que viajan a", ciudades, ":", contador)
    elif opcion==5:
        identificacion = int(input("Ingrese la identificación del pasajero: "))
        for pasajero in pasajeros:
            if pasajero[1] == identificacion:
                for destino in ciudades:
                    if pasajero[2] == destino[0]:
                        print("El pasajero viaja a:", destino[1])
                        break
                break
        else:
            print("No se encontró ningún pasajero con esa identificación.")
    elif opcion==6:
        pais = input("Ingrese el nombre del país: ")
        contador = 0
        for pasajero in pasajeros:
            for destino in ciudades:
                if pasajero[2] == destino[0] and destino[1] == pais:
                    contador += 1
                    break
        print("Cantidad de pasajeros que viajan a", pais, ":", contador)
    elif opcion == 7:
        op==False
        print("Se salio del programa exitosamente")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

"""Desarrollar un programa para jugar piedra, papel o tijera, donde trabaje funciones"""



import random
desicion=int(input("1.Piedra  2.Papel. 3.Tijera"))

def num():
    numero = random.randint(2, 4)
    print(numero)
    if desicion==1 & numero==2:
        return print("Ganaste :D")
    elif desicion==2 & numero==3:
        return print("Ganaste :D")
    elif desicion==3 & numero==4:
        return print("Ganaste :D")
    else:
        return print("Perdiste :(")
     

print(num())

"""Escribir una función que reciba un diccionario con las asignaturas y las notas de un
alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las
calificaciones correspondientes a las notas."""

diccionario={
    "Asignatura": [],
    "Notas": [],
}

diccionario2={
    "Asignatura": [],
    "Notas": [],
}

def notas():
    
    for i in range(3):
        Asig=input("Asignatura: ")
        nota=int(input("Nota: "))
        diccionario["Asignatura"].append(Asig)
        diccionario["Notas"].append(nota)
        # poner en mayusculas
        print(i)
        diccionario2["Asignatura"].append(diccionario["Asignatura"][i].upper())
        def curso(nota):
            if nota<=5:
                return 'Mal'
            elif nota<=7 & nota>=6:
                return 'Regular'
            elif nota<=9 & nota>=8:
                return 'Bueno'
            elif nota==10:
                return 'Muy bien'
            else:
                return 'Excelente'
        diccionario2["Notas"].append(curso(nota))
      
print(notas())
print(diccionario)
print(diccionario2)


