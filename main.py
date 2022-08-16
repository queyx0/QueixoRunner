from lib2to3 import pygram
from pickle import TRUE
from pickletools import int4
import pygame as pg
from sys import exit

def display_score():
    current_time = int(pg.time.get_ticks()/ 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)


pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption('Runner')
clock = pg.time.Clock()
test_font = pg.font.Font('Font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

sky_surface = pg.image.load('Graphics/Sky.png').convert()
ground_surface = pg.image.load('Graphics/ground.png').convert()

#score_surf = test_font.render('Em busca do pipico dourado', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center =(400, 50))

snail_surface = pg.image.load('Graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pg.image.load('Personagem/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

#Intro Screen
player_stand = pg.image.load('Personagem/player_stand.png').convert_alpha()
player_stand = pg.transform.scale2x(player_stand)
player_stand_rec = player_stand.get_rect(center = (400, 200))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if game_active:    
            if event.type == pg.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                player_gravity = -23

            if event.type == pg.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pg.K_SPACE:
                    player_gravity = -23
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pg.time.get_ticks()/ 1000)

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface,(0,300))
        #pg.draw.rect(screen, '#c0e8ec', score_rect)
        #pg.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, (score_rect))
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <+ 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # COLISIONS
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rec)

    pg.display.update()
    clock.tick(60)