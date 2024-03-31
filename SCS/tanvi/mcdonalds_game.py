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
food_objects = pygame.sprite.Group()
# TODO: Step 1: For starters, create one Food object here. 
# TODO: Step 2: Add it to food_objets using food_objects.add() 

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
    
    
    # McDonald's game. 
    # Stretch goal: Velocity is different for each type of food.
    # print("playing game. ")

    # Create a new food object every 60 frames.
    # TODO: Create a new food object every few (60? 30? up to you) frames. 
    # You can use pygame.time.get_ticks() 
    # It might help to remember what the % operator does. 
    # (remember to delete the old Food object you created at the top of this file! )

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


