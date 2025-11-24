class Vehiculo:
    def __init__(self,marca, modelo, año,velocidad_actual=0):
      self.marca = marca
      self.modelo = modelo
      self.año = año
      self.velocidad_actual = velocidad_actual

    def acelerar (self, cantidad):
       self.velocidad_actual = max(0,self.velocidad_actual + cantidad )
       print(f"la velocidad se esta incrementando: {self.velocidad_actual}")

    def frenar (self, cantidad):
       self.velocidad_actual = max(0, self.velocidad_actual - cantidad)
       print(f"{self.marca} {self.modelo} freno a {self.velocidad_actual}km/h ")
   
    def mostrar_info(self):
       print(f"marca:{self.marca}")
       print(f"modelo:{self.modelo}")
       print(f"año:{self.año}")
       print(f"velocidad actual:{self.velocidad_actual} km/h")


class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, num_depuertas, velocidad_actual=0):
       super().__init__(marca, modelo, año, velocidad_actual)
       self.num_depuertas = num_depuertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"el numero de puertas es {self.num_depuertas} ")
        print("")

class Moto(Vehiculo):
   def __init__(self, marca, modelo, año, cilindraje, velocidad_actual=0):
      super().__init__(marca, modelo, año, velocidad_actual)
      self.cilindraje = cilindraje

   def mostrar_info(self):
     super().mostrar_info()
     print(f"la potencia del cilindraje es {self.cilindraje} cc")
     print("")

class bicicleta(Vehiculo):
   def __init__(self, marca, modelo, año,tipo, velocidad_actual=0):
      super().__init__(marca, modelo, año, velocidad_actual)
      self.tipo = tipo 

   def mostrar_info(self):
     super().mostrar_info()
     print(f"el tipo de bicicleta es {self.tipo}")
     print("")



carro1 = Carro("Toyota", "supra", 2007, 2)
carro2 = Carro("Buggati", "Chiron", 2018, 2)

moto1 = Moto("Kawasaki", "H2R", 2022, 900)
moto2 = Moto("Suzuki", "Gixxer FI ABS", 2021, 150)

bici1 = bicicleta("GW", "Raven", 2023, "Urbana")
bici2 = bicicleta("Piraña", "FX2", 2024, "Urbana")


vehiculos = [carro1, carro2, moto1, moto2, bici1, bici2]


carro1.acelerar(20)
moto1.acelerar(15)
bici1.acelerar(5)

carro1.frenar(10)
moto1.frenar(5)
bici1.frenar(3)


print("INFORMACIÓN DE TODOS LOS VEHÍCULO")
for v in vehiculos:
    v.mostrar_info()
   
   


   

      
    
    


    
    
    
   
   


class moto (Vehiculo):
   def __init__(self, marca, modelo, año, velocidad_actual=0):
      super().__init__(marca, modelo, año, velocidad_actual)
       

    

    
    
