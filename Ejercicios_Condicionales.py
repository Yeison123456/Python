"""Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el
segundo que los reste y si no que los sume."""


num1=int(input("Digite la primer numero "))
num2=int(input("Digite la segundo numero "))

if num1==num2:
    mul=num1*num2
    print(f"La multiplicacion entre los dos numero es: {mul} ")
elif num1>num2:
    res=num1-num2
    print(f"La resta entre los dos numero es: {res} ")
elif num1<num2:
    sum=num1+num2
    print(f"La suma entre los dos numero es: {sum} ")


"""En una fábrica de computadoras se planea ofrecer a los clientes un descuento que
dependerá del número de computadoras que compre. Si las computadoras son menos
de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de
computadoras es mayor o igual a cinco, pero menos de diez se le otorga un 20% de
descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada
computadora es de $15,000"""


numC=int(input("¿Cuantas computadoras piensa comprar? "))
tol=numC*15000
if numC<5:
    des=int((90*tol)/100)
    print(f"Compraste {numC} computadores por lo cual te daremos un descuento del 10%, el total a pagar es de {des} ")
elif numC>=5 & numC<10 :
    des=int((80*tol)/100)
    print(f"Compraste {numC} computadores por lo cual te daremos un descuento del 20%, el total a pagar es de {des} ")
elif numC>=10:
    des=int((60*tol)/100)
    print(f"Compraste {numC} computadores por lo cual te daremos un descuento del 40%, el total a pagar es de {des} ")
   
   
"""En una llantera se ha establecido una promoción de las llantas marca “Ponchadas”,
dicha promoción consiste en lo siguiente:
 Si se compran menos de cinco llantas el precio es de $300 cada una,
 de $250 si se compran de cinco a 10 y
 de $200 si se compran más de 10.
 Obtener la cantidad de dinero que una persona tiene que pagar por cada una
de las llantas que compra y la que tiene que pagar por el total de la compra."""


numL=int(input("¿Cuantas llantas piensa comprar? "))
if numL<5:
    total=numL*300
    print(f"Tienes que pagar 300 por cada llanta, el total a pagar es de {total} ")
elif numL>=5 and numL<10 :
    total=numL*250
    print(f"Tienes que pagar 250 por cada llanta, el total a pagar es de {total} ")
elif numL>=10:
    total=numL*200
    print(f"Tienes que pagar 200 por cada llanta, el total a pagar es de {total} ")


"""En un juego de preguntas a las que se responde “Si” o “No” gana quien responda
correctamente las tres preguntas. Si se responde mal a cualquiera de ellas ya no se
pregunta la siguiente y termina el juego. Las preguntas son:

 ¿Colon descubrió América?
 ¿La independencia de México fue en el año 1810?
 ¿The Doors fue un grupo de rock americano?"""


numP=int(input("¿Colon descubrió América? 1.Si  2.No "))
if numP==1:
    numP2=int(input("¿La independencia de México fue en el año 1810? 1.Si  2.No "))
    if numP2==1:
            numP3=int(input("¿The Doors fue un grupo de rock americano? 1.Si  2.No "))
            if numP3==1:
                print(f"Ganaste :D ")
            else:
                print(f"Respondiste mal se termina el juego ")
    else:
        print(f"Respondiste mal se termina el juego ")
else :
    print(f"Respondiste mal se termina el juego ")
    
    
"""Leer tres números diferentes e imprimir el número mayor de los tres."""

num11=int(input("Digite la primer numero "))
num22=int(input("Digite la segundo numero "))
num33=int(input("Digite la tercero numero "))

if num11>num22 and num11>num33:
    print(f"El numero mayor es el primero ")
elif num22>num11 and num22>num33:
    print(f"El numero mayor es el segundo ")
elif num33>num11 and num33>num22:
    print(f"El numero mayor es el tercero ")
