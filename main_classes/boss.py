import sys
sys.path.append("classes")
sys.path.append("art")

import pygame
from general import General
from abilities import Crouch, Jump, Blow
from animations import Animations


class GeneralBoss(pygame.sprite.Sprite):
    def __init__(self, name: str):
        pygame.sprite.Sprite.__init__(self)

        self.name = name

        

