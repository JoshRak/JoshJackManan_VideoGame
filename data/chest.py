import pygame
from PIL import Image, ImageOps
import itertools
# from interactiveObject import InteractiveObject
class Chest():
    def __init__(self, name, contents, contentAmount, chestType, x, y): #initalize Chest with the name of the item, its contents and amounts, whether its computer or tool, and its x and y
        self.name = name
        self.contents = contents
        self.alreadyAccessed = False
        self.contentAmount = contentAmount
        self.starsImg = self.displayTier(self.contents.tier)
        self.type = chestType
        self.x = x
        self.y = y

        self.selections = itertools.cycle(["LEAVE", 'EQUIP', 'STORE'])
        self.selection = next(self.selections)
        self.states = self.initStates()

        if chestType == 'key':
            pass
        else:
            self.chestImage = self.states["DEFAULT"]
    
    def initStates(self): #intialize the screens for images of the tool chests
        states = {
            "DEFAULT":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestOpened.png"), (384, 426)),
            "LEAVE":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestLeave.png"), (384, 426)),
            "EQUIP":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestEquip.png"), (384, 426)),
            "STORE":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestStore.png"), (384, 426))
        }
        return states

    def displayTier(self, tier, gapWidth = 20): # display the star tiers under the image
        starImg = Image.open("./Assets/Images/transparentStar.png")
        scale = 0.1
        # starImg.show()
        img = Image.new('RGBA', ((starImg.size[0] * tier) + (gapWidth * (tier+1)), starImg.size[1] + (gapWidth * 2)), (127,0,127,0))
        for i in range(0, tier):
            img.paste(starImg, ((i * starImg.size[0]) + ((i + 1) * gapWidth), gapWidth), mask=starImg)
        
        img = img.resize((round(img.size[0] * scale), round(img.size[1] * scale)))
        
        path = "./Assets/Images/tier{}Stars.png".format(tier)
        img.save(path)
        return pygame.image.load(path).convert_alpha()

    def open(self, screen): # display the image of the items in the chest for the first time
        chestW, chestH = self.chestImage.get_rect().size
        starsW, starsH = self.starsImg.get_rect().size

        screen.blit(self.chestImage, (32,32))
        print(self.contents)
        screen.blit(pygame.transform.scale(pygame.image.load(self.contents.imagePath), (140, 163)), (155, 120))
        screen.blit(self.starsImg, (round((chestW - starsW) / 2) + 32, round((0.7 * chestH) - (starsH / 2)) + 32))
        
        #(round((chestW - starsW) / 2) + 999999, round((0.7 * chestH) - (starsH / 2)) + 32)

        # if self.type == 'KEY':
        #     sceneManager.drawImage(self.toolChestImage, (0,0))
        # else:
        #     sceneManager.drawImage('DEFAULT TOOL CHST IMAGE', (0,0))
    
    def selectNext(self): # the 'selected' option moves to the next one
        self.selection = next(self.selections)
    
    def selectPrev(self): # the 'selected' option moves to the left one
        self.selection = next(self.selections)
        self.selection = next(self.selections)

    
    def selected(self, screen): # do the specified action based on what the selected option is and what is possible
        player = self.scene.player
        if self.type == 'TOOL':
            if self.selection == 'LEAVE':
                self.alreadyAccessed = False
                player.isAccessingChest = False
            elif self.selection == 'EQUIP':
                try:
                    player.isAccessingChest = False
                    self.alreadyAccessed = True
                    player.equipPart(self.contents)
                except ValueError as Er:
                    print(Er)
                    if 'not' in str(Er):
                        self.alreadyAccessed = False
                        player.isAccessingChest = True
            else:
                try:
                    player.inventory.add_item(self.contents, 1)
                    self.alreadyAccessed = True
                    player.isAccessingChest = False
                except ValueError as Er:
                    print(Er)
                    self.alreadyAccessed = False
                    player.isAccessingChest = True
        if self.type == 'COMP':
            if self.selection == 'LEAVE':
                self.alreadyAccessed = False
                player.isAccessingChest = False
            elif self.selection == 'EQUIP':
                print("here1")
                try:
                    player.isAccessingChest = False
                    print("here2")
                    self.alreadyAccessed = True
                    print("here3")
                    player.equipComp(self.contents)
                    print("here4")
                except ValueError as Er:
                    print(Er)
                    if not ('or add' in str(Er)):
                        self.alreadyAccessed = False
                        player.isAccessingChest = True
            else:
                try:
                    player.inventory.add_item(self.contents, 1)
                    self.alreadyAccessed = True
                    self.player.chestDict[self.name] = True
                    player.isAccessingChest = False
                except ValueError as Er:
                    print(Er)
                    self.alreadyAccessed = False
                    player.isAccessingChest = True
    
    def update(self, screen): # display the chest image on the screen 
        self.chestImage = self.states[self.selection]
        chestW, chestH = self.chestImage.get_rect().size
        starsW, starsH = self.starsImg.get_rect().size

        screen.blit(self.chestImage, (32,32))
        print(self.contents)
        screen.blit(pygame.transform.scale(pygame.image.load(self.contents.imagePath), (140, 155)), (155, 120))
        screen.blit(self.starsImg, (round((chestW - starsW) / 2) + 32, round((0.7 * chestH) - (starsH / 2)) + 32))