import sys
sys.path.append("classes")
from only_once import OnlyOnce
import pygame
from boss import DavidBoss, ThomasBoss
from minions import DavidMinions, ThomasMinions

class LevelsGeneral:
    def __init__(self):
        # Things to only do once
        self.only_get_damaged_from_minion_once = [OnlyOnce() for _ in range(3)] # so that it happens to all players
        self.only_get_damaged_from_boss_once = [OnlyOnce() for _ in range(3)]
        self.only_land_on_david_boss_once = [OnlyOnce() for _ in range(3)]
        self.initiate_boss_prepairing = True # So that every time boss level starts this will be sett to false after first frame

        # Level score
        self.level_score_list = [0, 0] # Legg til etter kvart som eg legg til fleire level
        self.initial_level_score_list = self.level_score_list.copy()



    def start_current_level_func(self):
        # Player    
        for n, player in enumerate(self.player_group):
            if len(self.chosen_player_animation_list) >= n+1:
                player.remake_after_restart(max_level=self.max_level, person=self.chosen_player_animation_list[n], left_coordinate=-150*n**2+250*n+120, lifebar_top_left=(self.WIDTH*1/40, self.HEIGHT*1/25+n*30))
            else:
                player.remake_after_restart(max_level=None, person=None, left_coordinate=None, lifebar_top_left=None)
        
        self.all_minions_group.empty() # Clears mobs
        self.all_boss_group.empty()

        if self.current_level - int(self.current_level) == 0:
            self.level_score_list[int(self.current_level)-1] = 0
        else:
            self.initiate_boss_prepairing = True

        #reset boss

        self.start_current_level = False
        self.start_next_level = False
    
    def start_next_level_func(self):
        self.all_minions_group.empty() # Clears mobs
        self.all_boss_group.empty() # Clear boss
        print("start next level")
        self.start_next_level = False
    
    def skip_to_boss_level(self, score_to_reach):
        if self.level_score_list[int(self.current_level)-1] >= score_to_reach:
            if self.initiate_boss_prepairing:
                self.initiate_boss_prepairing = False
                for minions in self.all_minions_group:
                    minions.current_animation = minions.turn_around(minions.current_animation)
                    

            for minion in self.all_minions_group:

                minion.velocity = [600, 0]

                if minion.rect.left > self.WIDTH:
                    minion.kill()

            if len(self.all_minions_group) == 0:
                self.start_next_level = True
                self.current_level += 0.5
                self.initiate_boss_prepairing = True


    def player_lands_on_top(self, thing, do_once=False, known_player=None, player_number=None): # Can change so that it does it no mater the speed
            if known_player and do_once:
                return self.only_land_on_david_boss_once[player_number].do_once(thing.rect.top - 20 < known_player.rect.bottom < thing.rect.top and thing.rect.left + 10 < known_player.rect.right and thing.rect.right > known_player.rect.left and known_player.velocity[1] > 0)
            elif known_player:
                return thing.rect.top - 20 < known_player.rect.bottom < thing.rect.top and thing.rect.left + 10 < known_player.rect.right and thing.rect.right > known_player.rect.left and known_player.velocity[1] > 0

            for n, player in enumerate(self.player_group):
                if do_once:
                    return self.only_land_on_david_boss_once[n].do_once(thing.rect.top - 20 < player.rect.bottom < thing.rect.top and thing.rect.left + 10 < player.rect.right and thing.rect.right > player.rect.left and player.velocity[1] > 0)
                else:
                    return thing.rect.top - 20 < player.rect.bottom < thing.rect.top and thing.rect.left + 10 < player.rect.right and thing.rect.right > player.rect.left and player.velocity[1] > 0
                
    
    def update_obstacle_sprites(self):
        for minion in self.all_minions_group:
            if minion.rect.right < 0:
                minion.kill()
            for player_nr, player in enumerate(self.player_group):
                if self.player_lands_on_top(thing=minion, do_once=True, known_player=player, player_number=player_nr):
                    if isinstance(minion, DavidMinions):
                        player.velocity[1] = -250
                        minion.kill()
                        self.level_score_list[int(self.current_level)-1] += 1
                    elif isinstance(minion, ThomasMinions):
                        minion.kill()
                        player.velocity[1] = -250
                        if minion.rect.bottom == self.HEIGHT*0.65:
                            self.level_score_list[int(self.current_level)-1] += 2
                        elif minion.rect.bottom == self.HEIGHT*0.5:
                            self.level_score_list[int(self.current_level)-1] += 3
                        else:
                            print("Thomas er verken høgt oppe eller lavt nede")
    
    def update_boss_sprites(self):
        for boss in self.all_boss_group:
            for n, player in enumerate(self.player_group):
                if self.player_lands_on_top(boss, do_once=True, known_player=player, player_number=n):
                    if isinstance(boss, DavidBoss):
                        player.velocity[1] = -1000
                        boss.lives -= 1
                        boss.rect.right = self.WIDTH
                        boss.execute_movement(just_move_pos=True)

    def update_player_sprites(self):
        all_players_are_dead = True # So that if i go trough all players and none converts this value, all are dead 

        for n, player in enumerate(self.player_group):
            if player.update_player:
                all_players_are_dead = False
                if self.only_get_damaged_from_minion_once[n].do_once(pygame.sprite.spritecollide(player, self.all_minions_group, False)):
                    player.lives -= 1
                if self.only_get_damaged_from_boss_once[n].do_once(pygame.sprite.spritecollide(player, self.all_boss_group, False)):
                    player.lives -= 1

        if all_players_are_dead:
            self.stop = True
            self.game_over = True