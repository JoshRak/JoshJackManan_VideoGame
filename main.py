import pygame
import pytmx 
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *

pygame.init()

display_width = 460
display_height = 490

gameScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hacker Strike: Virus Offensive')
clock = pygame.time.Clock()
gameMap = load_pygame("./Assets/Map/map.tmx")
restingDownImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingDown.png").convert_alpha(), (32,32))
walkingDown1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingDown1.png").convert_alpha(), (32,32))
walkingDown2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingDown2.png").convert_alpha(), (32,32))
restingUpImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingUp.png").convert_alpha(), (32,32))
walkingUp1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingUp1.png").convert_alpha(), (32,32))
walkingUp2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingUp2.png").convert_alpha(), (32,32))
restingLeftImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingLeft.png").convert_alpha(), (32,32))
walkingLeft1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingLeft1.png").convert_alpha(), (32,32))
walkingLeft2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingLeft2.png").convert_alpha(), (32,32))
restingRightImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingRight.png").convert_alpha(), (32,32))
walkingRight1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingRight1.png").convert_alpha(), (32,32))
walkingRight2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingRight2.png").convert_alpha(), (32,32))
class Sprite(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.image = restingDownImage
        self.movedLeft = False
        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveRight = True
        self.canMoveLeft = True
        self.lastPressedButtons = ""
        # self.velocityX = 0
        # self.velocityY = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 7
        if any(key) and key.index(1) != 300:
            if (key[pygame.K_UP] or key[pygame.K_w]) and self.canMoveUp:
                self.y -= dist
                # self.velocityY = dist
                self.image = walkingUp1Image if self.movedLeft else walkingUp2Image
                self.lastPressedButtons = "UP"
            elif (key[pygame.K_DOWN] or key[pygame.K_s]) and self.canMoveDown:
                self.y += dist
                # self.velocityY = -dist
                self.image = walkingDown1Image if self.movedLeft else walkingDown2Image
                self.lastPressedButtons = "DOWN"
            # else:
                # self.velocityY = 0
            if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.canMoveLeft:
                self.x -= dist
                # self.velocityX = -dist
                self.image = walkingLeft1Image if self.movedLeft else walkingLeft2Image
                self.lastPressedButtons = "LEFT"
            elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.canMoveRight:
                self.x += dist
                # self.velocityX = dist
                self.image = walkingRight1Image if self.movedLeft else walkingRight2Image
                self.lastPressedButtons = "RIGHT"
            # else:
                # self.velocityX = 0
            self.movedLeft = not self.movedLeft
        else:
            # self.velocityX = self.velocityY = 0
            if self.lastPressedButtons == "LEFT":
                self.image = restingLeftImage
            elif self.lastPressedButtons == "UP":
                self.image = restingUpImage
            elif self.lastPressedButtons == "RIGHT":
                self.image = restingRightImage
            else:
                self.image = restingDownImage
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

sprite = Sprite()

def game_loop():
    gameExit = False
    while not gameExit:
        clock.tick(60)
        sleep(0.08)
        sprite.handle_keys()
        for layer in gameMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = gameMap.get_tile_image_by_gid(gid)
                    if tile:
                        gameScreen.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))
            elif isinstance(layer, pytmx.TiledObjectGroup):
                # if layer.name == 'Chests':
                # sprite.canMoveRight = True
                for obj in layer:
                    if sprite.x + 42 > obj.x and sprite.y + 32 >= obj.y and sprite.y <= obj.y + obj.height and sprite.x < obj.x:
                        sprite.canMoveRight = False
                        # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                        if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                            print("{} opened".format(obj.name))
                        if obj.type == 'new room':
                            print("You have entered the {}".format(obj.name))
                        break
                else:
                    for obj in layer:
                        if sprite.x < obj.x + obj.width and sprite.y + 32 >= obj.y and sprite.y <= obj.y + obj.height and sprite.x > obj.x:
                            sprite.canMoveLeft = False
                            # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                            if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                                print("{} opened".format(obj.name))
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name))
                            break
                    else:
                        sprite.canMoveLeft = True
                        sprite.canMoveRight = True
                # if any(sprite.x + 42 > obj.x and sprite.y + 32 >= obj.y and sprite.y <= obj.y + obj.height and sprite.x < obj.x for obj in layer):
                #     if obj.type == 'new room':
                #         print("You have entered the {}".format(obj.name))
                #     sprite.canMoveRight = False
                # elif any(sprite.x < obj.x + obj.width and sprite.y + 32 >= obj.y and sprite.y <= obj.y + height and sprite.x > obj.x for obj in layer):
                #     sprite.canMoveLeft = False
                # else:
                #     sprite.canMoveLeft = True
                #     sprite.canMoveRight = True
                for obj in layer:
                    if sprite.y < obj.y + obj.height and sprite.x + 32 >= obj.x and sprite.x <= obj.x + obj.width and sprite.y > obj.y:
                        sprite.canMoveUp = False
                        # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                        if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                            print("{} opened".format(obj.name))
                        if obj.type == 'new room':
                            print("You have entered the {}".format(obj.name))
                        break
                else:
                    for obj in layer:
                        if sprite.y + 42 > obj.y and sprite.x + 32 >= obj.x and sprite.x <= obj.x + obj.width and sprite.y < obj.y:
                            sprite.canMoveDown = False
                            if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
                                print("{} opened".format(obj.name))
                            # print ("name: {} \ntype: {}".format(obj.name, obj.type))
                            if obj.type == 'new room':
                                print("You have entered the {}".format(obj.name))
                            break
                    else:
                        sprite.canMoveUp = True
                        sprite.canMoveDown = True
            elif isinstance(layer, pytmx.TiledImageLayer):
                image = get_tile_image_by_gid(gid)
                if image:
                    surface.blit(image, (0,0))
        sprite.draw(gameScreen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
               gameExit = True

if __name__ == '__main__':
    game_loop()
    pygame.quit()
