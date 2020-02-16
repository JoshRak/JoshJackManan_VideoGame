import pygame
import itertools
# from interactiveObject import InteractiveObject
class Chest():
    def __init__(self, contents, contentAmount, chestType, x, y):
        self.contents = contents
        self.alreadyAccessed = False
        self.contentAmount = contentAmount
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
    
    def initStates(self):
        states = {
            "DEFAULT":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestOpened.png"), (384, 426)),
            "LEAVE":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestLeave.png"), (384, 426)),
            "EQUIP":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestEquip.png"), (384, 426)),
            "STORE":pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestStore.png"), (384, 426))
        }
        return states

    def open(self, screen):
        screen.blit(self.chestImage, (32,32))
        print(self.contents)
        screen.blit(pygame.transform.scale(pygame.image.load(self.contents.imagePath), (140, 155)), (155, 120))
        # if self.type == 'KEY':
        #     sceneManager.drawImage(self.toolChestImage, (0,0))
        # else:
        #     sceneManager.drawImage('DEFAULT TOOL CHST IMAGE', (0,0))
    
    def selectNext(self):
        self.selection = next(self.selections)
    
    def selectPrev(self):
        self.selection = next(self.selections)
        self.selection = next(self.selections)

    def selected(self, screen):
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
        else:
            player.keysCollection.append(self.contents)
    
    def update(self, screen):
        self.chestImage = self.states[self.selection]
        screen.blit(self.chestImage, (32,32))
        # print(self.contents)
        screen.blit(pygame.transform.scale(pygame.image.load(self.contents.imagePath), (140, 155)), (155, 120))