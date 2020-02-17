import pygame
from PIL import Image
from time import sleep

screen_width, screen_height = 448, 480
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
currentTime = 0

def displayTier(tier):
	gapWidth = 20
	starImg = Image.open("./Assets/Images/transparentStar.png")
	# starImg.show()
	img = Image.new('RGBA', ((starImg.size[0] * tier) + (gapWidth * (tier+1)), starImg.size[1] + (gapWidth * 2)), (127,0,127,0))
	for i in range(0, tier):
		img.paste(starImg, ((i * starImg.size[0]) + ((i + 1) * gapWidth), gapWidth), mask=starImg)

	resizeFactor = 0.1
	img = img.resize((round(img.size[0] * resizeFactor), round(img.size[1] * resizeFactor)))

	path = "./Assets/Images/testStars.png"
	img.save(path)
	return path

# displayTier(4)

starsImg = pygame.image.load(displayTier(3)).convert_alpha()
chestImage = pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestOpened.png"), (384, 426))




gameExit = False
while not gameExit:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gameExit = True

    # screen.blit(pygame.transform.scale(pygame.image.load(displayTier(4)).convert_alpha(), tuple(round(0.1*x) for x in Image.open(displayTier(4)).size)), (0,0))
    # screen.blit(pygame.image.load(displayTier(4)).convert_alpha(), (0,0))
    chestW, chestH = chestImage.get_rect().size
    starsW, starsH = starsImg.get_rect().size
    screenW, screenH = screen.get_size()


    screen.blit(chestImage, (0,0))
    # print(self.contents)
    # screen.blit(pygame.transform.scale(pygame.image.load(contents.imagePath), (140, 155)), (155, 120))
    screen.blit(starsImg, (round((chestW / 2) - (starsW / 2)), round((0.7 * chestH) - (starsH / 2))))
    pygame.display.flip()
    currentTime = clock.tick(30)