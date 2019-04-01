#!/usr/bin/env python3

import pygame, sys, player, point
from pygame.locals import *

collision = 0

def main():
    global collision

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

        point_text = myfont.render("Point: {0}".format(collision), False, white)
        speed_text = myfont.render("Speed: {0}".format(p.vel), False, white)
        screen.blit(point_text,(10,10))
        screen.blit(speed_text,(10,20))
        
        pygame.display.update()
        
        clock.tick(60)

def collision_check(player, point):
    global collision
    if player.x + player.w > point.x and player.x < point.x + point.w:
        if player.y + player.h > point.y and player.y < point.y + point.h:
            collision += 1
            point.recollocate()
            new_speed = player.vel + 2
            player.accellerate(new_speed)

if __name__ == '__main__': main()