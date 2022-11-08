import sys
sys.path.append("main_classes")
sys.path.append("art")
from display import BackGround, Display, display_text
from player import Player
import pygame

class Game(Display, BackGround):
    def __init__(self):

        Display.__init__(self)
        BackGround.__init__(self)
        #self.player = Player(self.screen, self.WIDTH, self.HEIGHT, 1, 1, acceleration, [0, 0], animation, can_crouch=False, jump_amount=1, jump_strength, blow_direction=[0, 1], position: list)

        
        self.current_level = 1
        self.max_level = 5
        self.stop = True
        self.main_menu = True
        self.level_menu = False
        self.pause = False
        self.game_over = False
        self.select_player_menu = False 


        


    def in_game_loop(self):
        if self.stop:
            self.display_menues()
            
        else:
            pass
            


        