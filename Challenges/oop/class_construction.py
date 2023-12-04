class Pokemon():
    def __init__(self, name, pokedexNumber, type):
        self.name = name
        self.pokedexNumber = pokedexNumber
        self.type = type

pikachu = Pokemon("Pikachu", 25, "Electric")

print(pikachu.name)
print(pikachu.pokedexNumber)
print(pikachu.type)