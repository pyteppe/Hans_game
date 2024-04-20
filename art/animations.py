from msilib.schema import Error
import pygame
from animation_storage import StoredAnimationDictionaries


class Animations(StoredAnimationDictionaries):
    def __init__(self, screen_size=None):
        if screen_size:
            self.WIDTH = screen_size[0]
            self.HEIGHT = screen_size[1]
        self.animation_index = 0

        # Geting stored animations
        StoredAnimationDictionaries.__init__(self)

    def execute_animation(self, animation: list, animation_speed, back_and_forth=False, dt=None):
        if dt != None:
            self.dt = dt
        self.animation_index += animation_speed*self.dt
        if not back_and_forth:
            if int(self.animation_index) >= len(animation):
                self.animation_index = 0
            self.image = animation[int(self.animation_index)]
        else:
            long_animation = animation + animation[::-1][1:-1]
            if int(self.animation_index) >= len(long_animation):
                self.animation_index = 0
            self.image = long_animation[int(self.animation_index)]




class ExecuteAnimation:
    def __init__(self):
        self.animation_index = 0
        
    def execute_animation(self, animation: list, animation_speed, back_and_forth=False, dt=None):
        if dt != None:
            self.dt = dt
        self.animation_index += animation_speed*self.dt
        if not back_and_forth:
            if int(self.animation_index) >= len(animation):
                self.animation_index = 0
            elif self.animation_index < 0:
                self.animation_index = len(animation)-0.0000000000001
            self.image = animation[int(self.animation_index)]

        else:
            long_animation = animation + animation[::-1][1:-1]
            if int(self.animation_index) >= len(long_animation):
                self.animation_index = 0
            elif self.animation_index < 0:
                self.animation_index = len(long_animation)-0.0000000000001
            self.image = long_animation[int(self.animation_index)]






