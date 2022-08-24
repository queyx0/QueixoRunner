from cgi import test
from lib2to3 import pygram
from pickle import TRUE
from pickletools import int4
import pygame as pg
from sys import exit
from random import randint

def display_score():
    current_time = int(pg.time.get_ticks()/ 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

    #player walking animation on floor
    #display the jump when jump

pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption('Runner')
clock = pg.time.Clock()
test_font = pg.font.Font('Font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_Music = pg.mixer.Sound('Sounds/music.wav')
bg_Music.set_volume(0.1)
bg_Music.play(loops = -1)

sky_surface = pg.image.load('Graphics/Sky.png').convert()
ground_surface = pg.image.load('Graphics/ground.png').convert()

#score_surf = test_font.render('Em busca do pipico dourado', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center =(400, 50))

#Sounds
jump_sound = pg.mixer.Sound('Sounds/audio_jump.mp3')
jump_sound.set_volume(0.15)



#Snail
snail_frame_1 = pg.image.load('Graphics/Snail/snail1.png').convert_alpha()
snail_frame_2 = pg.image.load('Graphics/Snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

#Fly
fly_frame_1 = pg.image.load('Graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pg.image.load('Graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pg.image.load('Personagem/player_walk_1.png').convert_alpha()
player_walk_2 = pg.image.load('Personagem/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pg.image.load('Personagem/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

#Intro Screen
player_stand = pg.image.load('Personagem/player_stand.png').convert_alpha()
player_stand = pg.transform.scale2x(player_stand)
player_stand_rec = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Queixada maravilha', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))
7
#Timer
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pg.USEREVENT + 2
pg.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pg.USEREVENT + 3
pg.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        

        if game_active:    
            if event.type == pg.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                player_gravity = -23
                jump_sound.play()

            if event.type == pg.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pg.K_SPACE:
                    player_gravity = -23
                    jump_sound.play()
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_active = True
                start_time = int(pg.time.get_ticks()/ 1000)

        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))
            
            if event.type == snail_animation_timer:    
                if snail_frame_index == 0:
                    snail_frame_index=1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1 
                else: 
                    fly_frame_index = 0
                fly_surf = fly_frames[snail_frame_index]
        
        


    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface,(0,300))
        #pg.draw.rect(screen, '#c0e8ec', score_rect)
        #pg.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, (score_rect))
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <+ 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # COLISIONS
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rec)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        

    pg.display.update()
    clock.tick(60)