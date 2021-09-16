import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',70)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('RUNNER', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))


while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()      
            exit()
    # attaching game surface to display surface        
    SURFACE.blit(sky_surface, (0,0))
    SURFACE.blit(ground_surface, (0,300))
    SURFACE.blit(text_surface, (325,100))
    SURFACE.blit(snail_surface, snail_rect) 
    snail_rect.left -= 4
    if snail_rect.left <= -50:
        snail_rect.left = 800
    
    SURFACE.blit(player_surface,player_rect)


    pygame.display.update()
    clock.tick(60)



