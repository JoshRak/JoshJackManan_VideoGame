import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *
from data import player, scene, sceneManager, ghostPlayer

def scaleImgs(imgList): # scale the image to a 32x32 pixel size
    output = []
    for img in imgList:
        output.append(pygame.transform.scale(pygame.image.load(img).convert_alpha(), (32,32)))
    return output

def initPlayer(poseImgs, isHacker): # intialize all the poses of the player
    return player.Player(250, 250, scaleImgs(poseImgs), isHacker)

def initGhostPlayer(poseImgs): # initalize the images of the ghost player from the server
    return ghostPlayer.GhostPlayer(250, 250, scaleImgs(poseImgs))

def initRooms(gameMaps, poseImgs, poseImgs2): # initalize the rooms and add the sprites to the rooms
    spriteGroup = pygame.sprite.Group()
    spriteGroup.add(initPlayer(poseImgs, False))
    spriteGroup.add(initGhostPlayer(poseImgs2))
    # 1, 2, 5, 6, 8

    lst = []

    for i in range(0, len(gameMaps)):
        lst.append(scene.Scene(i+1, gameMaps[i], spriteGroup))

    return lst

def main(): # open the game and load in all necessary images and map files
    pygame.init()

    screen_width, screen_height = 448, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Hackerverse')
    currentTime = 0

    gameMaps = [load_pygame("./Assets/Map/Tutorial_Room1.tmx"),
            load_pygame("./Assets/Map/Tutorial_Room2.tmx"),
            load_pygame("./Assets/Map/Garbage_Room.tmx"),
            load_pygame("./Assets/Map/Jail_Room.tmx"),
            load_pygame("./Assets/Map/Island_Room.tmx"),
            load_pygame("./Assets/Map/House_Room.tmx"),
            load_pygame("./Assets/Map/Brightness_Room.tmx"),
            load_pygame("./Assets/Map/Cat_Room.tmx"),
            load_pygame("./Assets/Map/Tac_Room.tmx"),
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
    
    ghostPlayerPoseImgs = [ "./Assets/Images/Sprites/Characters/restingDownP2.png",
                            "./Assets/Images/Sprites/Characters/restingUpP2.png",
                            "./Assets/Images/Sprites/Characters/restingLeftP2.png",
                            "./Assets/Images/Sprites/Characters/restingRightP2.png",
                            "./Assets/Images/Sprites/Characters/walkingDown1P2.png",
                            "./Assets/Images/Sprites/Characters/walkingDown2P2.png",
                            "./Assets/Images/Sprites/Characters/walkingUp1P2.png",
                            "./Assets/Images/Sprites/Characters/walkingUp2P2.png",
                            "./Assets/Images/Sprites/Characters/walkingLeft1P2.png",
                            "./Assets/Images/Sprites/Characters/walkingLeft2P2.png",
                            "./Assets/Images/Sprites/Characters/walkingRight1P2.png",
                            "./Assets/Images/Sprites/Characters/walkingRight2P2.png"]

    manager = sceneManager.SceneManager(initRooms(gameMaps, poseImgs, ghostPlayerPoseImgs), False)
    val = True
    screen.blit(pygame.transform.scale(pygame.image.load("./Assets/Images/startSceneAdmin.png").convert_alpha(), (448, 480)), (0,0))
    # manager.renderOpeningScene(screen, pygame.transform.scale(pygame.image.load("./Assets/Images/startSceneAdmin.png").convert_alpha(), (448,480)))
    pygame.display.update()
    # manager.draw(screen)
    while val:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    val = False
    
    # while True:
    #     pygame.display.update()
    #     events = pygame.event.get()
    #     if not manager.renderSelectionScene(screen, ["./Assets/Images/selectionSceneWindows.png", "./Assets/Images/selectionSceneMac.png", "./Assets/Images/selectionSceneLinux.png"], events):
    #         break

    manager.draw(screen)
    
    gameExit = False
    
    while not gameExit:
        events = pygame.event.get()

        manager.update(screen, currentTime, events)

        pygame.display.flip()
        currentTime = clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()
