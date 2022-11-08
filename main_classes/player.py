from msilib.schema import Error
import sys
sys.path.append("classes")
sys.path.append("art")

import pygame
from bindings import Bindings
from general import General
from abilities import Crouch, Jump, Blow
from animations import Animations


class Player(General, Animations, pygame.sprite.Sprite, Crouch, Jump, Blow, Bindings):
    def __init__(self, screen, WIDTH, HEIGHT, life_amount, max_life, acceleration: list, velocity: list, animation: dict, can_crouch: bool, jump_amount: int, jump_strength, blow_direction: list, position: list):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        General.__init__(self, life_amount, max_life, acceleration, velocity)


        Animations.__init__(self, animation)
        pygame.sprite.Sprite.__init__(self)
        # Abilities:
        Crouch.__init__(self, can_crouch)
        Jump.__init__(self, jump_amount, jump_strength)
        Blow.__init__(self, blow_direction)
        Bindings.__init__(self)
        self.pos = position
        


    def input(self):
        keys = pygame.key.get_pressed()
        for jumping in self.bindings_dict["jump"]:
            if keys[jumping]:
                if not self.jump_button_curently_down:
                    self.execute_jump()
                self.jump_button_curently_down = True
            elif not any([keys[i] for i in self.bindings_dict["jump"]]):
                self.jump_button_curently_down = False
        for crouching in self.bindings_dict["crouch"]:
            if keys[crouching]:
                print("crouch")
        
    

    def animation_for_ocasiones():
        pass







class Main():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = Player(self.screen, self.WIDTH, self.HEIGHT, 1, 1, [0, 0], [0, 0], {2: [2, 3]}, False, 1, 9, [1, 0], (200, 200))
        

    def loop(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))

            self.player.input()
            self.player.display_player_life_bar(120, 20)
            

            pygame.display.update()

            pygame.display.flip()
            

            self.clock.tick(60)


if __name__ == "__main__":
    runn = Main()
    runn.loop()
        


