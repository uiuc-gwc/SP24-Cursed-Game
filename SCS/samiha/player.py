import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Some starter stuff:
        starting_position = (400, 500)

        # Get the image and fix it to the correct size. 
        self.image = pygame.image.load("images/basket.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

        # self.rect is the rectangle around the image. 
        self.rect = self.image.get_rect(center=starting_position)

        self.score = 0    

    def display(self, screen):
        screen.blit(self.image, self.rect)

    # TODO: Implement this function.
    # This function should return True if the player is colliding with the food object.
    # You can use collierect to check if a player is colliding with a food object. 
    # https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
    def isCollidingWith(self, food):
        pass # Delete this line once you write real code.

    # keys_pressed is a list of all the keys that are currently pressed.
    # Documentation: https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
    # Examples: https://github.com/search?q=pygame.key.get_pressed+language%3APython&type=Code&l=Python
    # Find the list of keys here: https://www.pygame.org/docs/ref/key.html
    #
    # food_objects is a list of all the food objects. See food.py
    def update(self, keys_pressed, food_objects):
        # TODO: Update the player's position based on the keys that are pressed. 
        # You can change self.rect.x and self.rect.y to move the player.
        

        # TODO: Figure out what to do if the player is touching food objects.

        pass # Delete this line once you write real code.
