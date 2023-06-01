from alien import Alien


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1

        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_count = 999

        self.alien_rect = Alien.get_rect()
        self.alien_speed_x = 0.2
        self.alien_speed_y = 0.08
        self.alien_speed_x_offset = 0.1
        self.alien_speed_x_max = 2
        self.alien_row_count = 1
        self.alien_row_count_offset = 1
        self.alien_row_count_max = 3
        self.alien_row_size = 3
        self.alien_row_size_offset = 3
        self.alien_row_size_max = 12

        self.game_level = 0  # 0-经典 -1-简单 1-极速
        self.game_active = False

        self.default_button_color = (0, 255, 0)
        self.not_selected_button_color = (128, 128, 128)
        self.level_selected_button = None

        self.ship_life = 5

        self.score = [0, 0, 0]
        self.max_score = [0, 0, 0]



