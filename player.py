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
        self.initialVel = vel
        self.vel = vel
        self.screen = screen
        self.hDirection = 0
        self.vDirection = 1

    def draw(self):
        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.color, rect)

    def move(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.hDirection = -1
            self.vDirection = 0
        elif keys[pygame.K_RIGHT]:
            self.hDirection = 1
            self.vDirection = 0
        elif keys[pygame.K_UP]:
            self.hDirection = 0
            self.vDirection = -1
        elif keys[pygame.K_DOWN]:
            self.hDirection = 0
            self.vDirection = 1

        self.x += self.vel * self.hDirection
        self.y += self.vel * self.vDirection

    def accellerate(self, vel):
        self.vel = vel

    def wall_collision(self):
        if self.x - self.vel < 0:
            self.hDirection = 1
            self.vDirection = 0
            self.vel = self.initialVel
            return True
        elif self.x + self.w + self.vel > pygame.display.get_surface().get_width():
            self.hDirection = -1
            self.vDirection = 0
            self.vel = self.initialVel
            return True
        elif self.y - self.vel < 0:
            self.hDirection = 0
            self.vDirection = 1
            self.vel = self.initialVel
            return True
        elif self.y + self.h + self.vel > pygame.display.get_surface().get_height():
            self.hDirection = 0
            self.vDirection = -1
            self.vel = self.initialVel
            return True
