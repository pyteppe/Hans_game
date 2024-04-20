import sys
sys.path.append("important_classes")
sys.path.append("classes")
sys.path.append("art")
from levels import Levels
from display import BackGround, Display, display_text
from animations import Animations, ExecuteAnimation
from bindings import GlobalBindings
from player import Player
from ground import Ground
from only_once import OnlyOnce
import pygame

class Game(Display, BackGround, GlobalBindings, Levels, ExecuteAnimation):
    def __init__(self):

        self.animations = Animations(screen_size=(self.WIDTH, self.HEIGHT))
        ExecuteAnimation.__init__(self)
        Display.__init__(self)
        BackGround.__init__(self)
        GlobalBindings.__init__(self)
        Levels.__init__(self, current_level=1, max_level=3)

        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animations, [-200, 0])

        self.display_in_game_background()
        self.ground.update_ground(self.dt)

        # Pygame Groups
        self.all_minions_group = pygame.sprite.Group() 
        self.all_boss_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        for _ in range(3):
            self.player_group.add(Player(self.screen, self.WIDTH, self.HEIGHT, self.animations, self.ground, life_amount=2, max_life=2, acceleration=[0, 3000], velocity=[0, 0], can_crouch=False, jump_amount=1, jump_strength=800, position_top_left=(200, 200)))
        
        
        # Menu states
        self.stop = True
        self.main_menu = True
        self.level_menu = False
        self.pause = False
        self.game_over = False
        self.select_player_menu = False 
        self.select_player_animation_menu = False

        self.start_current_level = False

        # Things to only do once
        


    def in_game_loop(self):
        self.listen_for_key_strokes()

        if self.stop:
            self.display_menues(dt=self.dt)
            
        else:
            self.display_in_game_background()
            self.ground.update_ground(self.dt)
            
            if self.start_current_level:
                self.start_current_level_func()
            elif self.start_next_level:
                self.start_next_level_func()
            
            # Updating sprites
            for player in self.player_group:
                if player.update_player:
                    player.update(ground=self.ground, dt=self.dt)
            
            
            self.update_level()



            
            


        