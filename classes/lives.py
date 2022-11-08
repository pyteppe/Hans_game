from msilib.schema import Error
import sys
sys.path.append("art")
from display import display_text, display_bar
import pygame

class Lives:
    def __init__(self, life_amount, max_life, top_color=(255, 0, 0), bottom_color=(114, 114, 114), bar_radius=4):
        if max_life < life_amount:
            print(self.__class__.__name__)
            raise Error(f"Max life is bigger than life amount in class mentioned above error")
        
        self.max_lives = max_life
        self.lives = life_amount

        self.top_color_life_bar = top_color
        self.bottom_color_life_bar = bottom_color
        self.life_bar_radius = bar_radius

    def uppdate_life(self, life_taken=0, life_given=0):
        self.lives += life_given
        self.lives -= life_taken
        if self.lives > self.max_lives:
            self.lives = self.max_lives
        elif self.lives < 0:
            self.lives = 0

    def display_normal_life_bar(self, width, height, radius=None, new_top_left_pos=None, top_color=None, bottom_color=None):
        self.uppdate_life()
        top_left_pos = (self.rect.left + self.rect.width/2-width/2, self.rect.top-height*3/2)
        
        if bottom_color:
            self.bottom_color = bottom_color
        if top_color:
            self.top_color_life_bar = top_color
        if new_top_left_pos:
            top_left_pos = new_top_left_pos
        if radius:
            self.life_bar_radius = radius

        display_bar(self.screen, width, height, self.lives, self.max_lives, self.life_bar_radius, top_left_pos, self.top_color_life_bar, self.bottom_color_life_bar)


    def display_boss_life_bar(self, width, height, radius=None, new_top_left_pos=None, top_color=None, bottom_color=None):
        self.uppdate_life()
        top_left_pos = (self.WIDTH/2-width/2, self.HEIGHT*1/12)

        if bottom_color:
            self.bottom_color = bottom_color
        if top_color:
            self.top_color_life_bar = top_color
        if new_top_left_pos:
            top_left_pos = new_top_left_pos
        if radius:
            self.life_bar_radius = radius

        display_bar(self.screen, width, height, self.lives, self.max_lives, self.life_bar_radius, top_left_pos, self.top_color_life_bar, self.bottom_color_life_bar)
        center_pos_text = (self.WIDTH/2, self.HEIGHT*1/25)
        display_text(self.screen, self.name, center_pos_text, font=None, text_size=50, text_color=(0, 0, 0))


    def display_player_life_bar(self, width, height, radius=None, new_top_left_pos=None, top_color=None, bottom_color=None):
        self.uppdate_life()
        top_left_pos = (self.WIDTH*1/40, self.HEIGHT*1/25)

        if bottom_color:
            self.bottom_color = bottom_color
        if top_color:
            self.top_color_life_bar = top_color
        if new_top_left_pos:
            top_left_pos = new_top_left_pos
        if radius:
            self.life_bar_radius = radius

        display_bar(self.screen, width, height, self.lives, self.max_lives, self.life_bar_radius, top_left_pos, self.top_color_life_bar, self.bottom_color_life_bar)










class Jaaa(Lives):
    def __init__(self, screen, WIDTH, HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.name = "Thomas"
        self.surf = pygame.image.load("art\general_art\Projectile\spike\spike_2.jpg")
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.rect = self.surf.get_rect(topleft=(200, 200))
        
        super().__init__(500, 500, bar_radius=5)

    def damage(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.lives -= 3




class Main():
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 500

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.ja = Jaaa(self.screen, self.WIDTH, self.HEIGHT)

        

    def loop(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((200, 200, 200))

            self.screen.blit(self.ja.surf, self.ja.rect)
            self.ja.damage()

            self.ja.display_player_life_bar(120, 20)
            self.ja.display_normal_life_bar(40, 12)
            self.ja.display_boss_life_bar(400, 15)
            


            pygame.display.update()

            pygame.display.flip()
            

            self.clock.tick(60)


if __name__ == "__main__":
    runn = Main()
    runn.loop()





        