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
        # TODO: Step 4: If the player is colliding with the object, print "Colliding with food object"
                    #   If the player is not colliding, print "Not colliding with food object"
        collide = self.rect.colliderect(food.rect)
        
        return collide
        
        pass # Delete this line once you write real code.

    # keys_pressed is a list of all the keys that are currently pressed.
    # Documentation: https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
    # Examples: https://github.com/search?q=pygame.key.get_pressed+language%3APython&type=Code&l=Python
    # Find the list of keys here: https://www.pygame.org/docs/ref/key.html
    #
    # food_objects is a list of all the food objects. See food.py
    def update(self, keys_pressed, food_objects):
        # TODO: Step 1: If the right key is pressed, print "Right key"
        #               If the left key is pressed, print "Left key"
        if keys_pressed[pygame.K_RIGHT]:
            print("Right key")
            self.rect.x = self.rect.x + 8
        if keys_pressed [pygame.K_LEFT]:
            print("Left key")
            self.rect.x = self.rect.x - 8
        # TODO Step 2: Update the player's position based on the keys that are pressed. 
        # You can change self.rect.x and self.rect.y to move the player.
        for food in food_objects:
            print(self.isCollidingWith(food))

            if self.isCollidingWith(food):
                food.hide()
                #change the amount you add based on foodtype: fries(1), or burgers (2)
                
                if food.food_type == 'fries':
                    self.score =  self.score + 1
                if food.food_type == 'burgers':
                    self.score = self.score + 2
                if food.food_type == 'coke':
                    self.score = self.score + 1.75

        

        # TODO Step 3: Write a loop that goes through all the food objects. 
        # TODO step 4: Check if the player is touching each of the food objects. 
        # TODO Step 5: Figure out what to do if the player is touching food objects.

        pass # Delete this line once you write real code.
