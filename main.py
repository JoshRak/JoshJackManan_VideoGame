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

gameMaps = [load_pygame("./Assets/Map/Cow_Room.tmx"),
            load_pygame("./Assets/Map/Cow_Room.tmx"),
            load_pygame("./Assets/Map/Garbage_Room.tmx"),
            load_pygame("./Assets/Map/Jail_Room.tmx"),
            load_pygame("./Assets/Map/Cow_Room.tmx"),
            load_pygame("./Assets/Map/Cow_Room.tmx"),
            load_pygame("./Assets/Map/Cat_Room.tmx"),
            load_pygame("./Assets/Map/Cow_Room.tmx"),
            load_pygame("./Assets/Map/Brightness_Room.tmx"),
            load_pygame("./Assets/Map/Cow_Room.tmx"),
            load_pygame("./Assets/Map/Math_Room.tmx"),
            load_pygame("./Assets/Map/Zip_Room.tmx")]

# 1 2 garbage jail cd, cd, cat_room, reversecat, brightness, cow, math, zip

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

def initRooms():
    spriteGroup = pygame.sprite.Group()
    spriteGroup.add(initPlayer())
    # 1, 2, 5, 6, 8

    lst = []

    for i in range(0, len(gameMaps)):
        lst.append(scene.Scene(i+1, gameMaps[i], spriteGroup))

    return lst

def main():
    screen_width, screen_height = 448, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    currentTime = 0
    
    manager = sceneManager.SceneManager(initRooms())
    gameExit = False
    newRoom = True
    while not gameExit:
        if newRoom:
            manager.draw(screen)
            newRoom = False

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                gameExit = True
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            #     newRoom = True
            #     manager.nextScene()
        manager.update(screen, currentTime, events)

        pygame.display.flip()
        currentTime = clock.tick(30)
        
if __name__ == '__main__':
    main()
    pygame.quit()
