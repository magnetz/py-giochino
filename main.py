#!/usr/bin/env python3

import pygame
import sys
import player
import point
from pygame.locals import *

score = 0
max_score = 0
max_speed = 0
start_menu = 1
run = 1
replay = 1

def main():
    global score, max_score, max_speed, run, replay, start_menu

    pygame.init()
    clock = pygame.time.Clock()

    pygame.font.init()
    myfont = pygame.font.SysFont('ubuntu', 15)

    size = (320, 320)
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Giochino')

    p = player.Player(screen, 10, 40, 10, 10, (255, 0, 0), 2)
    max_speed = p.vel
    po = point.Point(screen, 5, 5, 5, 5, (255, 255, 255))
    po.recollocate()

    while start_menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(black)

        start_myfont = pygame.font.SysFont('ubuntu', 30)
        game_start = start_myfont.render('Giochino', False, white)
        screen.blit(game_start, (10, 10))

        text_myfont = pygame.font.SysFont('ubuntu', 20)
        game_text = text_myfont.render('Press <SPACE> and play!', False, white)
        screen.blit(game_text, (10, 40))

        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            start_menu = 0
            run = 1
            main()

        pygame.display.update()
        clock.tick(60)

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(black)
        po.draw()

        p.draw()
        p.move()

        if p.wall_collision():
            if score <= 0:
                run = 0
            else:
                score = 0
                screen.fill((255, 0, 0))

        collision_check(p, po)

        score_text = myfont.render(('score: %(score)s Highscore: %(max_score)s' % {"score": score, "max_score": max_score}), False, white)
        speed_text = myfont.render(('Speed: %(speed)s Max speed: %(max_speed)s' % {"speed": p.vel, "max_speed": max_speed}), False, white)
        screen.blit(score_text, (10, 10))
        screen.blit(speed_text, (10, 20))

        pygame.display.update()

        clock.tick(60)

    while replay:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(black)

        over_myfont = pygame.font.SysFont('ubuntu', 30)
        game_over = over_myfont.render('Game Over!', False, red)
        screen.blit(game_over, (10, 10))

        text_myfont = pygame.font.SysFont('ubuntu', 20)
        game_text = text_myfont.render('Reload with <SPACE>', False, white)
        screen.blit(game_text, (10, 40))

        score_text = text_myfont.render(('Highscore: %(max_score)s' % {"max_score": max_score}), False, white)
        speed_text = text_myfont.render(('Max speed: %(max_speed)s' % {"max_speed": max_speed}), False, white)
        screen.blit(score_text, (10, 60))
        screen.blit(speed_text, (10, 80))

        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            run = 1
            main()

        pygame.display.update()
        clock.tick(60)


    

def collision_check(player, point):
    global score, max_score, max_speed
    if player.x + player.w > point.x and player.x < point.x + point.w:
        if player.y + player.h > point.y and player.y < point.y + point.h:
            score += 10

            if score > max_score:
                max_score = score

            point.recollocate()
            new_speed = player.vel + 1

            if new_speed > max_speed:
                    max_speed = new_speed
            
            player.accellerate(new_speed)

if __name__ == '__main__': main()