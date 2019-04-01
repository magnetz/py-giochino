#!/usr/bin/env python3

import pygame, sys, player, point
from pygame.locals import *

collision = 0
max_collision = 0

def main():
    global collision, max_collision

    pygame.init()
    clock = pygame.time.Clock()

    pygame.font.init()
    myfont = pygame.font.SysFont('ubuntu', 15)


    size = (320, 320)
    black = (0, 0, 0)
    white = (255, 255, 255)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Giochino')
    
    p = player.Player(screen, 10,40,10,10,(255,0,0),2)
    po = point.Point(screen, 5,5,5,5,(255,255,255))
    po.recollocate()

    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit(0)

        screen.fill(black)
        po.draw()

        p.draw()
        p.move()
        if p.wall_collision() :
                collision = 0
                screen.fill((255,0,0))

        collision_check(p, po)

        #point_text = myfont.render("Point: {0} Highscore: {1}".format(collision).format(max_collision), False, white)
        point_text = myfont.render(('Point: %(point)s Highscore: %(max_point)s' %  {"point": collision, "max_point": max_collision}), False, white)
        #speed_text = myfont.render("Speed: {0} Max speed: {1}".format(p.vel).format(p.initialVel + (collision * 2)), False, white)
        speed_text = myfont.render(('Speed: %(speed)s Max speed: %(max_speed)s' %  {"speed": p.vel, "max_speed": p.initialVel + (max_collision * 2)}), False, white)
        screen.blit(point_text,(10,10))
        screen.blit(speed_text,(10,20))
        
        pygame.display.update()
        
        clock.tick(60)

def collision_check(player, point):
    global collision, max_collision
    if player.x + player.w > point.x and player.x < point.x + point.w:
        if player.y + player.h > point.y and player.y < point.y + point.h:
            collision += 1

            if collision > max_collision:
                max_collision = collision

            point.recollocate()
            new_speed = player.vel + 2
            player.accellerate(new_speed)

if __name__ == '__main__': main()