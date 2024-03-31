import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self, food_type):
        super().__init__()
        
        # Some starter stuff:
        starting_position = (200, 500)

        # Get the image and fix it to the correct size. 
        self.image = pygame.image.load("images/fries.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)

        # self.rect is the rectangle around the image. 
        self.rect = self.image.get_rect(center=starting_position)

        self.visible = True

    def update(self):
        # Move the food down. 
        # self.rect.y += 5
        pass

    def display(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

    def hide(self):
        self.visible = False
        self.kill()