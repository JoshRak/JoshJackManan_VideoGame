import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
import itertools
from pygame.locals import *
import data.items as items
import data.chest as chest
# from data.items import *
from data.dialogBox import DialogBox
import textboxify

class Scene(object):
    def __init__(self, roomNum, sceneMap, entities):
        self.sceneMap = sceneMap
        self.roomNum = roomNum
        self.entities = entities
        self.player = entities.sprites()[0]
        self.player.scene = self
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
        chestsDict = {
            "CPC1" : chest.Chest(computerTier2, 1, 'COMP', obj.x, obj.y),
            "KC1" : chest.Chest(keyboardTier1, 1, 'TOOL', obj.x, obj.y),
            "Chest1" : chest.Chest(mouseTier2, 2, 'TOOL', obj.x, obj.y),
            "Chest2" : chest.Chest(GPUTier3, 3, 'TOOL', obj.x, obj.y)
        }
        return chestsDict[obj.name]

    def initStates(self):
        statesDict = {
            "active":self.defaultState,
            "transitioning":self.transitionState,
            "chest":self.chestOpenedState,
            "popup":self.popupState
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
        info_text_1 = textboxify.Text(text="Press T to open terminal", size = 30, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        val = False
    def tutorialInventory(self, screen):
        info_text_1 = textboxify.Text(text="Press Q to open inventory and", size = 30, color=(255, 255, 255), background=(222,184,135))
        info_text_2 = textboxify.Text(text="escape to exit", size = 30, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        screen.blit(info_text_2.image, (40, 70))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        val = False
    def tutorialInteraction(self,screen):
        info_text_1 = textboxify.Text(text="Press E to interact with objects", size = 29, color=(255, 255, 255), background=(222,184,135))
        screen.blit(info_text_1.image, (40, 40))
        pygame.display.update()
        val = True
        while val:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        val = False

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
        for entity in self.entities:
            entity.draw(screen)
        if self.roomNum == 1:
            self.roomOne(screen)
        if self.roomNum == 2:
            self.roomTwo(screen)
        # dialogBox = DialogBox("Press WASD to move", (0,0,0), 25, (222,184,135))
        # dialogBox.render((100,100), screen)

    def roomOne(self, screen):
        self.tutorialMovement(screen)
        self.tutorialTerminal(screen)
        self.tutorialInteraction(screen)
        self.tutorialInventory(screen)
    def roomTwo(self, screen):
        self.tutorialMovement(screen)
        self.tutorialTerminal(screen)
        self.tutorialInteraction(screen)
        self.tutorialInventory(screen)
    # def roomThree(self, obj, screen):
    #     # while not self.player.roomThreeCompleted:
    #     return self.player.roomThreeCompleted and obj.type == 'removable'
    def roomFour(self, screen):
        pass
    def roomFive(self, screen):
        pass
    # def roomSix(self, screen):
    #     pass
    def roomSeven(self, screen):
        pass
    def roomEight(self, screen):
        pass
    def roomNine(self, screen):
        darkness = pygame.Surface(screen.get_rect().size)
        darkness.fill((0, 0, 0))
        darkness.set_alpha(170)
        screen.blit(darkness, (0,0))
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
                    if tile and not(self.roomNum == 3 and self.roomThree()):
                        screen.blit(tile, (x * self.sceneMap.tilewidth, y * self.sceneMap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if self.roomNum == 3 and self.player.roomThreeCompleted and obj.type == 'removable':
                        pass
                    elif self.player.x + 32 > obj.x and self.player.x < obj.x and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height:
                        print("hit on left, player's right")
                        self.player.canMoveRight = False
                        events = pygame.event.get()
                        for event in events:
                            if obj.type == 'chest':
                                if self.checkChests(screen, obj, event, currentTime):
                                    break
                            if obj.type == 'new room' and not (obj.name == 'Locked' and not self.player.roomFiveCompleted):
                                print("You have entered the {}".format(obj.name))
                                # self.manager.nextScene()
                                self.state = "transitioning"
                                self.player.selectStartPos("left", (None, self.player.y))
                                self.nextRoom = "right"
                                break
                        break
                else:
                    for obj in layer:
                        if self.roomNum == 3 and self.player.roomThreeCompleted and obj.type == 'removable':
                            pass
                        elif self.player.x < obj.x + obj.width and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x > obj.x:
                            print("hit on right, player's left")
                            self.player.canMoveLeft = False
                            events = pygame.event.get()
                            for event in events:
                                if obj.type == 'chest':
                                    if self.checkChests(screen, obj, event, currentTime):
                                        break
                                if obj.type == 'new room' and not (obj.name == 'Locked' and not self.player.roomFiveCompleted):
                                    print("You have entered the {}".format(obj.name))
                                    # self.manager.nextScene()
                                    self.state = "transitioning"
                                    self.player.selectStartPos("right")
                                    self.nextRoom = "left"
                                    break
                            break
                    else:
                        print("RIGHTLEFTTRUE")
                        self.player.canMoveLeft = True
                        self.player.canMoveRight = True

                for obj in layer:
                    if self.roomNum == 3 and self.player.roomThreeCompleted and obj.type == 'removable':
                        pass
                    elif self.player.y < obj.y + obj.height and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y > obj.y:
                        print("hit on bottom, player's top")
                        self.player.canMoveUp = False
                        events = pygame.event.get()
                        print(events)
                        for event in events:
                            if obj.type == 'chest':
                                if self.checkChests(screen, obj, event, currentTime):
                                    break
                            if obj.type == 'new room' and not (obj.name == 'Locked' and not self.player.roomFiveCompleted):
                                # self.manager.nextScene()
                                self.state = "transitioning"
                                self.player.selectStartPos("bottom")
                                self.nextRoom = "top"
                                break
                        break
                else:
                    for obj in layer:
                        if self.roomNum == 3 and self.player.roomThreeCompleted and obj.type == 'removable':
                            pass
                        elif self.player.y + 42 > obj.y and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y < obj.y:
                            self.player.canMoveDown = False
                            print("hit on top, player's bottom")
                            events = pygame.event.get()
                            for event in events:
                                if obj.type == 'chest':
                                    if self.checkChests(screen, obj, event, currentTime):
                                        break
                                if obj.type == 'new room' and not (obj.name == 'Locked' and not self.player.roomFiveCompleted):
                                    # self.manager.nextScene()
                                    self.state = "transitioning"
                                    self.player.selectStartPos("top")
                                    self.nextRoom = "bottom"
                                    break
                            break
                    else:
                        print("UPDOWNTRUE")
                        self.player.canMoveUp = True
                        self.player.canMoveDown = True
            # elif isinstance(layer, pytmx.TiledImageLayer):
            #     image = pygame.get_tile_image_by_gid(gid)
            #     if image:
            #         screen.blit(image, (0,0))

        # print("out of loop")
        # print(self.player.canMoveUp)
        # print(self.player.canMoveDown)
        # print(self.player.canMoveRight)
        # print(self.player.canMoveLeft)
        if self.player.roomNineCompleted == False:
            self.roomTypes[self.roomNum](screen)


        keys = pygame.key.get_pressed()
        self.player.update(screen, keys, currentTime)
        print("an updating")
        self.player.scene = self
        for entity in self.entities:
            entity.draw(screen)
        # self.player.update(screen, keys, currentTime)
        # self.player.scene = self

    def update(self, screen, currentTime, events):
        # if self.state != "active":
        #     self.pause(screen)
        self.states[self.state](screen, currentTime, events)

    def pause(self, screen):
        self.manager.pauseScene(screen)
