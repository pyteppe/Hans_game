from msilib.schema import Error
import sys
sys.path.append("classes")
sys.path.append("art")

import pygame
from only_once import OnlyOnce
from bindings import PlayerBindings
from general import General
from ground import Ground
from abilities import Crouch, Jump, Blow
from animations import Animations, ExecuteAnimation


class Player(General, Animations, pygame.sprite.Sprite, Crouch, Jump, Blow, PlayerBindings, ExecuteAnimation):
    def __init__(self, screen, WIDTH, HEIGHT, animations, ground, life_amount, max_life, acceleration: list, velocity: list, can_crouch: bool, jump_amount: int, jump_strength, position_top_left: tuple, person=None):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.animations = animations
        self.dt = 0

        General.__init__(self, life_amount, max_life, acceleration, velocity)

        ExecuteAnimation.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        # Abilities:
        Crouch.__init__(self, can_crouch)
        Jump.__init__(self, jump_amount, jump_strength)
        Blow.__init__(self)
        PlayerBindings.__init__(self)

        self.ground = ground
        self.tuching_ground = True

        self.update_player = True

        if person == None:
            self.animation_dict = self.animations.empty_player
        else:
            self.animation_dict = self.animations.all_player_animation_dicts_list[person]
        self.image = self.animations.empty_player["running"][0]
        self.rect = self.image.get_rect(topleft=position_top_left)
        self.current_animation = self.animation_dict["running"]
        

        # Things to do only once
        self.only_jump_once = OnlyOnce()

    

    def update(self, ground, dt):
        self.ground = ground
        self.dt = dt

        self.input()
        self.execute_movement()

        # Change animation
        
        self.execute_animation(self.current_animation, 5, True)
        self.display_player_life_bar(120, 20)


        self.tuching_ground = self.rect.bottom >= self.ground.rect.top # Must be after self.execute_movement() 
        if self.tuching_ground:
            self.when_tuching_ground()
        

        self.screen.blit(self.image, self.rect)

        if self.lives <= 0:
            self.lives = 0
            self.update_player = False
            return


    def input(self):
        keys = pygame.key.get_pressed()
        if self.only_jump_once.do_once(any([keys[i] for i in self.bindings_dict["jump"]])):
            if self.current_jump_amount > 0:
                self.execute_jump(self.ground)

        
        if any([keys[i] for i in self.bindings_dict["crouch"]]):
            if self.can_crouch and self.tuching_ground:
                self.execute_crouch()
        
    

    def when_tuching_ground(self):
        self.velocity = [0, 0]
        self.rect.bottom = self.ground.rect.top

        self.only_jump_once.done = False
        self.current_jump_amount = self.max_jump_amount

    
    def remake_after_restart(self, max_level, person, left_coordinate, lifebar_top_left):
        if person == None:
            self.update_player = False
            self.animation_dict = None
        else:
            self.update_player = True
            self.animation_dict = self.animations.all_player_animation_dicts_list[person]
            self.current_animation = self.animation_dict["running"]
        
            self.rect.bottomleft = (left_coordinate, self.ground.rect.top)
            self.velocity = [0, 0]

            self.execute_movement(just_move_pos=True)
            
            self.lives = self.max_lives
            self.player_top_left_lifebar = lifebar_top_left

            # Bars

            # Må legge til fleire evner
            if max_level > 1:
                self.can_crouch = True

                if max_level > 2:
                    self.max_jump_amount = 2
        
    

    





import time
class Main():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animastions = Animations((self.WIDTH, self.HEIGHT))


        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animastions, [-100, 0])
        self.player = Player(self.screen, self.WIDTH, self.HEIGHT, self.animastions, self.ground, 1, 1, [0, 100], [0, 0], True, 3, 800, (200, 200), person=0)


    def loop(self):
        running = True
        previous_time = time.time()
        while running:
            self.dt = time.time()-previous_time
            previous_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))

            self.player.update(ground=self.ground, dt=self.dt)
            self.ground.update_ground(self.dt)
            

            pygame.display.update()

            pygame.display.flip()


if __name__ == "__main__":
    runn = Main()
    runn.loop()
        


