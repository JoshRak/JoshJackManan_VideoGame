import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *

class Scene(object):
    def __init__(self, roomNum, sceneMap, entities):
        self.sceneMap = sceneMap
        self.entities = entities
        self.player = entities.sprites()[0]
        self.player.scene = self

        self.roomNum = roomNum
        
        # build the room

    def render(self, screen):
        key = pygame.key.get_pressed()
        for layer in self.sceneMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.sceneMap.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.sceneMap.tilewidth, y * self.sceneMap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                # if layer.name == 'Chests':
                # self.player.canMoveRight = True
                for obj in layer:
                    if self.player.x + 42 > obj.x and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x < obj.x:
                        self.player.canMoveRight = False
                        # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                        if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                            print("{} opened".format(obj.name))
                        if obj.type == 'new room':
                            print("You have entered the {}".format(obj.name))
                        break
                else:
                    for obj in layer:
                        if self.player.x < obj.x + obj.width and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x > obj.x:
                            self.player.canMoveLeft = False
                            # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                            if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                                print("{} opened".format(obj.name))
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name))
                            break
                    else:
                        self.player.canMoveLeft = True
                        self.player.canMoveRight = True
                # if any(self.player.x + 42 > obj.x and self.player.y + 32 >= obj.y and self.player.y <= obj.y + obj.height and self.player.x < obj.x for obj in layer):
                #     if obj.type == 'new room':
                #         print("You have entered the {}".format(obj.name))
                #     self.player.canMoveRight = False
                # elif any(self.player.x < obj.x + obj.width and self.player.y + 32 >= obj.y and self.player.y <= obj.y + height and self.player.x > obj.x for obj in layer):
                #     self.player.canMoveLeft = False
                # else:
                #     self.player.canMoveLeft = True
                #     self.player.canMoveRight = True
                for obj in layer:
                    if self.player.y < obj.y + obj.height and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y > obj.y:
                        self.player.canMoveUp = False
                        # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                        if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                            print("{} opened".format(obj.name))
                        if obj.type == 'new room':
                            print("You have entered the {}".format(obj.name))
                        break
                else:
                    for obj in layer:
                        if self.player.y + 42 > obj.y and self.player.x + 32 >= obj.x and self.player.x <= obj.x + obj.width and self.player.y < obj.y:
                            self.player.canMoveDown = False
                            if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                                print("{} opened".format(obj.name))
                            # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name))
                            break
                    else:
                        self.player.canMoveUp = True
                        self.player.canMoveDown = True
#             elif isinstance(layer, pytmx.TiledImageLayer):
#                 image = get_tile_image_by_gid(gid)
#                 if image:
#                     surface.blit(image, (0,0))
        for entity in self.entities:
            entity.draw(screen)

    def update(self, currentTime, events):
        keys = pygame.key.get_pressed()
        self.player.update(keys, currentTime)
        

    # def exit(self):
    #     if self.roomNum+1 in rooms:
    #         self.manager.go_to(GameScene(self.roomNum+1))
    #     else:
    #         self.manager.go_to(CustomScene("You win!"))

    # def die(self):
    #     self.manager.go_to(CustomScene("You lose!"))

    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.manager.go_to(TitleScene())
