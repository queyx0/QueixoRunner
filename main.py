import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption('Runner')
clock = pg.time.Clock()
test_font = pg.font.Font('Font/Pixeltype.ttf', 50)

sky_surface = pg.image.load('Graphics/Sky.png').convert()
ground_surface = pg.image.load('Graphics/ground.png').convert()
text_surface = test_font.render('Em busca do pipico de ouro', False, 'Black')

snail_surface = pg.image.load('Graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pg.image.load('Graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300, 50))
    snail_rect.x -= 4
    if snail_rect.right <+ 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(snail_rect): 
        break

    # draw all our elemtns
    # update everthing
    pg.display.update()
    clock.tick(60)