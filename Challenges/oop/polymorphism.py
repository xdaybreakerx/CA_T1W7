class Plants():
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height 

class GreenPlants(Plants):
    def __init__(self, name, height, colour) -> None:
        super().__init__(name, height)
        self.colour = colour

class LandPlants(GreenPlants):
    def __init__(self, name, height, colour) -> None:
        super().__init__(name, height, colour)

class VascularPlants(LandPlants):
    def __init__(self, name, height, colour, rootLength) -> None:
        super().__init__(name, height, colour)
        self.rootLength = rootLength

class SeedPlants(VascularPlants):
    def __init__(self, name, height, colour, rootLength, pollinationMethod) -> None:
        super().__init__(name, height, colour, rootLength)
        self.pollinationMethod = pollinationMethod

class Gymnosperms(SeedPlants):
    def __init__(self, name, height, colour, rootLength, pollinationMethod, coneSize) -> None:
        super().__init__( name,height, colour, rootLength, pollinationMethod)
        self.coneSize = coneSize

class Angiosperms(SeedPlants):
    def __init__(self, name, height, colour, rootLength, pollinationMethod, flowerSize, petalCount, flowerColour) -> None:
        super().__init__(name, height, colour, rootLength, pollinationMethod)
        self.flowerSize = flowerSize
        self.petalCount = petalCount
        self.flowerColour = flowerColour

cactus = LandPlants("cactus", 300, "green")
corn = Angiosperms("corn", 20, "yellow", 20, "bird", 24, 5, "white")
lavender = GreenPlants("lavender", 100, "purple")
cedar = Gymnosperms("cedar", 20000, "pine green", 40, "bird", 30)

for plant in (cactus, corn, lavender, cedar):
    print(f"{plant.name} are {plant.colour} and {plant.height}cm tall")