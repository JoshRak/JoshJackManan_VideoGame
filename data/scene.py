import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
import itertools
from pygame.locals import *
import data.items as items
import data.chest as chest
from data.items import *

class Scene(object):
    def __init__(self, roomNum, sceneMap, entities):
        self.sceneMap = sceneMap
        self.roomNum = roomNum
        self.entities = entities
        self.player = entities.sprites()[0]
        self.player.scene = self
        self.states = self.initStates()
        self.state = "active"
        self.chests = {}
        self.objects = self.initObjects()

        # build the room
    
    def initObjects(self):
        objectsDict = {
            "chests": self.chests
        }
        return objectsDict

    def initChest(self, obj):
        chestsDict = {
            "CPC1" : chest.Chest(mouseTier1, 1, 'TOOL', obj.x, obj.y),
            "KC1" : chest.Chest(mouseTier1, 1, 'TOOL', obj.x, obj.y),
        }
        
        return chestsDict[obj.name]

    def initStates(self):
        statesDict = {
            "active":self.default,
            "chest":self.chestOpened,
            "popup":self.popup,
            "challenge":self.challengeActive
        }
        return statesDict

    # def initChest(self, obj):
    #     chestsDict = {
    #         "CPC1" : chest.Chest(mouseTier1, 1, 'TOOL'),
    #         "KC1" : chest.Chest(mouseTier1, 1, 'TOOL'),
    #     }
    #     return chestsDict[obj.name]
    #     # for obj in layer:
    #     #     if obj.name == 'CPC1':
    #     #         chest1 = chest.Chest(mouseTier1, 1, 'TOOL', obj.x, obj.y)
    #     #     elif obj.name == 'CPC2':
                
    def render(self, screen):
        key = pygame.key.get_pressed()
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
            elif isinstance(layer, pytmx.TiledImageLayer):
                image = pygame.get_tile_image_by_gid(gid)
                if image:
                    screen.blit(image, (0,0))
        for entity in self.entities:
            entity.draw(screen)

    # def toggleState(self):
    #     if self.state == "active":
    #         self.state = "paused"
    #     elif self.state == "paused":
    #         self.state 

    def chestOpened(self, screen, obj, currentTime):
        self.chests[obj.name].open(screen, currentTime)
        # block player movement
        # self.chest.render()
    
    def chestClose(self, screen, obj, currentTime):
        pass

    def chestUpdate(self, screen, obj, currentTime, events):
        pass

    def popup(self, screen, currentTime, events):
        pass
    
    def challengeActive(self, screen, currentTime, events):
        pass

    def pause(self, screen):
        self.manager.pauseScene(screen)

    def update(self, screen, currentTime, events):
        if self.state != "active":
            self.pause(screen)
        self.states[self.state](screen, currentTime, events)
    def checkChests(self, screen, obj, event, currentTime):
        selections = itertools.cycle(["LEAVE", 'EQUIP', 'STORE'])
        selection = next(selections)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not self.objects['chests'][obj.name].alreadyAccessed:
            self.player.isAccessingChest = True
            pygame.draw.rect(screen,(0,0,0),[0, 0, 460, 490])
            self.chestOpened(screen, obj, currentTime)
            while self.player.isAccessingChest:
                # print("in loop")
                pygame.display.update()
                events = pygame.event.get()
                if any(event.type == pygame.KEYDOWN and event.key == pygame.K_e for event in events):
                    break
                # print (selections)
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e: 
                        self.player.isAccessingChest = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        selection = next(selections)
                        selection = next(selections)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        selection = next(selections)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.objects["chests"][obj.name].selected(screen, self.player, selection)
                    print(selection)

    def default(self, screen, currentTime, events):
        key = pygame.key.get_pressed()
        for layer in self.sceneMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.sceneMap.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.sceneMap.tilewidth, y * self.sceneMap.tileheight))

            elif isinstance(layer, pytmx.TiledObjectGroup):
                for obj in layer:
                    if self.player.x + 32 > obj.x and self.player.x < obj.x and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height:
                        # print("hit left")
                        self.player.canMoveRight = False
                        events = pygame.event.get()
                        for event in events:
                            if obj.type == 'chest':
                                self.checkChests(screen, obj, event, currentTime)
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name)) 
                        break 
                    elif self.player.x < obj.x + obj.width and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x > obj.x:
                        # print("hit right")
                        self.player.canMoveLeft = False
                        events = pygame.event.get()
                        for event in events:
                            if obj.type == 'chest':
                                self.checkChests(screen, obj, event, currentTime)
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name))
                        break
                else:
                    self.player.canMoveLeft = True
                    self.player.canMoveRight = True
                        
                for obj in layer:
                    if self.player.y < obj.y + obj.height and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y > obj.y:
                        # print("hit down")
                        self.player.canMoveUp = False
                        events = pygame.event.get()
                        for event in events:
                            if obj.type == 'chest':
                                self.checkChests(screen, obj, event, currentTime)
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name)) 
                        break
                    elif self.player.y + 42 > obj.y and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y < obj.y:
                        self.player.canMoveDown = False
                        # print("hit up")
                        events = pygame.event.get()
                        for event in events:
                            if obj.type == 'chest':
                                self.checkChests(screen, obj, event, currentTime)
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name))
                        break
                else:
                    self.player.canMoveUp = True
                    self.player.canMoveDown = True
            # elif isinstance(layer, pytmx.TiledImageLayer):
            #     image = pygame.get_tile_image_by_gid(gid)
            #     if image:
            #         screen.blit(image, (0,0))

        # print("out of loop")

        keys = pygame.key.get_pressed()
        self.player.update(screen, keys, currentTime)
        self.player.scene = self
        for entity in self.entities:
            entity.draw(screen)
        self.player.update(screen, keys, currentTime)
        self.player.scene = self

    
  
    # def chestInteraction(obj, chestContents, chestType):
    #     if obj.type == 'chest' and pygame.get_key_pressed()[pygame.K_e]:
    #         chest.Chest(chestContents, 1, chestType)

    # def exit(self):
    #     if self.roomNum+1 in rooms:
    #         self.manager.go_to(GameScene(self.roomNum+1))
    #     else:
    #         self.manager.go_to(CustomScene("You win!"))

    # def die(self):
    #     self.manager.go_to(CustomScene("You lose!"))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # self.manager.go_to(TitleScene())
                pass
