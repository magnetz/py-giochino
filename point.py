#!/usr/bin/env python3

import pygame, sys, random
from pygame.locals import *

class Point (object):

    def __init__(self, screen, x, y, w, h, color):
        self.x, self.y, self.w, self. h = x, y, w, h
        self.color = color
        self.screen = screen

    def draw(self):
        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.color, rect)

    def recollocate(self):
        self.x = random.randint(0 + 30, pygame.display.get_surface().get_width() - self.w - 30)
        self.y = random.randint(0 + 30, pygame.display.get_surface().get_height() - self.h - 30)