import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',60)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
score_surface = test_font.render('RUNNER', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,100))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    # draw all our elements
    # update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()      
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity =- 20


#        if event.type == pygame.MOUSEBUTTONUP:
#            print("mouse up")
        
#        if event.type == pygame.MOUSEMOTION:
#            if player_rect.collidepoint(event.pos):
#                print("OVER THE PLAYER")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity =- 20

#        if event.type == pygame.KEYUP:
#            print("keyup")
 

  # attaching game surface to display surface        
    SURFACE.blit(sky_surface, (0,0))
    SURFACE.blit(ground_surface, (0,300))
    
    pygame.draw.rect(SURFACE,'#c0e8ec',score_rect)
    pygame.draw.rect(SURFACE,'#c0e8ec',score_rect,6)
    SURFACE.blit(score_surface, score_rect)
    
    #pygame.draw.line(SURFACE,'White',(0,0),(799,399),5)

    SURFACE.blit(snail_surface, snail_rect) 
    snail_rect.left -= 4
    if snail_rect.left <= -50:
        snail_rect.left = 800
    
    #PLAYER
    player_gravity += 1
    player_rect.y += player_gravity
    
    if player_rect.bottom > 300:
        player_rect.bottom = 300

    if player_rect.top < 0:
        player_rect.top = 0
        player_gravity += 8
    #SURFACE.blit(player_surface,player_rect)
    SURFACE.blit(player_surface,player_rect)


    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')

    #if player_rect.colliderect(snail_rect):
    #    print("Collision")

#    mouse_pos = pygame.mouse.get_pos()
#    if player_rect.collidepoint(mouse_pos):
#        print("OVER THE PLAYER")


    pygame.display.update()
    clock.tick(60)



