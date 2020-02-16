from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json

from setup import Computer

bob = Computer(name = 'Potato', mouse = None, keyboard = None,
                    CPU = None, RAM = 0, storage = 0,
                    GPU = None, coolingSystem = None,
                    maxRAM = 0, maxStorage = 0, display = None, tier = 0, notes = "", imagePath = "./Assets/Images/Sprites/Computers/potato_sprite.png")

print(bob.imagePath)