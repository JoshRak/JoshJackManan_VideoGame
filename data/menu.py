import pygame
from PIL import Image, ImageOps
import itertools

class Menu(object):
    def __init__(self, player):
        self.player = player
        self.maxItems = {'PART':'AMOUNT AS INT'}
        self.inventory = []
        self.selections = None
        self.currentItem = None
        self.image = pygame.image.load("./Assets/Images/Inventory.png")
        self.currentlyDisplayed = False
        
    
    def __str__(self):
        return str(self.inventory)
        # for i,j in self.inventory:
        #     print(i,j)

    # def maxQuantity(self, item, itemQuantity):
    #     return 1
    #     # if self.inventory[item.name] + itemQuantity > self.maxItems[item.name]:
    #     #     itemQuantity = self.maxItems[item.name] - self.inventory[item.name]
        # return itemQuantity

    # def initSelections(self):
    #     if self.inventory:
    #         itertools.cycle(self.inventory)

    def add_item(self, item, itemAmount):
        if len(self.inventory) == 5:
            raise ValueError("You are holding too many items!")
            return
        if item is None:
            return
            # itemQuantity = self.maxQuantity(item, itemAmount)
            # if itemQuantity < itemAmount:
            #     print("You tried to add {} items but can only add {}".format(itemAmount, itemQuantity))
        self.inventory.append(item)
            # self.inventory[item.name] = self.inventory[item.name] + itemQuantity if self.contains(item) else itemQuantity

    def drop_item(self, item, itemAmount):
        if self.contains(item):
            # if itemAmount > self.inventory[item.name]:
            #     print("You tried to delete {} items but can only delete {}".format(itemAmount, self.inventory[item.name]))
            #     del self.inventory[item]
            # elif itemAmount == self.inventory[item.name]:
            #     del self.inventory[item.name]
            # else:
            self.inventory.remove(item)
        else:
            print("This item was not found")

    def contains(self, item):
        return item is not None and item in self.inventory

    def select_next(self):
        self.currentItem = next(self.selections)
    
    def select_prev(self):
        for i in range(1, len(self.inventory)):
            self.currentItem = next(self.selections)

    def add_border(self, img, outputPath):
        outputImg = ImageOps.expand(img, border=10, fill="#0000ff").resize(img.size, Image.ANTIALIAS)
        outputImg.save(outputPath)

    def select_item(self, item):
        # self.currentItem = item
        imgPath = item.imagePath
        selectedImgPath = "{0}_selected.png".format(imgPath[:imgPath.rfind(".")])
        try:
            Image.open(selectedImgPath)
        except:
            self.add_border(Image.open(imgPath), selectedImgPath)

    def render(self, screen):
        self.currentlyDisplayed = True
        screen.blit(self.image, (0,0))
        if self.inventory:
            self.selections = itertools.cycle(self.inventory)
            self.currentItem = next(self.selections)
        if self.player.equipped:
            print("here")
            screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.imagePath), (177, 185)), (155, 131))
            if self.player.equipped.cpu:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.cpu.imagePath), (75, 84)), (348, 230))
            if self.player.equipped.mouse:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.mouse.imagePath), (75, 84)), (350, 35))
            if self.player.equipped.gpu:
                print(self.player.equipped.gpu)
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.gpu.imagePath), (100, 90)), (50, 131))
            if self.player.equipped.coolingsystem:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.coolingsystem.imagePath),(77, 90)), (348, 131))
            if self.player.equipped.keyboard:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.keyboard.imagePath), (120,90)), (20, 225))
        # screen.blit('HOTBAR IMAGE', ('SOME LOW POINT'))
        i = -1
        print(self.inventory)
        for item in self.inventory:
            i += 1
            img = item.imagePath
            if item == self.currentItem:
                self.select_item(item)
                img = "{0}_selected.png".format(img[:img.rfind(".")])
                # screean.blit('./Assets/Sprites/{}'.format(item), ('HOTBAR X VAL' + i * 'IMAGE SIZE + 10', 'HOTBAR Y VAL'))
            screen.blit(pygame.transform.scale(pygame.image.load(img), (87, 96)), (1 + i * 90, 367))
    
    def update(self, screen):
        self.currentlyDisplayed = True
        screen.blit(self.image, (0,0))
        # if self.inventory:
        #     self.selections = itertools.cycle(self.inventory)
        #     self.currentItem = next(self.selections)
        if self.player.equipped:
            print("here")
            screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.imagePath), (177, 185)), (155, 131))
            if self.player.equipped.cpu:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.cpu.imagePath), (75, 84)), (348, 230))
            if self.player.equipped.mouse:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.mouse.imagePath), (75, 84)), (350, 35))
            if self.player.equipped.gpu:
                print(self.player.equipped.gpu)
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.gpu.imagePath), (100, 90)), (50, 131))
            if self.player.equipped.coolingsystem:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.coolingsystem.imagePath),(77, 90)), (348, 131))
            if self.player.equipped.keyboard:
                screen.blit(pygame.transform.scale(pygame.image.load(self.player.equipped.keyboard.imagePath), (120,90)), (20, 225))
        # screen.blit('HOTBAR IMAGE', ('SOME LOW POINT'))
        i = -1
        print(self.inventory)
        for item in self.inventory:
            i += 1
            img = item.imagePath
            if item == self.currentItem:
                self.select_item(item)
                img = "{0}_selected.png".format(img[:img.rfind(".")])
            screen.blit(pygame.transform.scale(pygame.image.load(img), (87, 96)), (1 + i * 90, 367))        

    def close(self, currentTime, events):
        self.currentlyDisplayed = False
        self.player.scene.render()