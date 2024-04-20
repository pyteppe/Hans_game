import sys
sys.path.append("classes")
sys.path.append("art")

import pygame
from general import General
from only_once import OnlyOnce
from ground import Ground
from abilities import Crouch, Jump, Blow
from animations import Animations, ExecuteAnimation


class GeneralBoss(pygame.sprite.Sprite, General, ExecuteAnimation):
    def __init__(self, screen, screen_size, name: str, life_amount, max_life, initial_velocity:list, botom_left_pos, animation_speed):
        self.name = name
        self.screen = screen
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]
        self.animation_speed = animation_speed

        pygame.sprite.Sprite.__init__(self)
        General.__init__(self, life_amount=life_amount, max_life=max_life, acceleration=[0, 0], velocity=initial_velocity)
        ExecuteAnimation.__init__(self)

        self.image = self.current_animation[0]
        self.rect = self.image.get_rect(bottomleft=botom_left_pos)


    
    def update(self, dt, ground):
        self.dt = dt
        self.ground = ground
        self.spesific_boss_update()
        self.execute_movement()
        self.execute_animation(self.current_animation, self.animation_speed)
        self.display_boss_life_bar(500, 10)




class DavidBoss(GeneralBoss):
    def __init__(self, screen, animations_instance: Animations, screen_size, botom_left_pos):
        self.animation_dict = animations_instance.all_boss_amination_dicts_list[0]
        self.boss_size = animations_instance.david_bos_size
        self.current_animation = self.animation_dict["crawling"]
        GeneralBoss.__init__(self, screen, screen_size, "David", life_amount=3, max_life=3, initial_velocity=[0, 0], botom_left_pos=botom_left_pos, animation_speed=1)
        self.do_approach = True

    def approach(self):
        if self.move_to(right=self.WIDTH, centery=self.ground.rect.top, speed=60):
            self.velocity = [-300, 0]


            self.do_approach = False

        

    def spesific_boss_update(self):
        # (x = a y³ + b)=>(y=((x-b)/a)**(1/3)) brukte denne likninga y er animasjon og x er fart, a er konstant og b er bakkefarta
        self.animation_speed = 1/5*(25)**(1/3)*(-self.velocity[0]+self.ground.velocity[0])**(1/3)
        if isinstance(self.animation_speed, complex):
            self.animation_speed = -abs(self.animation_speed)

        

        if self.do_approach:
            self.approach()


class ThomasBoss(GeneralBoss):
    def __init__(self, screen, animations_instance: Animations):
        self.animation_dict = animations_instance.all_boss_amination_dicts_list[1]
        self.boss_size = animations_instance.thomas_bos_size
        self.current_animation = self.animation_dict["flying"]
        GeneralBoss.__init__(self, screen, "Thomas", life_amount=3, max_life=3)
    
    def approach(self):
        pass
    
    def spesific_boss_update(self):
        pass



























import time
class Main():
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.animations = Animations(screen_size=(self.WIDTH, self.HEIGHT))
        self.ground = Ground(self.screen, (self.WIDTH, self.HEIGHT), self.animations, [-100, 0])
        self.all_boss_group = pygame.sprite.Group()

        self.all_boss_group.add(DavidBoss(self.screen, self.animations, (self.WIDTH, self.HEIGHT), botom_left_pos=(self.WIDTH, self.ground.rect.top+self.animations.david_bos_size[1]/2)))
        

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


            self.all_boss_group.update(self.dt, self.ground)
            self.all_boss_group.draw(self.screen)

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == "__main__":
    runn = Main()
    runn.loop()