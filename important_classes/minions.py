import pygame
import sys
sys.path.append("art")
sys.path.append("classes")
from animations import Animations, ExecuteAnimation
from general import General
from ground import Ground
from random import randint, choice
from timer import Timer





class Minions(pygame.sprite.Sprite, General, ExecuteAnimation):
    def __init__(self, screen, WIDTH, HEIGHT, life_amount, max_life, velocity, acceleration, animation_speed, botom_left_coordinate, animation_instance, minion):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen

        pygame.sprite.Sprite.__init__(self)
        General.__init__(self, life_amount, max_life, acceleration, velocity)
        ExecuteAnimation.__init__(self)
        self.animation_instance = animation_instance


        self.animation_types = [i for i in self.animation_dict]
        self.image = list(self.animation_dict.values())[0][0]
        self.rect = self.image.get_rect(bottomleft=botom_left_coordinate)

        self.current_animation = self.animation_dict[self.animation_types[0]]
        self.animation_speed = animation_speed


    def update(self, ground, dt):
        self.ground = ground
        self.dt = dt

        if __name__=="__main__":
            if self.rect.left < 0:
                self.rect.right = self.WIDTH
                self.execute_movement(just_move_pos=True)

        self.spesific_minion_update()
        self.execute_movement()
        if self.lives < self.max_lives:
            self.display_normal_life_bar(30, 10)

        # Must see what it is doing and change rect and animation list accordingly
        self.execute_animation(self.current_animation, self.animation_speed)
        
        

class DavidMinions(Minions):
    def __init__(self, screen, WIDTH, HEIGHT, animation_instance):
        self.animation_dict = animation_instance.all_minion_animation_dicts_list[0]
        super().__init__(screen, WIDTH, HEIGHT, life_amount=0.5, max_life=1, velocity=[-300, 0], acceleration=[0, 0], animation_speed=3, botom_left_coordinate=(randint(WIDTH*1.25, WIDTH*1.38), HEIGHT/4*3+40), animation_instance=animation_instance, minion=0)

    def spesific_minion_update(self):
        pass
        

class ThomasMinions(Minions):
    def __init__(self, screen, WIDTH, HEIGHT, animation_instance):
        self.animation_dict = animation_instance.all_minion_animation_dicts_list[1]
        super().__init__(screen, WIDTH, HEIGHT, life_amount=1, max_life=1, velocity=[-300, 0], acceleration=[0, 0], animation_speed=5, botom_left_coordinate=(randint(WIDTH*1.25, WIDTH*1.38), choice([HEIGHT*0.5, HEIGHT*0.65])), animation_instance=animation_instance, minion=1)

    def spesific_minion_update(self):
        pass




import time
class Main():
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 500
        self.dt = 0
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animations = Animations((self.WIDTH, self.HEIGHT))
        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animations, [-50, 0])

        self.david_minions = DavidMinions(self.screen, self.WIDTH, self.HEIGHT, self.animations)
        self.thomas_minion = ThomasMinions(self.screen, self.WIDTH, self.HEIGHT, self.animations)
        self.minion_group = pygame.sprite.Group()
        self.minion_group.add(self.david_minions)
        self.minion_group.add(self.thomas_minion)
        self.start_time = time.time()


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
            self.ground.update_ground(self.dt)

            
            self.minion_group.update(self.ground, self.dt)
            self.minion_group.draw(self.screen)

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(200)
if __name__ == "__main__":
    runn = Main()
    runn.loop()
        
