from msilib.schema import Error
import pygame


class Animations:
    def __init__(self, animation_dict: dict):

        self.animation_dict = animation_dict
        for i in animation_dict:
            self.surf = self.animation_dict[i][0]
            break


        self.animation_index = 0


    def execute_animation(self, animation: list, animation_speed, back_and_forth=False):
        # Picture changes for every whole integer the animation index changes,
        # and animation index changes with animation speed every frame
        if not back_and_forth:
            self.animation_index += animation_speed
            if int(self.animation_index) >= len(animation):
                self.animation_index = 0
            self.surf = animation[int(self.animation_index)]
        else:
            long_animation = animation + animation[::-1][1:-1]
            if int(self.animation_index) >= len(long_animation):
                self.animation_index = 0
            self.surf = animation[int(self.animation_index)]
    






