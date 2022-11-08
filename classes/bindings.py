import pygame

class Bindings:
    def __init__(self):
        self.bindings_dict = {"jump": [pygame.K_UP, pygame.K_SPACE], "crouch": [pygame.K_DOWN, pygame.K_LSHIFT, pygame.K_RSHIFT]}
    
    def change_binding(self):
        pass