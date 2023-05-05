"""Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a
la semana. Su política de pagos es que un vendedor recibe un sueldo base y un 10% extra
por comisiones de sus ventas. El gerente de su compañía desea saber cuánto dinero
obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas
realizadas, y cuánto gana tomando en cuenta su sueldo base y sus comisiones."""

sb=500000


for n in range(3):
    nv=0
    while nv<=3:
        nv+=1
        v1=int(input("primera venta "))
        v2=int(input("primera venta "))
        v3=int(input("primera venta "))
        com=int((v1+v2+v3)*0.1)
        print(f"El empleado {n} tiene un sueldo base de {sb} mas las comisiones que son {com}, su suelto total es {sb+com}")
    n+=1
    
"""En una tienda de descuento las personas que van a pagar el importe de su compra llegan a
la caja y sacan una bolita de color, que les dirá que descuento tendrán sobre el total de su
compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta
que cierra.
 Se sabe que, si el color de la bolita es rojo, el cliente obtendrá un 40% de
descuento; si es amarilla un 25% y si es blanca no obtendrá descuento."""


for c in range(4):
    com=int(input("De cuanto fue la compra? "))
    el=int(input("Escoja un numero entre el 1, 2 o 3 "))
    if el==1:
        de=int(com*0.4)
        to=int(com*0.6)
        print(f"Sacaste la bolita roja obtienes un descuento del 40% ({de} respecto al total de la compra) por lo cual tendras que paga {to}")
    elif el==2:
        de=int(com*0.25)
        to=int(com*0.75)
        print(f"Sacaste la bolita amarilla obtienes un descuento del 25% ({de} respecto al total de la compra) por lo cual tendras que paga {to}")
    elif el==3:
        print(f"Sacaste la bolita blanca obtienes un descuento del 0%, por lo cual tendras que paga {com}")
    c+=1
    
"""El profesor de una materia desea conocer la cantidad de sus alumnos que no tienen
derecho al examen de nivelación.
Diseñe un algoritmo que lea las calificaciones obtenidas en las 5 materias por cada uno de
los 40 alumnos y escriba la cantidad de ellos que no tienen derecho al examen de
nivelación."""

td=0
nd=0
for n in range(3):
    n+=1
    n1=int(input("primera nota de 0 a 100 "))
    n2=int(input("segunda nota  de 0 a 100 "))
    n3=int(input("tercera nota de 0 a 100 "))
    n4=int(input("cuarta nota  de 0 a 100 "))
    n5=int(input("quinta nota de 0 a 100 "))
    pro=int((n1+n2+n3+n4+n5)/5)
    print(f"El estudiante {n} tiene estas notas:{n1},{n2},{n3},{n4},{n5} y su promedio fue {pro} ")
    if pro>=70:
        nd+=1
    elif pro<70:
        td+=1        
    
print(f"El numero de estudiantes que tienen derecho son: {td} y el numero de estudiantes que no tienen derecho son: {nd} ")

"""Diseñe un diagrama que lea los 2,500,000 votos otorgados a los 3 candidatos a
gobernador e imprima el número del candidato ganador y su cantidad de votos."""


y=0
d=0
j=0

for n in range(10):
    e=int(input("Por quien vas a votar? 1.Yeison  2.David  3.Jaider "))
    if e==1: 
        y+=1
    elif e==2:
        d+=1
    elif e==3:
        j+=1
    print("Su voto se guardo correctamente")

if y>d and y>j:
    print(f"Gano el candidato Yeison con {y} votos")
elif d>y and d>j:
    print(f"Gano el candidato David con {d} votos")
elif j>y and j>d:
    print(f"Gano el candidato Jaider con {j} votos")

"""Un grupo de 100 estudiantes presentan un examen de Física. Diseñe un diagrama que lea
por cada estudiante la calificación obtenida y calcule e imprima:
 La cantidad de estudiantes que obtuvieron una calificación menor a 50 en el área
del Tecnólogo en Análisis y Desarrollo de Sistemas de Información.
 La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero
menor que 70.
 La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero
menor que 80.
 La cantidad de estudiantes que obtuvieron una calificación de 80 o más."""

n1=0
n2=0
n3=0
n4=0


for e in range(10):
    n=int(input("Cual fue tu calificacion en el examen de fisica? "))
    if n<50: 
        n1+=1
    elif n>=50 and n<70:
        n2+=1
    elif n>=70 and n<80:
        n3+=1
    elif n>=80:
        n4+=1

print(f"{n1} estudiante obtuvieron una calificación menor a 50")
print(f"{n2} estudiante obtuvieron una calificación entre 50 y 69.")
print(f"{n3} estudiante obtuvieron una calificación entre 70 y 79")
print(f"{n4} estudiante obtuvieron una calificación mayor a 80")