import pygame 

def cutscene_slide_0(screen, bg_surface_path, dad_path, boy_path, dad_text1_path):

    bg_surface = pygame.image.load(bg_surface_path).convert()
    bg_surface = pygame.transform.rotozoom(bg_surface, 0, 2.05)


    dad = pygame.image.load(dad_path).convert_alpha()
    dad = pygame.transform.rotozoom(dad, 0, 0.25)
    boy = pygame.image.load(boy_path).convert_alpha()
    boy = pygame.transform.rotozoom(boy, 0, 0.1)
    dad_text1 = pygame.image.load(dad_text1_path).convert_alpha()
    dad_text1 = pygame.transform.rotozoom(dad_text1, 0, 0.5)


    screen.blit(bg_surface, (0, 0))
    screen.blit(dad, (1280/4, 720/2))
    screen.blit(boy, (1280/4+250, 720/2+100))
    screen.blit(dad_text1, (1280/4+150, 720/2-100))