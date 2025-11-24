class Personaje:
    def __init__(self, tipo, nombre, equipo_especial, resistencia, poder,
                 oficio, poder_equipo, tipo_arma, dano_arma):

        self.tipo = tipo
        self.nombre = nombre
        self.equipo_especial = equipo_especial
        self.vidas = 3
        self.resistencia = resistencia
        self.poder = poder
        self.oficio = oficio
        self.poder_equipo = poder_equipo
        self.tipo_arma = tipo_arma
        self.dano_arma = dano_arma
        self.nivel_arma = self.clasificar_arma()

    # clasificación del arma
    def clasificar_arma(self):
        if 500 <= self.dano_arma <= 1500:
            return "Ordinario"
        elif 1200 <= self.dano_arma <= 5000:
            return "Raro"
        elif 5000 <= self.dano_arma <= 50000:
            return "Leyenda"
        elif 50000 <= self.dano_arma <= 500000:
            return "Legendario"
        elif self.dano_arma >= 500000:
            return "Divino"
        else:
            return "No válido"

    def mostrar_info(self):
        print("\n--- PERSONAJE ---")
        print("Tipo:", self.tipo)
        print("Nombre:", self.nombre)
        print("Equipo especial:", self.equipo_especial)
        print("Vidas:", self.vidas)
        print("Resistencia:", self.resistencia)
        print("Poder:", self.poder)
        print("Oficio:", self.oficio)
        print("Poder del equipo:", self.poder_equipo)
        print("Arma:", self.tipo_arma)
        print("Daño del arma:", self.dano_arma)
        print("Nivel del arma:", self.nivel_arma)
        print("-----------------\n")



kazuki = Personaje(
    tipo="Ronin",
    nombre="Kazuki",
    equipo_especial="Mascara Roja",
    resistencia=4000,
    poder=7000,
    oficio="Cazador",
    poder_equipo=1500,
    tipo_arma="Katana Kurogumo",
    dano_arma=5200
)

kazuki.mostrar_info()