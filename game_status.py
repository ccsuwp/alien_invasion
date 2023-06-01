class GameStatus:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.score = 0
        self.ship_life = self.settings.ship_life
        self.game_level = self.settings.game_level
        self.alien_speed_x = self.settings.alien_speed_x
        self.alien_row_count = self.settings.alien_row_count
        self.alien_row_size = self.settings.alien_row_size

        self.alien_speend_update_flag = False

    def reset_game(self):
        self.score = 0
        self.ship_life = self.settings.ship_life
        self.game_level = self.settings.game_level
        self.alien_speed_x = self.settings.alien_speed_x
        self.alien_row_count = self.settings.alien_row_count
        self.alien_row_size = self.settings.alien_row_size
        self.alien_speend_update_flag = False
        if self.game_level == 1:
            self.alien_speed_x = self.settings.alien_speed_x_max

    def update_game(self):
        row_count_flag = self.alien_row_count + self.settings.alien_row_count_offset <= \
                         self.settings.alien_row_count_max
        row_size_flag = self.alien_row_size + self.settings.alien_row_size_offset <= self.settings.alien_row_size_max
        if not self.alien_speend_update_flag:
            if row_size_flag or row_count_flag:
                if row_count_flag:
                    self.alien_row_count += self.settings.alien_row_count_offset
                if row_size_flag:
                    self.alien_row_size += self.settings.alien_row_size_offset
            else:
                self.alien_speend_update_flag = True
        else:
            if self.game_level == 0 and self.alien_speed_x <= \
                    self.settings.alien_speed_x_max:
                self.alien_speed_x += self.settings.alien_speed_x_offset
