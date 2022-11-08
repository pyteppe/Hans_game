import pygame
import os

def importing_image_animations(dir_path:str):
    
    raw_path = r'{}'.format(dir_path)
    count = 0
    animation = []
    for root_dir, cur_dir, files in os.walk(raw_path):
        for i in files:
            animation.append(pygame.image.load(root_dir+ "/" + i))
    return animation
    
    