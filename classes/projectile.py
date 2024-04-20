import pygame
import sys
sys.path.append("art")
from animations import Animations
from general import General
from animations import Animations

    
    

class Projectile(pygame.sprite.Sprite, Animations, General):
    def __init__(self, screen, velocity: list, acceleration: list, center_pos: tuple, animation_dict: dict, animation_speed, hostile_for_player=False, acceleration_acceleration=[0, 0], life_amount=1, max_life=1):
        self.screen = screen
        
        self.animation_dict = animation_dict
        self.normal_animation_list = self.animation_dict["normal"]
        self.animation_speed = animation_speed

        self.hostile_for_player = hostile_for_player

        self.image = self.normal_animation_list[0]
        self.rect = self.image.get_rect(center=center_pos)

        # Initialise
        pygame.sprite.Sprite.__init__(self)
        General.__init__(self, life_amount, max_life, acceleration, velocity, acceleration_acceleration=acceleration_acceleration)


    def update(self, dt):
        self.dt = dt
        self.execute_movement(desimal_movement=True)
        self.execute_animation(self.normal_animation_list, self.animation_speed)
        self.screen.blit(self.image, self.rect)
        




class Wind(Projectile, Animations):
    def __init__(self, screen, screen_size, animation_speed: list, velocity: list, acceleration: list, center_pos: tuple, hostile_for_player, acceleration_acceleration: list=[0, 0]):
        Animations.__init__(self, screen_size)
        Projectile.__init__(self, screen, velocity, acceleration, center_pos, self.wind_animation_dict, animation_speed, hostile_for_player=hostile_for_player, acceleration_acceleration=acceleration_acceleration)
        
        
        


        
        
import time
class LocalMain():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.wind = Wind(self.screen, (self.WIDTH, self.HEIGHT), 20, [-200, 100], [0, 0], (self.WIDTH/2, self.HEIGHT/2), hostile_for_player=False)
        self.wind2 = Wind(self.screen, (self.WIDTH, self.HEIGHT), 20, [-100, 100], [0, 0], (self.WIDTH/2, self.HEIGHT/2), hostile_for_player=False)
        

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

            self.wind.update(self.dt)
            self.wind2.update(self.dt)




            pygame.display.update()

            pygame.display.flip()
            

            self.clock.tick(60)


if __name__ == "__main__":
    runn = LocalMain()
    runn.loop()
        