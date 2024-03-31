import pygame 

def cutscene_slide_0(screen, bg_surface, dad, boy, dad_text1):
    screen.blit(bg_surface, (0, 0))
    screen.blit(dad, (1280/4, 720/2))
    screen.blit(boy, (1280/4+250, 720/2+100))
    screen.blit(dad_text1, (1280/4+150, 720/2-100))