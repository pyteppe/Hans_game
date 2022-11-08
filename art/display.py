import pygame
from button import Button

class Display:
    def __init__(self):
        self.WIDTH = self.WIDTH
        self.HEIGHT = self.HEIGHT

        # Multiple use buttons
        self.back_to_main_menu_button = Button(self.screen, "<<", 50, 30, (self.WIDTH*1.1/8, self.HEIGHT*7/50))

        # Menu back_ground
        self.menu_back_ground_surf = pygame.image.load("art/back_ground/brown_ice_by_darkwood67.jpg")
        self.menu_back_ground_surf = pygame.transform.scale(self.menu_back_ground_surf, (self.WIDTH*3/4, self.HEIGHT*4/5))
        self.menu_back_ground_rect = self.menu_back_ground_surf.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))

        # Main menu
        self.levels_button = Button(self.screen, "Play", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*5/40, self.HEIGHT*1.4/5))
        self.select_player_button = Button(self.screen, "Select player", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*5/40, 200))

        # Level menu
        self.level_1 = Button(self.screen, "Level 1", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*1.3/5))
        self.level_1_boss = Button(self.screen, "David boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*1.8/5), text_size=18)
        self.level_2 = Button(self.screen, "Level 2", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*2.3/5))
        self.level_2_boss = Button(self.screen, "Thomas boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*2.8/5), text_size=18)
        self.level_3 = Button(self.screen, "Level 3", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*3.3/5))
        self.level_3_boss = Button(self.screen, "Jaran boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*3.8/5), text_size=18)

        self.level_4 = Button(self.screen, "Level 4", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*1.3/5))
        self.level_4_boss = Button(self.screen, "4 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*1.8/5), text_size=18)
        self.level_5 = Button(self.screen, "Level 5", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*2.3/5))
        self.level_5_boss = Button(self.screen, "5 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*2.8/5), text_size=18)
        self.level_6 = Button(self.screen, "Level 6", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*3.3/5))
        self.level_6_boss = Button(self.screen, "6 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*3.8/5), text_size=18)

        self.list_of_normal_level_buttons = [self.level_1, self.level_1_boss, self.level_2, self.level_2_boss,\
                                self.level_3, self.level_3_boss, self.level_4, self.level_4_boss, \
                                self.level_5, self.level_5_boss, self.level_6, self.level_6_boss]
        

        # Game over menu
        self.evil_hans_surf = pygame.image.load("art\general_art\general_hans_art\evil_hans.png")
        self.evil_hans_surf = pygame.transform.scale(self.evil_hans_surf, (self.WIDTH*1/4, self.HEIGHT*2/5))
        self.evil_hans_rect = self.evil_hans_surf.get_rect(center=(self.WIDTH*1/2, self.HEIGHT*1.2/5))
        self.game_over_main_menu_button = Button(self.screen, "Main menu", 140, 60, (self.WIDTH/4, self.HEIGHT*0.6), font=None, hover_color=(0, 0, 0), hover_text_color=(255, 0, 0))
        self.game_over_restart_button = Button(self.screen, "Restart", 140, 60, (self.WIDTH*0.55, self.HEIGHT*0.6), font=None, hover_color=(0, 0, 0), hover_text_color=(255, 0, 0))

        # Pause menu
        self.pause_main_menu_button = Button(self.screen, "Main menu", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*11/25))
        self.pause_restart_level = Button(self.screen, "Continue", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*1.4/5))

        # Select player menu
        self.move_to_right_player = Button(self.screen, ">", self.WIDTH*1/20, self.HEIGHT*3/50, (self.WIDTH*3/4, self.HEIGHT*47/100))
        self.move_to_left_player = Button(self.screen, "<", self.WIDTH*1/20, self.HEIGHT*3/50, (self.WIDTH*1/5, self.HEIGHT*47/100))
        self.player_to_show_in_select_player_menu = 0
        self.list_of_player_stand_animations = []

    def display_level_menu(self):
        self.screen.blit(self.menu_back_ground_surf, self.menu_back_ground_rect)
        display_text(self.screen, "Level Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.back_to_main_menu_button.draw_and_check_click():
            self.level_menu = False
            self.main_menu = True

        for n, button in enumerate(self.list_of_normal_level_buttons):
            if n+1 < 2*self.max_level:
                if button.draw_and_check_click():
                    self.current_level = (n)/2 + 1
                    self.level_menu = False
                    self.stop = False
            else:
                button.draw_disabled_button()
        if self.max_level >= 7:
            # Show secret button
            print("Show secret button")
    

    def display_main_menu(self):
        self.screen.blit(self.menu_back_ground_surf, self.menu_back_ground_rect)
        display_text(self.screen, "Main Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.levels_button.draw_and_check_click():
            self.main_menu = False
            self.level_menu = True
        if self.select_player_button.draw_and_check_click():
            self.main_menu = False
            self.select_player_menu = True


    def display_pause_menu(self):
        self.screen.blit(self.menu_back_ground_surf, self.menu_back_ground_rect)
        display_text(self.screen, "Pause", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.pause_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.pause = False
        if self.pause_restart_level.draw_and_check_click():
            self.pause = False
            self.stop = False


    def display_game_over_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.menu_back_ground_rect)
        display_text(self.screen, "You died", (self.WIDTH/2, self.HEIGHT/2), text_color=(255, 0, 0), font=None, text_size=60)
        self.screen.blit(self.evil_hans_surf, self.evil_hans_rect)
        if self.game_over_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.game_over = False
        if self.game_over_restart_button.draw_and_check_click():
            self.game_over = False
            self.stop = False
    
    def display_select_player_menu(self):
        self.screen.blit(self.menu_back_ground_surf, self.menu_back_ground_rect)
        display_text(self.screen, "Select your Player", (self.WIDTH/2, self.HEIGHT*9/50), text_color=(0, 0, 0), text_size=50)
        if self.back_to_main_menu_button.draw_and_check_click():
            self.select_player_menu = False
            self.main_menu = True
        if self.move_to_right_player.draw_and_check_click():
            if self.player_to_show_in_select_player_menu < len(self.list_of_player_stand_animations)-1:
                self.player_to_show_in_select_player_menu += 1
            else:
                self.player_to_show_in_select_player_menu = 0
        if self.move_to_left_player.draw_and_check_click():
            if self.player_to_show_in_select_player_menu > 0:
                self.player_to_show_in_select_player_menu -= 1
            else:
                self.player_to_show_in_select_player_menu = len(self.list_of_player_stand_animations)-1
        print(self.player_to_show_in_select_player_menu)


    def display_menues(self):
        if self.main_menu:
            self.display_main_menu()
        elif self.level_menu:
            self.display_level_menu()
        elif self.pause:
            self.display_pause_menu()
        elif self.game_over:
            self.display_game_over_menu()
        elif self.select_player_menu:
            self.display_select_player_menu()





class BackGround:
    def __init__(self):
        back_ground = pygame.image.load("art/back_ground/Snapchat-864863571.jpg")
        self.back_ground = pygame.transform.scale(back_ground, (self.WIDTH, self.HEIGHT))
        

    def display_background(self):
        self.screen.blit(self.back_ground, (0, 0))


def display_text(screen, text: str, center_pos: tuple, text_color=(255, 255, 255), font="art/font\Canterbury.ttf", text_size=30):
    text_font = pygame.font.Font(font, text_size)
    surf = text_font.render(text, True, text_color)
    rect = surf.get_rect(center=center_pos)
    screen.blit(surf, rect)


def display_bar(screen, width, height, curent, maximum, bar_radius, top_left_pos, top_color, bottom_color):
    bottom_rect = pygame.Rect(top_left_pos, (width, height))
    top_rect = pygame.Rect(top_left_pos, (width*curent/maximum, height))
    pygame.draw.rect(screen, bottom_color, bottom_rect, border_radius=bar_radius)
    pygame.draw.rect(screen, top_color, top_rect, border_radius=bar_radius) 
        

