#!/usr/bin/env python3

import pygame, sys
from pygame.locals import *

class Player (object):
    
    def __init__(self, screen, x, y, w, h, color, vel):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.vel = vel
        self.screen = screen

    def draw(self):
        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.color, rect)

    def move(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x += self.vel * -1
        elif keys[pygame.K_RIGHT] and self.x + self.w < pygame.display.get_surface().get_width():
            self.x += self.vel * 1
        elif keys[pygame.K_UP] and self.y > 0:
            self.y += self.vel * -1
        elif keys[pygame.K_DOWN] and self.y + self.h < pygame.display.get_surface().get_height():
            self.y += self.vel * 1
