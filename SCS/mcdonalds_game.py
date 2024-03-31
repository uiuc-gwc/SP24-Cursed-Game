import pygame
from cutscenefunctions import *
from food import Food
from player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# https://stackoverflow.com/questions/18948981/do-something-every-x-milliseconds-in-pygame  
ACTION = pygame.event.custom_type() # our custom event that contains an action

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
# food_objects = [Food("fries")]
food_objects = pygame.sprite.Group()

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
            bg_surface_path = "images/tanvi_samiha_house_background.jpeg"
            dad_path = "images/dad.png"
            boy_path = "images/boiii.png"
            dad_text1_path = "images/dad_text1.png"
            cutscene_slide_0(screen, bg_surface_path, dad_path, boy_path, dad_text1_path)

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

        # Create a new food object every 60 frames.
        if pygame.time.get_ticks() % 60 == 0:
            print("created new food object")
            food_objects.add(Food("fries", SCREEN_WIDTH, SCREEN_HEIGHT))

        # Update the food objects
        food_objects.update()

        # Update the player. 
        player.update(pygame.key.get_pressed(), food_objects)

        # Draw everything on the screen. 
        food_objects.draw(screen)
        player.display(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {player.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30) 

pygame.quit()


