import writeraw
import colour
import naming


class MaterialInorganic:
    def __init__(self):
        self.name = naming.metalname()
        self.colour = colour.randomcolour()

    def write(self, raw):
        raw.writetoken("INORGANIC", self.name.upper())
        raw.writetoken("USE_MATERIAL_TEMPLATE", "METAL_TEMPLATE")
        # Name
        raw.writetoken("STATE_NAME_ADJ:ALL_SOLID", self.name.lower())
        raw.writetoken("STATE_NAME_ADJ:LIQUID", "molten " + self.name.lower())
        raw.writetoken("STATE_NAME_ADJ:GAS", "boiling " + self.name.lower())
        # Set appropriate recipes
        raw.writetoken("ITEMS_METAL")
        raw.writetoken("ITEMS_WEAPON")
        raw.writetoken("ITEMS_WEAPON_RANGED")
        raw.writetoken("ITEMS_AMMO")
        raw.writetoken("ITEMS_DIGGER")
        raw.writetoken("ITEMS_ARMOR")
        raw.writetoken("ITEMS_ANVIL")
        raw.writetoken("ITEMS_HARD")
        raw.writetoken("ITEMS_BARRED")
        raw.writetoken("ITEMS_SCALED")
        # Colour
        raw.writetoken("STATE_COLOR:ALL_SOLID", self.colour)


class InorganicRaw:
    def __init__(self):
        self.raw = writeraw.DFRaw("modgen/objects/", "inorganic_metal_gen", "INORGANIC")
        self.materials = []

    def addmaterial(self):
        newmat = MaterialInorganic()
        self.materials.append(newmat)

    def write(self):
        for m in self.materials:
            m.write(self.raw)
            self.raw.newline()
        self.raw.finishraw()
