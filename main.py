import pygame
import pytmx 
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *
from data import player, scene, sceneManager

pygame.init()

display_width = 460
display_height = 490

gameScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hacker Strike: Virus Offensive')
clock = pygame.time.Clock()

gameMap = load_pygame("./Assets/Map/map.tmx")

poseImgs = ["./Assets/Images/Sprites/Characters/restingDown.png",
            "./Assets/Images/Sprites/Characters/restingUp.png",
            "./Assets/Images/Sprites/Characters/restingLeft.png",
            "./Assets/Images/Sprites/Characters/restingRight.png",
            "./Assets/Images/Sprites/Characters/walkingDown1.png",
            "./Assets/Images/Sprites/Characters/walkingDown2.png",
            "./Assets/Images/Sprites/Characters/walkingUp1.png",
            "./Assets/Images/Sprites/Characters/walkingUp2.png",
            "./Assets/Images/Sprites/Characters/walkingLeft1.png",
            "./Assets/Images/Sprites/Characters/walkingLeft2.png",
            "./Assets/Images/Sprites/Characters/walkingRight1.png",
            "./Assets/Images/Sprites/Characters/walkingRight2.png"]

def scaleImgs(imgList):
    output = []
    for img in imgList:
        output.append(pygame.transform.scale(pygame.image.load(img).convert_alpha(), (32,32)))
    return output

def initPlayer():
    return player.Player(250, 250, scaleImgs(poseImgs))

# player = Player(250, 250)

# def game_loop():
#     gameExit = False
#     while not gameExit:
#         clock.tick(60)
#         sleep(0.08)
        
        

#         for layer in gameMap.visible_layers:
#             if isinstance(layer, pytmx.TiledTileLayer):
#                 for x, y, gid in layer:
#                     tile = gameMap.get_tile_image_by_gid(gid)
#                     if tile:
#                         gameScreen.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))
#             elif isinstance(layer, pytmx.TiledObjectGroup):
#                 # if layer.name == 'Chests':
#                 # player.canMoveRight = True
#                 for obj in layer:
#                     if player.x + 42 > obj.x and player.y + 32 >= obj.y and player.y <= obj.y + obj.height and player.x < obj.x:
#                         player.canMoveRight = False
#                         # print ("name: {} \ntype: {}".format(obj.name, obj.type))
#                         if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
#                             print("{} opened".format(obj.name))
#                         if obj.type == 'new room':
#                             print("You have entered the {}".format(obj.name))
#                         break
#                 else:
#                     for obj in layer:
#                         if player.x < obj.x + obj.width and player.y + 32 >= obj.y and player.y <= obj.y + obj.height and player.x > obj.x:
#                             player.canMoveLeft = False
#                             # print ("name: {} \ntype: {}".format(obj.name, obj.type))
#                             if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
#                                 print("{} opened".format(obj.name))
#                             if obj.type == 'new room':
#                                 print("You have entered the {}".format(obj.name))
#                             break
#                     else:
#                         player.canMoveLeft = True
#                         player.canMoveRight = True
#                 # if any(player.x + 42 > obj.x and player.y + 32 >= obj.y and player.y <= obj.y + obj.height and player.x < obj.x for obj in layer):
#                 #     if obj.type == 'new room':
#                 #         print("You have entered the {}".format(obj.name))
#                 #     player.canMoveRight = False
#                 # elif any(player.x < obj.x + obj.width and player.y + 32 >= obj.y and player.y <= obj.y + height and player.x > obj.x for obj in layer):
#                 #     player.canMoveLeft = False
#                 # else:
#                 #     player.canMoveLeft = True
#                 #     player.canMoveRight = True
#                 for obj in layer:
#                     if player.y < obj.y + obj.height and player.x + 32 >= obj.x and player.x <= obj.x + obj.width and player.y > obj.y:
#                         player.canMoveUp = False
#                         # print ("name: {} \ntype: {}".format(obj.name, obj.type))
#                         if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
#                             print("{} opened".format(obj.name))
#                         if obj.type == 'new room':
#                             print("You have entered the {}".format(obj.name))
#                         break
#                 else:
#                     for obj in layer:
#                         if player.y + 42 > obj.y and player.x + 32 >= obj.x and player.x <= obj.x + obj.width and player.y < obj.y:
#                             player.canMoveDown = False
#                             if obj.type == 'chest' and pygame.key.get_pressed()[pygame.K_e]:
#                                 print("{} opened".format(obj.name))
#                             # print ("name: {} \ntype: {}".format(obj.name, obj.type))
#                             if obj.type == 'new room':
#                                 print("You have entered the {}".format(obj.name))
#                             break
#                     else:
#                         player.canMoveUp = True
#                         player.canMoveDown = True
#             elif isinstance(layer, pytmx.TiledImageLayer):
#                 image = get_tile_image_by_gid(gid)
#                 if image:
#                     surface.blit(image, (0,0))
#         player.draw(gameScreen)
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#                gameExit = True

def main():
    screen_width, screen_height = 920, 490
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    currentTime = 0
    spriteGroup = pygame.sprite.Group()
    spriteGroup.add(initPlayer())
    scene1 = scene.Scene(1, gameMap, spriteGroup)
    manager = sceneManager.SceneManager([scene1, scene1])
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                manager.nextScene()

        manager.draw(screen)
        manager.update(currentTime, events)

        pygame.display.flip()
        currentTime = clock.tick(30)
        
if __name__ == '__main__':
    main()
    pygame.quit()