import pygame
from cutscenefunctions import *
from food import Food
from player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_surface = pygame.image.load("images/tanvi_samiha_house_background.jpeg").convert()
bg_surface = pygame.transform.rotozoom(bg_surface, 0, 2.05)


dad = pygame.image.load("images/dad.png")
dad = pygame.transform.rotozoom(dad, 0, 0.25)
boy = pygame.image.load("images/boiii.png")
boy = pygame.transform.rotozoom(boy, 0, 0.1)
dad_text1 = pygame.image.load("images/dad_text1.png")
dad_text1 = pygame.transform.rotozoom(dad_text1, 0, 0.5)

player = Player()
food_objects = [Food("fries")]

clock = pygame.time.Clock()


running = True
cutscene = True
cutscene_slide_number = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # reset the entire screen to white. 
    screen.fill((255, 255, 255))
    
    if cutscene:
        # Display the correct cutscene. 
        if cutscene_slide_number == 0:
            cutscene_slide_0(screen, bg_surface, dad, boy, dad_text1)

        # If the space button is pressed, move to the next cutscene. 
        keys = pygame.key.get_pressed()
        # Documentation: https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        # Examples: https://github.com/search?q=pygame.key.get_pressed+language%3APython&type=Code&l=Python
        # Find the list of keys here: https://www.pygame.org/docs/ref/key.html
        if keys[pygame.K_SPACE]:
            cutscene_slide_number += 1
        if cutscene_slide_number > 1:
            cutscene = False
                
    else:
        # McDonald's game. 
        # Stretch goal: Velocity is different for each type of food.
        # print("playing game. ")

        for food in food_objects:
            food.update()
            food.display(screen)

        player.update(pygame.key.get_pressed(), food_objects)
        player.display(screen)


        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {player.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

