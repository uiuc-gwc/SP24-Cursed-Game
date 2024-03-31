import pygame, random

class Food(pygame.sprite.Sprite):
    def __init__(self, food_type, screen_width, screen_height):
        super().__init__()


        self.screen_width = screen_width
        self.screen_height = screen_height

        # Some starter stuff:
        # TODO: Step 4: Change the starting position of the food object.
        # https://docs.python.org/3/library/random.html
        # has some resources on how to get a random number. 
        starting_position = (300, 500)

        # Get the image and fix it to the correct size. 
        self.image = pygame.image.load("images/fries.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

        # self.rect is the rectangle around the image. 
        self.rect = self.image.get_rect(center=starting_position)

        self.visible = True


    def update(self):
        # TODO: Move the food down. 
        # You can change the position of the food by changing self.rect.x and self.rect.y

        # If the food is off the screen, hide it.
        pass # Delete this line once you write real code. 

    def display(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

    def hide(self):
        self.visible = False
        self.kill()