
import pygame
from game import Game


class Main(Game):
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Hans game")
        hans_icon = pygame.image.load("art\general_art\general_hans_art\hans_face.png")
        pygame.display.set_icon(hans_icon)
        self.clock = pygame.time.Clock()

        
        Game.__init__(self) # Game mecanics to be initialised


        

    def loop(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))
            self.display_background()

            self.in_game_loop() # Game mecanics to loop

            pygame.display.update()
            pygame.display.flip()

            self.clock.tick(60)


if __name__ == "__main__":
    runn = Main()
    runn.loop()
