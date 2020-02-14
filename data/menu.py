import pygame
from PIL import Image, ImageOps

class Menu(object):
    def __init__(self, player):
        self.player = player
        self.maxItems = {'PART':'AMOUNT AS INT'}
        self.inventory = {}
        self.currentItem = None
        self.image = "ADD TEMPLATE IMAGE HERE"
        self.currentlyDisplayed = False

    def maxQuantity(item, itemQuantity):
        if self.inventory[item] + itemQuantity > self.maxItems[item]:
            itemQuantity = self.maxItems[item] - self.inventory[item]
        return itemQuantity

    def add_item(self, item, itemAmount):
        if len(self.inventory) == 9:
            print("You have too many items in your inventory")
        else:
            itemQuantity = maxQuantity(item, itemAmount)
            if itemQuantity != itemAmount:
                print("You tried to add {} items but can only add {}".format(itemAmount, itemQuantity))
            self.inventory[item] = self.inventory[item] + itemQuantity if self.contains(item) else itemQuantity

    def drop_item(self, item, itemAmount):
        if self.contains(item):
            if itemAmount > self.inventory[item]:
                print("You tried to delete {} items but can only delete {}".format(itemAmount, self.inventory[item]))
                del self.inventory[item]
            elif itemAmount == self.inventory[item]
                del self.inventory[item]
            else:
                self.inventory[item] -= itemAmount
        else:
            print("This item was not found")

    def contains(self, item):
        return item is not None and item in self.inventory

    def add_border(self, img, outputPath):
        outputImg = ImageOps.expand(img, border=10, fill="#0000ff").resize(img.size, Image.ANTIALIAS)
        outputImg.save(outputPath)

    def select_item(self, item):
        self.currentItem = item
        imgPath = item.imagePath
        selectedImgPath = "{0}_selected.png".format(imgPath[:imgPath.rfind(".")])
        try:
            Image.open(selectedImgPath)
        except FileNotFoundError:
            add_border(Image.open(imgPath), selectedImgPath)

    def render(self, screen):
        self.currentlyDisplayed = True
        screen.blit(self.image, (0,0))
        screen.blit(player.equipped['CPU'] if 'CPU' in player.equipped else 'DEFAULT IMAGE', ('(X,Y) CPU LOCATION'))
        screen.blit('HOTBAR IMAGE', ('SOME LOW POINT'))
        i = 0
        for item in self.inventory.keys():
            i += 1
            img = item.imagePath
            if item = self.currentItem:
                img = "{0}_selected.png".format(imgPath[:imgPath.rfind(".")])
                # screen.blit('./Assets/Sprites/{}'.format(item), ('HOTBAR X VAL' + i * 'IMAGE SIZE + 10', 'HOTBAR Y VAL'))
            screen.blit(img, ('HOTBAR X VAL' + i * 'IMAGE SIZE + 10', 'HOTBAR Y VAL'))
    
    def update(self, currentTime, events):


    def close(self, currentTime, events):
        self.currentlyDisplayed = False
        self.player.scene.render()