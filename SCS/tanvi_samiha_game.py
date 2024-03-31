import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
bg_surface = pygame.image.load("tanvi_samiha_house_background.jpeg").convert()
bg_surface = pygame.transform.rotozoom(bg_surface, 0, 2.05)


dad = pygame.image.load("dad.png")
dad = pygame.transform.rotozoom(dad, 0, 0.25)
boy = pygame.image.load("boiii.png")
boy = pygame.transform.rotozoom(boy, 0, 0.1)
dad_text1 = pygame.image.load("dad_text1.png")
dad_text1 = pygame.transform.rotozoom(dad_text1, 0, 0.5)
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.blit(bg_surface, (0, 0))
    screen.blit(dad, (1280/4, 720/2))
    screen.blit(boy, (1280/4+250, 720/2+100))
    screen.blit(dad_text1, (1280/4+150, 720/2-100))

    for event in event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                
                

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
