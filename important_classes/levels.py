import pygame
import random
import sys
sys.path.append("classes")
sys.path.append("art")
from animations import Animations
from levels_general import LevelsGeneral
from boss import DavidBoss, ThomasBoss
from minions import DavidMinions, ThomasMinions
from only_once import OnlyOnce
from timer import Timer, Timer2

class Levels(LevelsGeneral):
    def __init__(self, current_level, max_level):
        LevelsGeneral.__init__(self)

        self.current_level = current_level
        self.max_level = max_level

        # timer
        self.spawn_minion_level_1 = Timer(1)
        self.spawn_minion_level_2 = Timer(1)

        

    def update_level_1(self):
        if self.spawn_minion_level_1.time_it(self.dt):
            self.all_minions_group.add(DavidMinions(self.screen, self.WIDTH, self.HEIGHT, animation_instance=self.animations))

        self.skip_to_boss_level(5)
        self.update_obstacle_sprites()
        self.update_player_sprites()
        self.all_minions_group.draw(self.screen)
        self.all_minions_group.update(ground=self.ground, dt=self.dt) 

              

    def update_level_2(self):
        if self.spawn_minion_level_2.time_it(self.dt):
            if random.random() > 0.4:
                self.all_minions_group.add(ThomasMinions(self.screen, self.WIDTH, self.HEIGHT, animation_instance=self.animations))
            else:
                self.all_minions_group.add(DavidMinions(self.screen, self.WIDTH, self.HEIGHT, animation_instance=self.animations))
        
        self.skip_to_boss_level(20)
        self.update_obstacle_sprites()
        self.update_player_sprites()
        self.all_minions_group.draw(self.screen)
        self.all_minions_group.update(ground=self.ground, dt=self.dt) 


    def update_boss_level_david(self):
        if self.initiate_boss_prepairing:
            self.all_boss_group.add(DavidBoss(self.screen, self.animations, (self.WIDTH, self.HEIGHT), botom_left_pos=(self.WIDTH, self.ground.rect.top)))  
            self.initiate_boss_prepairing = False
        self.update_boss_sprites()
        self.update_player_sprites()
        self.all_boss_group.update(self.dt, self.ground)
        self.all_boss_group.draw(self.screen)
        

        


    def update_level(self):
        
        if self.current_level == 1:
            self.update_level_1()
        elif self.current_level == 1.5:
            self.update_boss_level_david()
        elif self.current_level == 2:
            self.update_level_2()
    

        