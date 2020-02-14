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
    imagePath : str

@dataclass_json
@dataclass
class Keyboard:
    name : str
    tier : int
    notes : str
    imagePath : str

@dataclass_json
@dataclass
class CPU:
    name : str
    tier : int
    notes : str
    imagePath : str

@dataclass_json
@dataclass
class GPU:
    name : str
    tier : int
    notes : str
    imagePath : str

@dataclass_json
@dataclass
class CoolingSystem:
    name : str
    tier : int
    notes : str
    imagePath : str

@dataclass_json
@dataclass
class Computer:
    name : str
    mouse : Mouse
    keyboard : Keyboard
    CPU : CPU
    RAM : int
    storage : int
    GPU : GPU
    coolingSystem : CoolingSystem
    maxRAM : int
    maxStorage : int
    display : str
    tier : int
    notes : str
    imagePath : str

mouseTier1 = Mouse(name = "IBM PS/2 Two Button Combo Classic", dpi = 200, tier = 1, notes="", imagePath="/Images/Sprites/Mice/imbmouse_sprite.png")
mouseTier2 = Mouse(name = "Logitech B100 corded mouse", dpi = 800, tier = 2, notes="", imagePath="/Images/Sprites/Mice/logitech_sprite.png")
mouseTier3 = Mouse(name = "Apple magic mouse", dpi = 1300, tier = 3, notes="", imagePath="/Images/Sprites/Mice/magicMouse_sprite.png")
mouseTier4 = Mouse(name = "Logitech G502 HERO", dpi = 16000, tier = 1, notes="", imagePath="/Images/Sprites/Mice/logitechHero_sprite.png")
mouseTier5 = Mouse(name = "Razer Lancehead Tournament Edition", dpi = 16000, tier = 5, notes="", imagePath="/Images/Sprites/Mice/razer_sprite.png")

keyboardTier0 = Keyboard(name = "Typewriter", tier = 0, notes = "", imagePath = "/Images/Sprites/Keyboards/typewriter_sprite.png")
keyboardTier1 = Keyboard(name = "HP Standard 104 Key", tier = 1, notes = "", imagePath = "/Images/Sprites/Keyboards/hp_sprite.png")
keyboardTier2 = Keyboard(name = "Dell 2GR91", tier = 2, notes = "", imagePath = "/Images/Sprites/Keyboards/")
keyboardTier3 = Keyboard(name = "Redragon K552", tier = 3, notes = "", imagePath = "/Images/Sprites/Keyboards/redDragon_sprite.png")
keyboardTier4 = Keyboard(name = "Ideazon MERC Stealth", tier = 4, notes = "", imagePath = "/Images/Sprites/Keyboards/ideazon_sprite.png")
keyboardTier5 = Keyboard(name = "SafeType Keyboard", tier = 5, notes = "", imagePath = "/Images/Sprites/Keyboards/safetype_sprite.png")

CPUTier1_1 = CPU(name="Pentium M 780", tier = 1, notes="", imagePath="/Images/Sprites/CPUs/pentiumM.png")
CPUTier1_2 = CPU(name="Pentium Dual-Core", tier = 1, notes="", imagePath="/Images/Sprites/CPUs/pentiumDualCore.png")
CPUTier2_1 = CPU(name="AMD Athlon II", tier = 2, notes="", imagePath="/Images/Sprites/CPUs/amdAthlon2_sprite.png")
CPUTier2_2 = CPU(name="Intel Core i3", tier = 2, notes="", imagePath="/Images/Sprites/CPUs/i3_sprite.png")
CPUTier3_1 = CPU(name="Intel Core i5", tier = 3, notes="", imagePath="/Images/Sprites/CPUs/i5_sprite.png")
CPUTier3_2 = CPU(name="AMD Ryzen 5", tier = 3, notes="", imagePath="/Images/Sprites/CPUs/ryzen5_sprite.png")
CPUTier4_1 = CPU(name="Intel Core i7", tier = 4, notes="", imagePath="/Images/Sprites/CPUs/i7_sprite.png")
CPUTier4_2 = CPU(name="AMD Ryzen 7", tier = 4, notes="", imagePath="/Images/Sprites/CPUs/ryzen7_sprite.png")
CPUTier5_1 = CPU(name="AMD Ryzen 9", tier = 5, notes="", imagePath="/Images/Sprites/CPUs/ryzen9_sprite.png")
CPUTier5_2 = CPU(name="Intel Core i9", tier = 5, notes="", imagePath="/Images/Sprites/CPUs/i9_sprite.png")

GPUTier1 = GPU(name = "Radeon HD 2400", tier = 1, notes = "", imagePath = "/Images/Sprites/GPUs/radeon2400_sprite.png")
GPUTier2 = GPU(name = "Radeon RX Vega", tier = 2, notes = "", imagePath = "/Images/Sprites/GPUs/radionvega_sprite.png")
GPUTier3 = GPU(name = "NVIDIA GTX 1080", tier = 3, notes = "", imagePath = "/Images/Sprites/GPUs/NVIDIA1080_sprite.png")
GPUTier4 = GPU(name = "AMD RX 5700", tier = 4, notes = "", imagePath = "/Images/Sprites/GPUs/amd5700_sprite.png")
GPUTier5 = GPU(name = "NVIDIA Tesla V100", tier = 5, notes = "", imagePath = "/Images/Sprites/GPUs/NVIDIAtesla_sprite.png")

coolingSystemTier1 = CoolingSystem(name="Minka Aire Retro", tier = 1, notes="", imagePath = "/Images/Sprites/Cooling_Systems/minka_sprite.png")
coolingSystemTier2 = CoolingSystem(name="Dayton External Cooling Fan Blade", tier = 2, notes="", imagePath = "/Images/Sprites/Cooling_Systems/dayton_sprite.png")
coolingSystemTier4 = CoolingSystem(name="Polar Tech Dry Ice Transport Cooler", tier = 4, notes="", imagePath = "/Images/Sprites/Cooling_Systems/dryice_sprite.png")
coolingSystemTier5 = CoolingSystem(name="Cooler Master Silver Edition", tier = 5, notes="Comes with LEDs", imagePath = "/Images/Sprites/Cooling_Systems/coolermaster_sprite.png")

computerTier0 = Computer(name = 'Potato', mouse = None, keyboard = None, CPU = None, RAM = 0, storage = 0, GPU = None, coolingSystem = None,
                    operatingSystem = None, maxRAM = 0, maxStorage = 0, display = None, tier = 0, notes = "", imagePath = "/Images/Sprites/Computers/potato_sprite.png")

computerTier1 = Computer(name = 'Vintage IBM Thinkpad R52', mouse = None, keyboard = None,
                    CPU = CPU(name = 'Intel Pentium M 740', tier = 0, notes = "", imagePath = ""), RAM = .512, storage = 40,
                    GPU = GPU(name = 'Intel GMA 900', tier = 0, notes = "", imagePath = ""), coolingSystem = None,
                    maxRAM = 0, maxStorage = 0, display = "720 x 480", tier = 1, notes = "", imagePath = "/Images/Sprites/Computers/ibm_sprite.png")

computerTier2 = Computer(name = 'Dell Latitude E6400', mouse = None, keyboard = None,
                    CPU = CPUTier2_2, RAM = 2, storage = 320,
                    GPU = None, coolingSystem = None,
                    maxRAM = 4, maxStorage = 512, display = "1280 x 800", tier = 2, notes = "", imagePath = "/Images/Sprites/Computers/latitude_sprite.png")

computerTier3 = Computer(name = 'Lenovo Flex', mouse = None, keyboard = None,
                    CPU = CPUTier3_1, RAM = 8, storage = 512,
                    GPU = GPU(name = "Nvidia GeForce MX230", tier = 2, notes = "", imagePath = ""),
                    coolingSystem = CoolingSystem(name = "Internal Fans", tier = 2, notes = "", imagePath = ""),
                    maxRAM = 16, maxStorage = 1536, display = "1920 x 1080", tier = 3, notes = "", imagePath = "/Images/Sprites/Computers/lenovo_sprite.png")
                    
computerTier4 = Computer(name = 'Acer Predator Helios 300', mouse = None, keyboard = None, CPU = CPUTier4_1, RAM = 16, storage = 256, 
                    GPU = GPU(name="NVIDIA GeForce GTX 1060", tier=3, notes="", imagePath=""), 
                    coolingSystem = CoolingSystem(name="Internal Fans", tier=3, notes="", imagePath=""),
                    maxRAM = 64, maxStorage = 1024, display = "1920 x 1080", tier = 4, notes = "", imagePath = "/Images/Sprites/Computers/predator_sprite.png")
                    
computerTier5 = Computer(name = 'ROG Mothership GZ700 Gaming Laptop', mouse = Mouse(name="Glaudius II Gaming Mouse", tier = 4, notes="", imagePath=""), 
                    keyboard = None, CPU = CPUTier5_2, RAM = 64, storage = 1536, GPU = GPU(name="NVIDIA GeForce RTX 2080", tier=4, notes="", imagePath=""), 
                    coolingSystem = CoolingSystem(name="Internal Fans", tier=3, notes="", imagePath=""),
                    maxRAM = 256, maxStorage = 4096 display = "1920 x 1080", tier = 5, notes = "", imagePath = "/Images/Sprites/Computers/")