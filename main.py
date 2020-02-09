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
            if key[pygame.K_UP] and self.canMoveUp:
                self.y -= dist
                # self.velocityY = dist
                self.image = restingDownImage
                self.lastPressedButtons = "UP"
            elif key[pygame.K_DOWN] and self.canMoveDown:
                self.y += dist
                # self.velocityY = -dist
                self.image = walkingDown1Image if self.movedLeft else walkingDown2Image
                self.lastPressedButtons = "DOWN"
            # else:
                # self.velocityY = 0
            if key[pygame.K_LEFT] and self.canMoveLeft:
                self.x -= dist
                # self.velocityX = -dist
                self.image = restingDownImage
                self.lastPressedButtons = "LEFT"
            elif key[pygame.K_RIGHT] and self.canMoveRight:
                self.x += dist
                # self.velocityX = dist
                self.image = restingDownImage
                self.lastPressedButtons = "RIGHT"
            # else:
                # self.velocityX = 0
            self.movedLeft = not self.movedLeft
        else:
            # self.velocityX = self.velocityY = 0
            if self.lastPressedButtons == "LEFT":
                pass
            elif self.lastPressedButtons == "UP":
                pass
            elif self.lastPressedButtons == "RIGHT":
                pass
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
                if layer.name == 'Chests':
                    for obj in layer:
                        print ("obj: {},{}".format(obj.x, obj.y))
                        print ("sprite: {},{}".format(sprite.x, sprite.y))
                        if sprite.x + 42 > obj.x and sprite.y + 32 >= obj.y and sprite.y <= obj.y + 32 and sprite.x < obj.x:
                            sprite.canMoveRight = False
                        elif sprite.x < obj.x + 42 and sprite.y + 32 >= obj.y and sprite.y <= obj.y + 32 and sprite.x > obj.x:
                            sprite.canMoveLeft = False
                        else:
                            sprite.canMoveLeft = True
                            sprite.canMoveRight = True
                        if sprite.y < obj.y + 42 and sprite.x + 32 >= obj.x and sprite.x <= obj.x + 32 and sprite.y > obj.y:
                            sprite.canMoveUp = False
                        elif sprite.y + 42 > obj.y and sprite.x + 32 >= obj.x and sprite.x <= obj.x + 32 and sprite.y < obj.y:
                            sprite.canMoveDown = False
                        else:
                            sprite.canMoveDown = True
                            sprite.canMoveUp = True
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
