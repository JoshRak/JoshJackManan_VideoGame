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
    delay : float

@dataclass_json
@dataclass
class Keyboard:
    name : str
    tier : int
    notes : str
    imagePath : str
    delay : float

@dataclass_json
@dataclass
class CPU:
    name : str
    tier : int
    notes : str
    imagePath : str
    delay : float

@dataclass_json
@dataclass
class GPU:
    name : str
    tier : int
    notes : str
    imagePath : str
    delay : float

@dataclass_json
@dataclass
class CoolingSystem:
    name : str
    tier : int
    notes : str
    imagePath : str
    delay : float

@dataclass_json
@dataclass
class Computer:
    name : str
    mouse : Mouse
    keyboard : Keyboard
    cpu : CPU
    ram : int
    storage : int
    gpu : GPU
    coolingsystem : CoolingSystem
    
    maxram : int
    maxstorage : int
    display : str
    tier : int
    notes : str
    imagePath : str
    delay : float

mouseTier1 = Mouse(name = "IBM PS/2 Two Button Combo Classic", dpi = 200, tier = 1, notes="", imagePath="./Assets/Images/Sprites/Mice/ibmmouse_sprite.png", delay = 0.24)
mouseTier2 = Mouse(name = "Logitech B100 corded mouse", dpi = 800, tier = 2, notes="", imagePath="./Assets/Images/Sprites/Mice/logitech_sprite.jpeg", delay = 0.2)
mouseTier3 = Mouse(name = "Apple magic mouse", dpi = 1300, tier = 3, notes="", imagePath="./Assets/Images/Sprites/Mice/magicMouse_sprite.png" , delay = 0.1)
mouseTier4 = Mouse(name = "Logitech G502 HERO", dpi = 16000, tier = 1, notes="", imagePath="./Assets/Images/Sprites/Mice/logitechHero_sprite.png", delay = 0.05)
mouseTier5 = Mouse(name = "Razer Lancehead Tournament Edition", dpi = 16000, tier = 5, notes="", imagePath="./Assets/Images/Sprites/Mice/razer_sprite.png", delay = 0)

keyboardTier0 = Keyboard(name = "Typewriter", tier = 0, notes = "", imagePath = "./Assets/Images/Sprites/Keyboards/typewriter_sprite.png", delay = 1)
keyboardTier1 = Keyboard(name = "HP Standard 104 Key", tier = 1, notes = "", imagePath = "./Assets/Images/Sprites/Keyboards/hp_sprite.png", delay = 0.2)
keyboardTier2 = Keyboard(name = "Dell 2GR91", tier = 2, notes = "", imagePath = "./Assets/Images/Sprites/Keyboards/", delay = 0.15)
keyboardTier3 = Keyboard(name = "Redragon K552", tier = 3, notes = "", imagePath = "./Assets/Images/Sprites/Keyboards/redDragon_sprite.png", delay = 0.1)
keyboardTier4 = Keyboard(name = "Ideazon MERC Stealth", tier = 4, notes = "", imagePath = "./Assets/Images/Sprites/Keyboards/ideazon_sprite.png", delay = 0.05)
keyboardTier5 = Keyboard(name = "SafeType Keyboard", tier = 5, notes = "", imagePath = "./Assets/Images/Sprites/Keyboards/safetype_sprite.png", delay = 0)

CPUTier1_1 = CPU(name="Pentium M 780", tier = 1, notes="", imagePath="./Assets/Images/Sprites/CPUs/pentiumM.png", delay = 0.45)
CPUTier1_2 = CPU(name="Pentium Dual-Core", tier = 1, notes="", imagePath="./Assets/Images/Sprites/CPUs/pentiumDualCore.png", delay = 0.4)
CPUTier2_1 = CPU(name="AMD Athlon II", tier = 2, notes="", imagePath="./Assets/Images/Sprites/CPUs/amdAthlon2_sprite.png", delay = 0.35)
CPUTier2_2 = CPU(name="Intel Core i3", tier = 2, notes="", imagePath="./Assets/Images/Sprites/CPUs/i3_sprite.png", delay = 0.3)
CPUTier3_1 = CPU(name="Intel Core i5", tier = 3, notes="", imagePath="./Assets/Images/Sprites/CPUs/i5_sprite.png", delay = 0.25)
CPUTier3_2 = CPU(name="AMD Ryzen 5", tier = 3, notes="", imagePath="./Assets/Images/Sprites/CPUs/ryzen5_sprite.png", delay = 0.2)
CPUTier4_1 = CPU(name="Intel Core i7", tier = 4, notes="", imagePath="./Assets/Images/Sprites/CPUs/i7_sprite.png", delay = 0.15)
CPUTier4_2 = CPU(name="AMD Ryzen 7", tier = 4, notes="", imagePath="./Assets/Images/Sprites/CPUs/ryzen7_sprite.png", delay = 0.1)
CPUTier5_1 = CPU(name="AMD Ryzen 9", tier = 5, notes="", imagePath="./Assets/Images/Sprites/CPUs/ryzen9_sprite.png", delay = 0.05)
CPUTier5_2 = CPU(name="Intel Core i9", tier = 5, notes="", imagePath="./Assets/Images/Sprites/CPUs/i9_sprite.png", delay = 0)

GPUTier1 = GPU(name = "Radeon HD 2400", tier = 1, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/radeon2400_sprite.png", delay = 0.2)
GPUTier2 = GPU(name = "Radeon RX Vega", tier = 2, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/radionvega_sprite.png", delay = 0.15)
GPUTier3 = GPU(name = "NVIDIA GTX 1080", tier = 3, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/NVIDIA1080_sprite.png", delay = 0.1)
GPUTier4 = GPU(name = "AMD RX 5700", tier = 4, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/amd5700_sprite.png", delay = 0.05)
GPUTier5 = GPU(name = "NVIDIA Tesla V100", tier = 5, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/NVIDIAtesla_sprite.png", delay = 0)

coolingSystemTier1 = CoolingSystem(name="Minka Aire Retro", tier = 1, notes="", imagePath = "./Assets/Images/Sprites/Cooling_Systems/minka_sprite.png", delay = 0.2)
coolingSystemTier2 = CoolingSystem(name="Dayton External Cooling Fan Blade", tier = 2, notes="", imagePath = "./Assets/Images/Sprites/Cooling_Systems/dayton_sprite.png", delay = 0.15)
coolingSystemTier4 = CoolingSystem(name="Polar Tech Dry Ice Transport Cooler", tier = 4, notes="", imagePath = "./Assets/Images/Sprites/Cooling_Systems/dryice_sprite.png", delay = 0.05)
coolingSystemTier5 = CoolingSystem(name="Cooler Master Silver Edition", tier = 5, notes="Comes with LEDs", imagePath = "./Assets/Images/Sprites/Cooling_Systems/coolermaster_sprite.png", delay = 0)

computerTier0 = Computer(name = 'Potato', mouse = None, keyboard = None,
                    cpu = None, ram = 0, storage = 0,
                    gpu = None, coolingsystem = None,
                    maxram = 0, maxstorage = 0, display = None, tier = 0, notes = "", imagePath = "./Assets/Images/Sprites/Computers/potato_sprite.png", delay = 1)

computerTier1 = Computer(name = 'Vintage IBM Thinkpad R52', mouse = None, keyboard = None,
                    cpu = CPU(name = 'Intel Pentium M 740', tier = 0, notes = "", imagePath = "./Assets/Images/Sprites/CPUs/intelPentiumM740.jpg", delay = 0.4), ram = .512, storage = 40,
                    gpu = GPU(name = 'Intel GMA 900', tier = 0, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/IntelGMA900.jpeg", delay = 0.25), coolingsystem = None,
                    maxram = 0, maxstorage = 0, display = "720 x 480", tier = 1, notes = "", imagePath = "./Assets/Images/Sprites/Computers/ibm_sprite.png", delay = 0.25)

computerTier2 = Computer(name = 'Dell Latitude E6400', mouse = None, keyboard = None,
                    cpu = CPUTier2_2, ram = 2, storage = 320,
                    gpu = None, coolingsystem = None,
                    maxram = 4, maxstorage = 512, display = "1280 x 800", tier = 2, notes = "", imagePath = "./Assets/Images/Sprites/Computers/latitude_sprite.png", delay = 0.2)

computerTier3 = Computer(name = 'Lenovo Flex', mouse = None, keyboard = None,
                    cpu = CPUTier3_1, ram = 8, storage = 512,
                    gpu = GPU(name = "Nvidia GeForce MX230", tier = 2, notes = "", imagePath = "./Assets/Images/Sprites/GPUs/mx230.jpeg", delay = 0.15),
                    coolingsystem = CoolingSystem(name = "Internal Fans", tier = 2, notes = "", imagePath = "./Assets/Images/Sprites/Cooling_Systems/internalFans.jpeg", delay = 0.2),
                    maxram = 16, maxstorage = 1536, display = "1920 x 1080", tier = 3, notes = "", imagePath = "./Assets/Images/Sprites/Computers/lenovo_sprite.png", delay = 0.1)
                    
computerTier4 = Computer(name = 'Acer Predator Helios 300', mouse = None, keyboard = None, cpu = CPUTier4_1, ram = 16, storage = 256, 
                    gpu = GPU(name="NVIDIA GeForce GTX 1060", tier=3, notes="", imagePath="./Assets/Images/Sprites/GPUs/gtx1060.jpeg", delay = 0.09), 
                    coolingsystem = CoolingSystem(name="Internal Fans", tier=3, notes="", imagePath="./Assets/Images/Sprites/Cooling_Systems/internalFans.jpeg", delay = 0.1),
                    maxram = 64, maxstorage = 1024, display = "1920 x 1080", tier = 4, notes = "", imagePath = "./Assets/Images/Sprites/Computers/predator_sprite.png", delay = 0.05)
                    
computerTier5 = Computer(name = 'ROG Mothership GZ700 Gaming Laptop', mouse = Mouse(name="Glaudius II Gaming Mouse", dpi = 16000, tier = 4, notes="", imagePath="./Assets/Images/Sprites/Mice/glaudius2.jpeg", delay = 0.02), 
                    keyboard = None, cpu = CPUTier5_2, ram = 64, storage = 1536, gpu = GPU(name="NVIDIA GeForce RTX 2080", tier=4, notes="", imagePath="./Assets/Images/Sprites/GPUs/rtx2080.jpeg", delay = 0.05), 
                    coolingsystem = CoolingSystem(name="Internal Fans", tier=3, notes="", imagePath="./Assets/Images/Sprites/Cooling_Systems/internalFans.jpeg", delay = 0),
                    maxram = 256, maxstorage = 4096, display = "1920 x 1080", tier = 5, notes = "", imagePath = "./Assets/Images/Sprites/Computers/", delay = 0)