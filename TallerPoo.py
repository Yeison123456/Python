class Motocicleta:

    estadoMotocicleta="Nueva"
    motor=False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas,
                marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        print("Iniciando el constructor")
        self.color=color
        self.matricula=matricula
        self.combustible_litros=combustible_litros
        self.numero_ruedas=numero_ruedas
        self.marca=marca
        self.modelo=modelo
        self.fecha_fabricacion=fecha_fabricacion
        self.velocidad_punta=velocidad_punta
        self.peso=peso


    def arrancar(self,motor):
        if motor==False:
            print(f"El motor ha sido arrancado , {motor}")
            motor=True
        else:
            print(f"El motor ya estaba en marcha esta en {motor}")

    def detener(self,motor):
        if motor==True:
            print("El motor ha sido detenido")
            motor=False
        else:
            print("El motor ya estaba detenido")

    def concultaPrecio(self):
        print(f"El precio de la pimera motocicleta {moto.marca} modelo {moto.modelo} es de {moto.precio} ")

    
moto= Motocicleta("Negro","123edfr",10,2,"Benelli",2020,20-8-2020,"50km/h","50kl")

moto2= Motocicleta(peso="50Kl",velocidad_punta="30km/h",fecha_fabricacion=20-10-2020,modelo=2021,marca="Ninja",numero_ruedas=2,combustible_litros=0,matricula="dsa213",color="Azul")

moto2.arrancar(False)
moto2.detener(True)

moto.precio=27000
print(f"El precio de la pimera motocicleta {moto.marca} modelo {moto.modelo} es de {moto.precio} ")

moto.concultaPrecio()
moto2.concultaPrecio()










