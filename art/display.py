import pygame
import sys
sys.path.append("art")
from animations import Animations, ExecuteAnimation
from button import Button

class Display:
    def __init__(self):
        self.WIDTH = self.WIDTH
        self.HEIGHT = self.HEIGHT

        # Multiple use buttons
        self.back_button = Button(self.screen, "<<", 50, 30, (self.WIDTH*1.1/8, self.HEIGHT*7/50))

        # Menu back_ground
        self.animations.image = self.animations.menu_back_ground_dict["normal"][0]
        self.menu_back_ground_rect = self.animations.menu_back_ground_dict["normal"][0].get_rect(center=(self.WIDTH/2, self.HEIGHT/2))

        # Main menu
        self.levels_button = Button(self.screen, "Play", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*5/40, self.HEIGHT*1.4/5))
        self.player_amount_button = Button(self.screen, "Select player", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.4))

        # Level menu
        self.level_1_button = Button(self.screen, "Level 1", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*1.3/5))
        self.level_1_boss_button = Button(self.screen, "David boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*1.8/5), text_size=18)
        self.level_2_button = Button(self.screen, "Level 2", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*2.3/5))
        self.level_2_boss_button = Button(self.screen, "Thomas boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*2.8/5), text_size=18)
        self.level_3_button = Button(self.screen, "Level 3", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*1.5/8, self.HEIGHT*3.3/5))
        self.level_3_boss_button = Button(self.screen, "Jaran boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*1/4, self.HEIGHT*3.8/5), text_size=18)

        self.level_4_button = Button(self.screen, "Level 4", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*1.3/5))
        self.level_4_boss_button = Button(self.screen, "4 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*1.8/5), text_size=18)
        self.level_5_button = Button(self.screen, "Level 5", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*2.3/5))
        self.level_5_boss_button = Button(self.screen, "5 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*2.8/5), text_size=18)
        self.level_6_button = Button(self.screen, "Level 6", self.WIDTH*1.2/8, self.HEIGHT*4/50, (self.WIDTH*5/8, self.HEIGHT*3.3/5))
        self.level_6_boss_button = Button(self.screen, "6 boss", self.WIDTH/8, self.HEIGHT/20, (self.WIDTH*5.5/8, self.HEIGHT*3.8/5), text_size=18)

        self.list_of_normal_level_buttons = [self.level_1_button, self.level_1_boss_button, self.level_2_button, self.level_2_boss_button,\
                                            self.level_3_button, self.level_3_boss_button, self.level_4_button, self.level_4_boss_button, \
                                            self.level_5_button, self.level_5_boss_button, self.level_6_button, self.level_6_boss_button]
        

        # Game over menu
        self.evil_hans_image = pygame.image.load("art\general_art\general_hans_art\evil_hans.png")
        self.evil_hans_image = pygame.transform.scale(self.evil_hans_image, (self.WIDTH*1/4, self.HEIGHT*2/5))
        self.evil_hans_rect = self.evil_hans_image.get_rect(center=(self.WIDTH*1/2, self.HEIGHT*1.2/5))
        self.game_over_main_menu_button = Button(self.screen, "Main menu", self.WIDTH*0.175, self.HEIGHT*0.12, (self.WIDTH/4, self.HEIGHT*0.6), font=None, hover_color=(0, 0, 0), hover_text_color=(255, 0, 0))
        self.game_over_restart_button = Button(self.screen, "Restart", self.WIDTH*0.175, self.HEIGHT*0.12, (self.WIDTH*0.55, self.HEIGHT*0.6), font=None, hover_color=(0, 0, 0), hover_text_color=(255, 0, 0))

        # Pause menu
        self.pause_main_menu_button = Button(self.screen, "Main menu", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*0.44))
        self.pause_continue_level_button = Button(self.screen, "Continue", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*0.28))
        self.pause_restart_level_button = Button(self.screen, "Restart", self.WIDTH*1/5, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/10, self.HEIGHT*0.6))

        # Player amount menu
        self.select_player_buttons = [Button(self.screen, "Player 1", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.28))]
        self.add_player_button = Button(self.screen, "+", self.WIDTH*0.0625, self.HEIGHT*0.08, (self.WIDTH*0.75, self.HEIGHT*0.76), text_size=50)
        self.remove_player_button = Button(self.screen, "-", self.WIDTH*0.0625, self.HEIGHT*0.08, (self.WIDTH*0.75, self.HEIGHT*0.66), text_size=50)
        self.current_chosen_player_to_choose_animation = 0 # To know which player to give animation to

        # Select player animation menu
        self.move_to_right_player = Button(self.screen, ">", self.WIDTH*1/20, self.HEIGHT*3/50, (self.WIDTH*3/4, self.HEIGHT*47/100))
        self.move_to_left_player = Button(self.screen, "<", self.WIDTH*1/20, self.HEIGHT*3/50, (self.WIDTH*1/5, self.HEIGHT*47/100))
        self.player_to_show_in_select_player_menu = 0
        self.stand_animation = Animations(screen_size=(self.WIDTH, self.HEIGHT))
        self.animation_speed = 10
        self.player_stand_rect = self.stand_animation.all_player_animation_dicts_list[0]["standing"][0].get_rect(center=(self.WIDTH/2, self.HEIGHT/2))
        self.button_to_choose_player = [Button(self.screen, f"Choose {i}", self.WIDTH*1/4, self.HEIGHT*4/50, (self.WIDTH/2-self.WIDTH*1/8, self.HEIGHT*4/5))\
                                        for i in ["Hans", "David", "Thomas", "Jaran"]]
        self.chosen_player_animation_list = [0]
    
    def display_menu_background(self):
        if self.game_over:
            self.screen.blit(self.evil_hans_image, self.evil_hans_rect)
            #self.animations.execute_animation(self.stand_animation.menu_back_ground_dict["normal"])
            #self.screen.blit(self.animations.image, self.menu_back_ground_rect)
        else:
            self.execute_animation(self.stand_animation.menu_back_ground_dict["normal"], animation_speed=0.3, dt=self.dt)
            self.screen.blit(self.animations.image, self.menu_back_ground_rect)

    def display_level_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Level Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.back_button.draw_and_check_click():
            self.level_menu = False
            self.main_menu = True

        for n, button in enumerate(self.list_of_normal_level_buttons):
            if n+1 < 2*self.max_level:
                if button.draw_and_check_click():
                    self.current_level = (n)/2 + 1
                    self.level_menu = False
                    self.stop = False
                    self.start_current_level = True
            else:
                button.draw_disabled_button()
        if self.max_level >= 7:
            # Show secret button
            print("Show secret button")
    

    def display_main_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Main Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.levels_button.draw_and_check_click():
            self.main_menu = False
            self.level_menu = True
        if self.player_amount_button.draw_and_check_click():
            self.main_menu = False
            self.select_player_menu = True


    def display_pause_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Pause", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.pause_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.pause = False
        if self.pause_continue_level_button.draw_and_check_click():
            self.pause = False
            self.stop = False
        if self.pause_restart_level_button.draw_and_check_click():
            self.pause = False
            self.stop = False
            self.start_current_level = True


    def display_game_over_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.menu_back_ground_rect)
        display_text(self.screen, "You died", (self.WIDTH/2, self.HEIGHT/2), text_color=(255, 0, 0), font=None, text_size=60)
        self.display_menu_background()

        self.level_score_list = self.initial_level_score_list.copy()

        if self.game_over_main_menu_button.draw_and_check_click():
            self.main_menu = True
            self.game_over = False
        if self.game_over_restart_button.draw_and_check_click():
            self.game_over = False
            self.stop = False
            self.start_current_level = True
    
    def display_select_player_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Player Menu", (self.WIDTH/2, self.HEIGHT*9/50), text_size=50, text_color=(10, 10, 10))
        if self.back_button.draw_and_check_click():
            self.main_menu = True
            self.select_player_menu = False
        for number, player in enumerate(self.select_player_buttons):
            if player.draw_and_check_click():
                self.select_player_animation_menu = True
                self.select_player_menu = False
                self.current_chosen_player_to_choose_animation = number # To know which player to give animation

        if len(self.select_player_buttons) < 3 and self.add_player_button.draw_and_check_click():
            self.select_player_buttons.append(Button(self.screen, f"Player {len(self.select_player_buttons)+1}", self.WIDTH*5/20, self.HEIGHT*4/50, (self.WIDTH*0.375, self.HEIGHT*0.28+len(self.select_player_buttons)*self.HEIGHT*0.12)))
            self.chosen_player_animation_list.append(0)
        if len(self.select_player_buttons) > 1 and self.remove_player_button.draw_and_check_click():
            self.select_player_buttons.pop(-1)
            self.chosen_player_animation_list.pop(-1)



    def display_select_player_animation_menu(self):
        self.display_menu_background()
        display_text(self.screen, "Select your Animation", (self.WIDTH/2, self.HEIGHT*9/50), text_color=(0, 0, 0), text_size=50)
        if self.back_button.draw_and_check_click():
            self.select_player_menu = True
            self.select_player_animation_menu = False
        if self.move_to_right_player.draw_and_check_click():
            if self.player_to_show_in_select_player_menu < len(self.stand_animation.all_player_animation_dicts_list)-1:
                self.player_to_show_in_select_player_menu += 1
            else:
                self.player_to_show_in_select_player_menu = 0
        if self.move_to_left_player.draw_and_check_click():
            if self.player_to_show_in_select_player_menu > 0:
                self.player_to_show_in_select_player_menu -= 1
            else:
                self.player_to_show_in_select_player_menu = len(self.stand_animation.all_player_animation_dicts_list)-1
                
        self.stand_animation.execute_animation(self.stand_animation.all_player_animation_dicts_list[self.player_to_show_in_select_player_menu]["standing"], self.animation_speed, back_and_forth=True, dt=self.dt)
        self.screen.blit(self.stand_animation.image, self.player_stand_rect)
        if self.button_to_choose_player[self.player_to_show_in_select_player_menu].draw_and_check_click():
            self.chosen_player_animation_list[self.current_chosen_player_to_choose_animation] = self.player_to_show_in_select_player_menu

    def display_menues(self, dt):
        self.dt = dt
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
        elif self.select_player_animation_menu:
            self.display_select_player_animation_menu()





class BackGround(ExecuteAnimation):
    def __init__(self):
        ExecuteAnimation.__init__(self)

        self.in_game_background = Animations(screen_size=(self.WIDTH, self.HEIGHT))

        self.in_game_background.image = self.animations.in_game_background_dict["normal"][0]
    
    def display_in_game_background(self):
        self.execute_animation(self.animations.in_game_background_dict["normal"], animation_speed=5, dt=self.dt)
        self.screen.blit(self.in_game_background.image, (0, 0))


def display_text(screen, text: str, center_pos: tuple, text_color=(255, 255, 255), font="art/font\Canterbury.ttf", text_size=30):
    text_font = pygame.font.Font(font, text_size)
    image = text_font.render(text, True, text_color)
    rect = image.get_rect(center=center_pos)
    screen.blit(image, rect)


def display_bar(screen, width, height, curent, maximum, bar_radius, top_left_pos, top_color, bottom_color):
    bottom_rect = pygame.Rect(top_left_pos, (width, height))
    top_rect = pygame.Rect(top_left_pos, (width*curent/maximum, height))
    pygame.draw.rect(screen, bottom_color, bottom_rect, border_radius=bar_radius)
    pygame.draw.rect(screen, top_color, top_rect, border_radius=bar_radius) 
        

