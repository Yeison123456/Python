"""Una persona desea iniciar un negocio, para lo cual piensa verificar cuánto dinero le
prestara el banco por hipotecar su casa. Tiene una cuenta bancaria, pero no quiere
disponer de ella a menos que el monto por hipotecar su casa sea muy pequeño.
a. Si el monto de la hipoteca es menor que $1.000.000, entonces invertirá el 50% de
la inversión total y un socio invertirá el otro 50%.
b. Si el monto de la hipoteca es de $ 1.000.000 o más, entonces invertirá el monto
total de la hipoteca y el resto del dinero que se necesite para cubrir la inversión
total se repartirá a partes iguales entre el socio y el."""

inv=int(input("Cuanto es la inversion de la casa"))
hip=int(input("Cuanto es la hipoteca de la casa"))

if hip<1000000:
    pa=int(inv*0.5)
    print(f"entonces invertirá el 50% ({pa}) de la inversión total y un socio invertirá el otro 50% ({pa}).")
elif hip>=1000000:
    to=int(inv-hip)
    to1=int(to*0.5)
    to2=int(hip+to1)
    print(f"entonces invertirá el monto de la hipoteca y mas la mitad de el resto del dinero ({to2}) y la otra mitad la cubrira el socio ({to1})")
    
"""El gobierno de Colombia, desea reforestar un bosque que mide determinado número de
hectáreas. Si la superficie del terreno excede a 1 millón de metros cuadrados, entonces
decidirá sembrar de la siguiente manera:"""

sup=int(input("Cuantas hectarias desean reforestar"))
supt=int(sup*10000)



if supt>1000000:
    pi=int(supt*0.7)
    oy=int(sup*0.2)
    ce=int(sup*0.1)
    print(f"Sombraran un 70% del terrero ({pi}) en arboles de tipo pinos, un 20% del tenerreno ({oy}) en  arboles de tipo oyamel y un 10% del terreno ({ce}) en arboles de tipo cedro ")
elif supt<=1000000:
    pi=int(supt*0.5)
    oy=int(sup*0.3)
    ce=int(sup*0.2)
    print(f"Sombraran un 50% del terrero ({pi}) en arboles de tipo pinos, un 30% del tenerreno ({oy}) en  arboles de tipo oyamel y un 20% del terreno ({ce}) en arboles de tipo cedro ")


"""Una persona debe realizar un muestreo con 50 personas para determinar el promedio de
peso de los niños, jóvenes, adultos y viejos que existen en su zona habitacional. Se
determinan las categorías con base en la siguiente tabla:"""

cn=1
cj=1
ca=1
cv=1
n=0
j=0
a=0
v=0
pn=0
pj=0
pa=0
pv=0

for p in range(10):
    e=int(input("Cuantos años tiene"))
    if e>=0 and e<=12:
        p=int(input("Cuanto pesa el niño?"))
        n=n+p
        cn+=1
    elif e>=13 and e<=29:
        p=int(input("Cuanto pesa el joven?"))
        j=j+p
        cj+=1
    elif e>=30 and  e<=59:
        p=int(input("Cuanto pesa el adulto?"))
        a=a+p
        ca+=1
    elif e>=60:
        p=int(input("Cuanto pesa el viejo?"))
        v=v+p
        cv+=1
pn=n/cn
pj=j/cj
pa=a/ca
pv=v/cv

print(f"El promedio del peso en niños es de: {pn}")
print(f"El promedio del peso en jovenes es de: {pj}")
print(f"El promedio del peso en adultos es de: {pa}")
print(f"El promedio del peso en viejos es de: {pv}")

"""En una empresa se requiere calcular el salario semanal de cada uno de los n obreros que
laboran en ella. El salario se obtiene de la sig. forma: Si el obrero trabaja 40 horas o menos
se le paga $20 por hora, Si trabaja más de 40 horas se le paga $20 por cada una de las
primeras 40 horas y $25 por cada hora extra."""


for n in range(3):
    ht=int(input("Cuantas horas trabaja? "))
    if ht<=40:
        to=ht*20
        print(f"Tu salario sera de {to}")
    if ht>40:
        to=int(40*20)
        ma=int((ht-40)*25)
        print(f"Tu salario dera de {to+ma}")
        
"""Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero
que el teatro deja de percibir por cada una de las categorías. Tomar en cuenta que los
niños menores de 5 años no pueden entrar al teatro y que existe un precio único en los
asientos. Los descuentos se hacen tomando en cuenta el siguiente cuadro:"""

a=5000
cd=0



for n in range(5):
    e=int(input("Cuantos años tiene"))
    if e>=5 and e<=14:
        des=a*0.35
        print(f"El descuento para la categoria 1 es: {des}")
        cd=cd+des
    elif e>=15 and e<=19:
        des=a*0.25
        print(f"El descuento para la categoria 2 es: {des}")
        cd=cd+des
    elif e>=20 and  e<=45:
        des=a*0.1
        print(f"El descuento para la categoria 3 es: {des}")
        cd=cd+des
    elif e>=46 and e<=65:
        des=a*0.25
        print(f"El descuento para la categoria 4 es: {des}")
        cd=cd+des
    elif e>=66:
        des=a*0.35
        print(f"El descuento para la categoria 1 es: {des}")
        cd=cd+des

print(f"La cantidad de dinero que el teatro dejo percibir por los descuentos es de {cd}")
