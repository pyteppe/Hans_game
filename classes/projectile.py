import pygame
import sys
sys.path.append("art")
from animations import Animations
from general import General
from importing_image import importing_image_animations

    
    

class Projectile(pygame.sprite.Sprite, Animations, General):
    def __init__(self, screen, velocity: list, acceleration: list, center_pos: tuple, size:tuple, animation_images_path: str, animation_speed, hostile_for_player=False, acceleration_acceleration=[0, 0], life_amount=1, max_life=1):

        # Movement
        
        self.animation_list = importing_image_animations(animation_images_path)
        for n, i in enumerate(self.animation_list):
            self.animation_list[n] = pygame.transform.scale(i, size)
        self.animation_speed = animation_speed
        
        self.rect = self.animation_list[0].get_rect(center=center_pos)
        self.screen = screen
        self.hostile_for_player = hostile_for_player

        # Initialise
        Animations.__init__(self, {"projectile": self.animation_list})
        pygame.sprite.Sprite.__init__(self)
        General.__init__(self, life_amount, max_life, acceleration, velocity, acceleration_acceleration=acceleration_acceleration)


    def draw_and_update(self, stop):
        if not stop:
            self.move_projectile()
            self.execute_animation(self.animation_list, self.animation_speed)
        self.screen.blit(self.surf, self.rect)
        




class Wind(Projectile):
    def __init__(self, screen, speed: list, acceleration: list, center_pos: tuple, size:tuple, hostile_for_player, acceleration_acceleration=[0, 0]):
        Projectile.__init__(self, screen, speed, acceleration,center_pos, size, "art\general_art\Projectile/tornado", 0.5, hostile_for_player=hostile_for_player, acceleration_acceleration=acceleration_acceleration)
        
        
        


        
        

class LocalMain():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.wind = Wind(self.screen, [2, 1], [0.15, 0], (self.WIDTH/2, self.HEIGHT/2), (40, 50), False, acceleration_acceleration=[-0.002, 0])
        self.wind2 = Wind(self.screen, [-2, -1], [0, 0], (self.WIDTH/2, self.HEIGHT/2), (40, 50), False)
        

    def loop(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))

            self.wind.draw_and_update(False)
            self.wind2.draw_and_update(False)




            pygame.display.update()

            pygame.display.flip()
            

            self.clock.tick(60)


if __name__ == "__main__":
    runn = LocalMain()
    runn.loop()
        