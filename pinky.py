"""
Pinky - różowy duszek

Tryby:
Chase - poscig, celuje w 4 pola przed pacmanem
Scatter - udaje sie do bezpiecznego rogu (lewy gorny)
Frightend - zmiana koloru i chaotyczne ruchy
Eaten - wraca do domku
"""

import pygame
import math
import CONST as const
from board import board as grid
from hero import CapMan as pacman

class Pinky(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.home.x = const.STARTING_POSITION_X
        self.home.y = const.STARTING_POSITION_Y
        self.position = self.image.get_rect(center = (self.home.x, self.home.y))
        self.direction = const.LEFT
        self.mode = "SCATTER"
        self.speed = const.PINKY_SPEED
        self.angle = 0
        self.image = pygame.image.load("cap_man_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(45,45))
    def get_target(self, pacman):
        if self.mode == "SCATTER": return 0, 0
        if self.mode == "FRIGHTEND": return -1, -1
        if self.mode == "EATEN": return self.home.x, self.home.y
        target_x = pacman.rect.x + (4*pacman.capman_direction)
        target_y = pacman.rect.y + (4*pacman.capman_direction)
        return target_x, target_y
    def update(self, pacman):
        target_x, target_y = self.get_target(self, pacman)
        if self.mode == "CHASE" or self.mode == "SCATTER": self.speed = const.PINKY_SPEED
        elif self.mode == "FRIGHTEND": self.speed = const.FRIGHTENED_SPEED
        elif self.mode == "EATEN": self.speed = const.EATEN_SPEED
        #move towards the target based on manhattan distance
    