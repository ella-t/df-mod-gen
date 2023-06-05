import random

import writeraw
import colour
import naming


class MetalMaterial:
    def __init__(self):
        self.name = naming.metalname()
        self.colour = colour.randomcolour()
        self.acquisition = "ore"

    def write(self, raw):
        raw.writetoken("INORGANIC", self.name.upper().replace(" ", "_"))
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

class OreMaterial:
    def __init__(self, name = None):
        if name is None:
            self.name = naming.metalorename()
        else:
            if random.randint(1, 4) == 1:
                self.name = "native " + name
            else:
                self.name = naming.metalorename()
        self.colour = colour.randomcolour()
        self.ores = []
        self.env = []

    def setore(self, metalname, weighting):
        self.ores.append((metalname, weighting))

    def setenvironment(self):
        env_igneous = random.randint(1, 10)
        if env_igneous == 1:
            self.env.append("IGNEOUS_ALL")
        elif env_igneous == 2 or env_igneous == 3:
            self.env.append("IGNEOUS_INTRUSIVE")
        elif env_igneous == 4 or env_igneous == 5:
            self.env.append("IGNEOUS_EXTRUSIVE")
        env_soil = random.randint(1, 10)
        if env_soil == 1:
            self.env.append("SOIL")
        elif env_soil == 2 or env_soil == 3:
            self.env.append("SOIL_SAND")
        elif env_soil == 4 or env_soil == 5:
            self.env.append("IGNEOUS_EXTRUSIVE")
        env_meta = random.randint(1, 2)
        if env_meta == 1:
            self.env.append("METAMORPHIC")
        env_sediment = random.randint(1, 3)
        if env_sediment == 1:
            self.env.append("SEDIMENTARY")
        env_alluvial = random.randint(1, 4)
        if env_alluvial == 1:
            self.env.append("ALLUVIAL")
        if len(self.env) == 0:
            self.env.append("ALL_STONE")

    def write(self, raw):
        raw.writetoken("INORGANIC", self.name.upper().replace(" ", "_"))
        raw.writetoken("USE_MATERIAL_TEMPLATE", "STONE_TEMPLATE")
        # Name
        raw.writetoken("STATE_NAME_ADJ:ALL_SOLID", self.name.lower())
        # Colour
        raw.writetoken("STATE_COLOR:ALL_SOLID", self.colour)
        raw.writetoken("TILE", "156")
        # Gameplay
        raw.writetoken("IS_STONE")
        raw.writetoken("MATERIAL_VALUE", 8)
        for o in self.ores:
            raw.writetoken("METAL_ORE", o[0].upper().replace(" ", "_") + ":" + str(o[1]))
        for e in self.env:
            raw.writetoken("ENVIRONMENT", e + ":VEIN:100")


class InorganicRaw:
    def __init__(self):
        self.raw = writeraw.DFRaw("modgen/objects/", "inorganic_metal_gen", "INORGANIC")
        self.metals = []
        self.ores = []

    def addmaterial(self):
        newmat = MetalMaterial()
        self.metals.append(newmat)

    def addores(self):
        metalscount = 0
        for i in self.metals:
            if i.acquisition == "ore":
                metalscount += 1
        # Native ores
        for j in self.metals:
            if j.acquisition == "ore":
                newore = OreMaterial(j.name)
                newore.setore(j.name, 100)
                newore.setenvironment()
                self.ores.append(newore)
        # Extra ores
        extraores = random.randint(0, round(metalscount / 2))
        for o in range(extraores):
            newore = OreMaterial()
            neworemetals = random.randint(1, 4)
            neworechoices = random.choices(self.metals, k=neworemetals)
            for k in range (neworemetals):
                if k == 0:
                    orechance = 100
                else:
                    orechance = random.randint(1, 100)
                newore.setore(neworechoices[k].name, orechance)
            newore.setenvironment()
            self.ores.append(newore)

    def write(self):
        for m in self.metals:
            m.write(self.raw)
            self.raw.newline()
        for o in self.ores:
            o.write(self.raw)
            self.raw.newline()
        self.raw.finishraw()
