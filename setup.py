from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json

@dataclass_json
@dataclass
class Mouse: 
    name : str
    dpi : int
    tier : int
    notes : str

@dataclass_json
@dataclass
class Keyboard:
    name : str
    tier : int
    notes : str

@dataclass_json
@dataclass
class CPU:
    name : str
    tier : int
    notes : str

@dataclass_json
@dataclass
class GPU:
    name : str
    tier : int
    notes : str

@dataclass_json
@dataclass
class CoolingSystem:
    name : str
    tier : int
    notes : str

@dataclass_json
@dataclass
class OperatingSystem:
    name : str
    notes : str

@dataclass_json
@dataclass
class Computer:
    name : str
    mouse : Mouse
    #keyboard : Keyboard
    #CPU : CPU
    RAM : int
    storage : int
    #GPU : GPU
    #coolingSystem : CoolingSystem
    #operatingSystem : OperatingSystem
    maxRAM : int
    maxStorage : int
    display : str
    tier : int
    notes : str

testMouse = Mouse(name = "testMouse", dpi = 50, tier = 1, notes = "test")
testComputer = Computer(name = "banana", mouse = testMouse, RAM = 50, storage = 50, maxRAM = 50, maxStorage = 50, display = "banana", tier = 1, notes = "none")
print(json.dumps(testComputer.to_dict(), indent=4, separators=(",", "= ")))