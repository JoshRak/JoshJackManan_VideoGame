import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
import itertools
from pygame.locals import *
# import data.items as items
import data.chest as chest
from data.items import *
from data.dialogBox import DialogBox
import textboxify
import random

class Scene(object):
    def __init__(self, roomNum, sceneMap, entities):
        self.sceneMap = sceneMap
        self.roomNum = roomNum
        self.entities = entities
        for entity in entities.sprites():
            entity.scene = self
        self.player = entities.sprites()[0]
        # self.player.scene = self
        self.states = self.initStates()
        self.roomTypes = self.initRooms()
        self.state = "active"
        self.nextRoom = None
        self.chests = {}
        self.currentChest = None
        self.objects = self.initObjects()

        # build the room

    def initObjects(self):
        objectsDict = {
            "chests": self.chests
        }
        return objectsDict

    def initChest(self, obj):
        # chestsDict = {
        #     "CPC1" : chest.Chest(computerTier2, 1, 'COMP', obj.x, obj.y),
        #     "KC1" : chest.Chest(keyboardTier1, 1, 'TOOL', obj.x, obj.y),
        #     "Chest1" : chest.Chest(mouseTier2, 2, 'TOOL', obj.x, obj.y),
        #     "Chest2" : chest.Chest(GPUTier3, 3, 'TOOL', obj.x, obj.y)
        # }
        # return chestsDict[obj.name]
        itemType = ""
        if obj.name == "Room1_Chest1":
            item = computerTier1
        # elif obj.name == "Room1_Chest2":
        #     item = computerTier4
        elif obj.name == "Room7_Chest1":
            item = computerTier3
        elif obj.name == "Room2_Chest1":
            item = computerTier1
        else:
            item = getRandItem()
        
        if getItemClass(item) == "computer":
            itemType = "COMP"
        else:
            itemType = "TOOL"

        return chest.Chest(obj.name, item, 1, itemType, obj.x, obj.y)

    def initStates(self):
        statesDict = {
            "active":self.defaultState,
            "transitioning":self.transitionState,
            "chest":self.chestOpenedState
        }
        return statesDict

    def initRooms(self):
        rooms = {
            1:self.roomOne,
            2:self.roomTwo,
            3:self.roomThree,
            4:self.roomFour,
            5:self.roomFive,
            6:self.roomSix,
            7:self.roomSeven,
            8:self.roomEight,
            9:self.roomNine,
            10:self.roomTen,
            11:self.roomEleven,
            12:self.roomTwelve
        }
        return rooms

    def tutorialMovement(self, screen):
        info_text_1 = textboxify.Text(text="Press WASD to move", size = 30, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                        val = False

    def tutorialTerminal(self, screen):
        info_text_1 = textboxify.Text(text="Press T to open terminal.", size = 30, color=(255, 255, 255), background=(222,184,135))
        info_text_2 = textboxify.Text(text="Type in the flag if you find one!", size = 30, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        screen.blit(info_text_2.image, (40, 70))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        val = False

    def tutorialInventory(self, screen):
        info_text_1 = textboxify.Text(text="Press Q to open inventory,", size = 30, color=(255, 255, 255), background=(222,184,135))
        info_text_2 = textboxify.Text(text="F to throw out items,", size = 30, color=(255, 255, 255), background=(222,184,135))
        info_text_3 = textboxify.Text(text="and escape to exit.", size = 30, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        screen.blit(info_text_2.image, (40, 70))
        screen.blit(info_text_3.image, (40, 100))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        val = False

    def tutorialInteraction(self,screen):
        info_text_1 = textboxify.Text(text="Press E to interact with objects.", size = 29, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        val = False

    def tutorialEquipmenet(self,screen):
        info_text_1 = textboxify.Text(text="If you try to equip a computer with one already", size = 20, color=(255, 255, 255), background=(222,184,135))
        info_text_2 = textboxify.Text(text="it will try to place it in your inventory.", size = 20, color=(255, 255, 255), background=(222,184,135))
        info_text_3 = textboxify.Text(text="If your inventory is full, it will through out items.", size = 20, color=(255, 255, 255), background=(222,184,135))
        info_text_4 = textboxify.Text(text="If the tier is too high, you cannot equip that item.", size = 20, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        screen.blit(info_text_2.image, (40, 70))
        screen.blit(info_text_3.image, (40, 100))
        screen.blit(info_text_4.image, (40, 130))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        val = False
    
    def refreshScreen(self, screen):
        self.state = "active"
        key = pygame.key.get_pressed()
        # dialog_group = pygame.sprite.LayeredDirty()
        # dialog_group.clear(screen, pygame.Surface(screen.get_size()))
        for layer in self.sceneMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.sceneMap.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.sceneMap.tilewidth, y * self.sceneMap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.type == 'chest':
                        self.chests[obj.name] = self.initChest(obj)
                        self.chests[obj.name].scene = self
            # elif isinstance(layer, pytmx.TiledImageLayer):
            #     image = pygame.get_tile_image_by_gid(gid)
            #     if image:
            #         screen.blit(image, (0,0))
        # while True:
        #     print(str([str(entity) for entity in self.entities]))
        for entity in self.entities.sprites():
            entity.draw(screen)

    def render(self, screen):
        self.state = "active"
        key = pygame.key.get_pressed()
        # dialog_group = pygame.sprite.LayeredDirty()
        # dialog_group.clear(screen, pygame.Surface(screen.get_size()))
        for layer in self.sceneMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.sceneMap.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.sceneMap.tilewidth, y * self.sceneMap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if obj.type == 'chest':
                        self.chests[obj.name] = self.initChest(obj)
                        self.chests[obj.name].scene = self
            # elif isinstance(layer, pytmx.TiledImageLayer):
            #     image = pygame.get_tile_image_by_gid(gid)
            #     if image:
            #         screen.blit(image, (0,0))
        # while True:
        #     print(str([str(entity) for entity in self.entities]))
        for entity in self.entities.sprites():
            entity.draw(screen)
        if self.roomNum == 1:
            self.roomOne(screen)
        if self.roomNum == 2:
            self.roomTwo(screen)
        # dialogBox = DialogBox("Press WASD to move", (0,0,0), 25, (222,184,135))
        # dialogBox.render((100,100), screen)

    def roomOne(self, screen):
        self.tutorialMovement(screen)
        self.refreshScreen(screen)
        self.tutorialTerminal(screen)
        self.refreshScreen(screen)
        self.tutorialInteraction(screen)
        self.refreshScreen(screen)
        self.tutorialInventory(screen)
        self.refreshScreen(screen)
        self.tutorialEquipmenet(screen)
    def roomTwo(self, screen):
        self.tutorialMovement(screen)
        self.refreshScreen(screen)
        self.tutorialTerminal(screen)
        self.refreshScreen(screen)
        self.tutorialInteraction(screen)
        self.refreshScreen(screen)
        self.tutorialInventory(screen)
        self.refreshScreen(screen)
        self.tutorialEquipmenet(screen)
    def roomThree(self, screen):
        pass
        # return self.player.roomThreeCompleted and obj.type == 'removable'
    def roomFour(self, screen):
        pass
    def roomFive(self, screen):
        pass
    def roomSix(self, screen):
        pass
    def roomSeven(self, screen):
        darkness = pygame.Surface(screen.get_rect().size)
        darkness.fill((0, 0, 0))
        darkness.set_alpha(240)
        screen.blit(darkness, (0,0))
    def roomEight(self, screen):
        pass
    def roomNine(self, screen):
        pass
            # self.defaultState(screen, currentTime, events)
    def roomTen(self, screen):
        pass
    def roomEleven(self, screen):
        pass
    def roomTwelve(self, screen):
        pass

    # def toggleState(self):
    #     if self.state == "active":
    #         self.state = "paused"
    #     elif self.state == "paused":
    #         self.state

    def checkChests(self, screen, obj, event, currentTime):
        print("checking chests")
        chest = self.objects['chests'][obj.name]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not chest.alreadyAccessed:
            self.state = "chest"
            self.currentChest = chest
            print("open chest")
            return True

    def chestOpenedState(self, screen, currentTime, events):
        print("chest opened")
        self.player.isAccessingChest = True
        pygame.draw.rect(screen,(0,0,0),[0, 0, 460, 490])
        self.currentChest.open(screen)
        while self.player.isAccessingChest:
            # print("in loop")
            self.currentChest.update(screen)
            pygame.display.update()
            events = pygame.event.get()
            if any(event.type == pygame.KEYDOWN and event.key == pygame.K_e for event in events):
                break
            # print (selections)
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.player.isAccessingChest = False
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    self.currentChest.selectPrev()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    self.currentChest.selectNext()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.currentChest.selected(screen)
                    self.state = "active"
                print(self.currentChest.selection)
        # block player movement


    def transitionState(self, screen, currentTime, events):
        self.manager.nextScene()
        # self.state = "active"
        pass

    def defaultState(self, screen, currentTime, events):
        # print("default")
        key = pygame.key.get_pressed()
        for layer in self.sceneMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.sceneMap.get_tile_image_by_gid(gid)
                    if tile and ((not(self.roomNum == 3 and self.player.roomThreeCompleted and layer.name == 'Removable Props')) and (not(self.roomNum == 4 and self.player.roomFourCompleted and layer.name == 'removable4'))):
                        if not self.player.roomTwelveCompleted and layer=='Removable12':
                            pass
                        else:
                            screen.blit(tile, (x * self.sceneMap.tilewidth, y * self.sceneMap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                allHit = [False, False, False, False]
                for obj in layer:
                    if (not (self.roomNum == 3 and self.player.roomThreeCompleted and obj.type == 'removable')) and (not (self.roomNum == 4 and self.player.roomFourCompleted and obj.type == 'removable4')):
                        # print ("\n{objName}\n{objX}\n{objY}\n".format(objName=obj.name, objX = obj.x, objY = obj.y))
                        # print(self.player.roomThreeCompleted)
                        if self.player.x + 32 > obj.x and self.player.x < obj.x and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height:
                            print("hit on left, player's right")
                            allHit[0] = True
                            self.player.x -= 5
                            # self.player.canMoveRight = False
                        elif self.player.x + 42 > obj.x and self.player.x < obj.x and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height:
                            events = pygame.event.get()
                            for event in events:
                                if obj.type == 'chest':
                                    if (obj.name == 'Room8_Chest1' and not self.player.roomEightCompleted) or (obj.name == 'Room9_Chest1' and not self.player.roomNineCompleted) or ((obj.name == 'Room12_Chest1' or obj.name == 'Room12_Chest2') and not self.player.roomTwelveCompleted) or (obj.name == 'Room10_Chest1' and not self.player.roomTenCompleted):
                                        info_text_1 = textboxify.Text(text="This chest is locked", size = 30, color=(255, 255, 255), background=(222,184,135))
                                        screen.blit(info_text_1.image, (200, 150))
                                        pygame.display.update()
                                        sleep(0.15)
                                    elif self.checkChests(screen, obj, event, currentTime):
                                        break
                                if obj.type == 'new room':
                                    if (obj.name == 'Locked' and not self.player.roomFiveCompleted) or (obj.name == 'Locked10' and self.player.equipped.tier < 3):
                                        info_text_1 = textboxify.Text(text="This door is locked", size = 30, color=(255, 255, 255), background=(222,184,135))
                                        screen.blit(info_text_1.image, (200, 150))
                                        pygame.display.update()
                                        sleep(0.15)
                                    else:
                                        print("You have entered the {}".format(obj.name))
                                        # self.manager.nextScene()
                                        self.state = "transitioning"
                                        self.player.selectStartPos("left", (None, self.player.y))
                                        self.nextRoom = "right"
                                        break
                        if self.player.x < obj.x + obj.width and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x > obj.x:
                            print("hit on right, player's left")
                            allHit[1] = True
                            self.player.x += 5
                            # self.player.canMoveLeft = False
                        elif self.player.x - 10 < obj.x + obj.width and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x > obj.x:
                            events = pygame.event.get()
                            for event in events:
                                if obj.type == 'chest':
                                    if obj.name == 'Room8_Chest1' and not self.player.roomEightCompleted:
                                        pass
                                    elif obj.name == 'Room9_Chest1' and not self.player.roomNineCompleted:
                                        pass
                                    elif obj.name == 'Room12_Chest1' and not self.player.roomTwelveCompleted:
                                        pass
                                    elif obj.name == 'Room12_Chest2' and not self.player.roomTwelveCompleted:
                                        pass
                                    elif obj.name == 'Room10_Chest1' and not self.player.roomTenCompleted:
                                        pass
                                    elif self.checkChests(screen, obj, event, currentTime):
                                        break
                                if obj.type == 'new room':
                                    if (obj.name == 'Locked' and not self.player.roomFiveCompleted) or (obj.name == 'Locked10' and self.player.equipped.tier < 3):
                                        info_text_1 = textboxify.Text(text="This door is locked", size = 30, color=(255, 255, 255), background=(222,184,135))
                                        screen.blit(info_text_1.image, (200, 250))
                                        pygame.display.update()
                                        sleep(0.15)
                                    else:
                                        print("You have entered the {}".format(obj.name))
                                        # self.manager.nextScene()
                                        self.state = "transitioning"
                                        self.player.selectStartPos("right")
                                        self.nextRoom = "left"
                                        break
                        if self.player.y < obj.y + obj.height and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y > obj.y:
                            print("hit on bottom, player's top")
                            allHit[2] = True
                            self.player.y += 5
                            # self.player.canMoveUp = False
                        elif self.player.y - 10 < obj.y + obj.height and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y > obj.y:
                            events = pygame.event.get()
                            print(events)
                            for event in events:
                                if obj.type == 'chest':
                                    if obj.name == 'Room8_Chest1' and not self.player.roomEightCompleted:
                                        pass
                                    elif obj.name == 'Room9_Chest1' and not self.player.roomNineCompleted:
                                        pass
                                    elif obj.name == 'Room12_Chest1' and not self.player.roomTwelveCompleted:
                                        pass
                                    elif obj.name == 'Room12_Chest2' and not self.player.roomTwelveCompleted:
                                        pass
                                    elif obj.name == 'Room10_Chest1' and not self.player.roomTenCompleted:
                                        pass
                                    elif self.checkChests(screen, obj, event, currentTime):
                                        break
                                if obj.type == 'new room':
                                    if (obj.name == 'Locked' and not self.player.roomFiveCompleted) or (obj.name == 'Locked10' and self.player.equipped.tier < 3):
                                        info_text_1 = textboxify.Text(text="This door is locked", size = 30, color=(255, 255, 255), background=(222,184,135))
                                        screen.blit(info_text_1.image, (200, 250))
                                        pygame.display.update()
                                        sleep(0.15)
                                    else:
                                        # self.manager.nextScene()
                                        self.state = "transitioning"
                                        self.player.selectStartPos("bottom")
                                        self.nextRoom = "top"
                                        break
                        if self.player.y + 32 > obj.y and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y < obj.y:
                            self.player.y -= 5
                            allHit[3] = True
                            # self.player.canMoveDown = False
                            print("hit on top, player's bottom")
                        elif self.player.y + 42 > obj.y and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y < obj.y:
                            events = pygame.event.get()
                            for event in events:
                                if obj.type == 'chest':
                                    if obj.name == 'Room8_Chest1' and not self.player.roomEightCompleted:
                                        pass
                                    elif obj.name == 'Room9_Chest1' and not self.player.roomNineCompleted:
                                        pass
                                    elif obj.name == 'Room12_Chest1' and not self.player.roomTwelveCompleted:
                                        pass
                                    elif obj.name == 'Room12_Chest2' and not self.player.roomTwelveCompleted:
                                        pass
                                    elif obj.name == 'Room10_Chest1' and not self.player.roomTenCompleted:
                                        pass
                                    elif self.checkChests(screen, obj, event, currentTime):
                                        break
                                if obj.type == 'new room':
                                    if (obj.name == 'Locked' and not self.player.roomFiveCompleted) or (obj.name == 'Locked10' and self.player.equipped.tier < 3):
                                        info_text_1 = textboxify.Text(text="This door is locked", size = 30, color=(255, 255, 255), background=(222,184,135))
                                        screen.blit(info_text_1.image, (200, 250))
                                        for entity in self.entities:
                                            entity.draw(screen)
                                        pygame.display.update()
                                        sleep(0.15)
                                    else:
                                        # self.manager.nextScene()
                                        self.state = "transitioning"
                                        self.player.selectStartPos("top")
                                        self.nextRoom = "bottom"
                                        break
        if all(allHit):
            print("here")
            self.player.x -= 10
            self.player.y -= 10
        self.player.challengeStates = self.player.refreshChallengeStates()
        
        for challNum in self.player.challengeStates:
            if self.roomNum == challNum and not self.player.challengeStates[challNum]:
                self.roomTypes[self.roomNum](screen)
        
        # self.player.update(screen, key, currentTime)
        print("an updating")

        for entity in self.entities:
            entity.scene = self
            entity.draw(screen)
            # entity.update(screen, key, currentTime)
        self.player.update(screen, key, currentTime)
        # self.player.update(screen, keys, currentTime)
        # self.player.scene = self

    def update(self, screen, currentTime, events):
        # if self.state != "active":
        #     self.pause(screen)
        self.states[self.state](screen, currentTime, events)

    def pause(self, screen):
        self.manager.pauseScene(screen)
