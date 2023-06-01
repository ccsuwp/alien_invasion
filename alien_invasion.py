import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from game_status import GameStatus
from score_board import ScoreBoard


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = pygame.sprite.Group()
        self.ship.add(Ship(self))

        self.game_status = GameStatus(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # 用于定位水平边界元素
        self.aliens_level_side = []
        self.create_new_alien()

        self.play_button = Button(self, "PLAY",
                                  self.settings.default_button_color, -3)
        self.classic_button = Button(self, "Classic",
                                     self.settings.default_button_color, -1)
        self.easy_button = Button(self, "EASY",
                                  self.settings.not_selected_button_color, 1)
        self.harder_button = Button(self, "HARDER",
                                    self.settings.not_selected_button_color, 3)
        self.settings.level_selected_button = self.classic_button

        self.current_life_ships = pygame.sprite.Group()
        self.create_life_ship()

        self.score_board = ScoreBoard(self)

    def create_life_ship(self):
        self.current_life_ships.empty()
        for i in range(self.settings.ship_life):
            ship = Ship(self)
            ship.rect.top = self.screen.get_rect().top + 20
            ship.rect.left = 20 + ship.rect.width * i
            self.current_life_ships.add(ship)

    def creat_alien(self, row_count, row_size):
        max_row_size = int((self.settings.screen_width // self.settings.alien_rect.width - 1) // 2)
        max_row_count = int(self.settings.screen_height * 3 / 4 // (self.settings.alien_rect.height * 2))

        row_count = row_count if row_count < max_row_count else max_row_count
        row_size = row_size if row_size < max_row_size else max_row_size

        inter_width = (self.settings.screen_width - self.settings.alien_rect.width * row_size) / (row_size + 1)
        inter_height = self.settings.alien_rect.height

        for r in range(row_count):
            for c in range(row_size):
                al = Alien(self)
                position_x = (c + 1) * inter_width + c * al.rect.width
                position_y = (r + 1) * inter_height + r * al.rect.height
                al.set_position(position_x, position_y)
                self.aliens.add(al)

                # 用于定位水平边界元素
                self.aliens_level_side = sorted(self.aliens.sprites(), key=lambda alien: alien.rect.x)

    def create_new_alien(self):
        self.creat_alien(self.game_status.alien_row_count, self.game_status.alien_row_size)

    def key_down_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.sprites()[0].move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.sprites()[0].move_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.sprites()[0].move_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.sprites()[0].move_right = True
        elif event.key == pygame.K_SPACE and self.settings.game_active:
            self.bullets.add(Bullet(self))
            self.settings.bullet_count -= 1

    def key_up_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.sprites()[0].move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.sprites()[0].move_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.sprites()[0].move_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.sprites()[0].move_right = False

        # 按ESC键退出游戏
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_button(self, mouse_pos):
        level_before_button = self.settings.level_selected_button

        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.game_active = True
            self.settings.score[self.settings.game_level] = 0
        elif self.classic_button.rect.collidepoint(mouse_pos):
            if self.settings.game_level != 0:
                self.settings.game_level = 0
                self.settings.level_selected_button = self.classic_button
                self.reset_alien_and_ship()
        elif self.easy_button.rect.collidepoint(mouse_pos):
            if self.settings.game_level != -1:
                self.settings.game_level = -1
                self.settings.level_selected_button = self.easy_button
                self.reset_alien_and_ship()
        elif self.harder_button.rect.collidepoint(mouse_pos):
            if self.settings.game_level != 1:
                self.settings.game_level = 1
                self.settings.level_selected_button = self.harder_button
                self.reset_alien_and_ship()

        level_after_button = self.settings.level_selected_button
        if level_before_button != level_after_button:
            level_before_button.button_color = self.settings.not_selected_button_color
            level_after_button.button_color = self.settings.default_button_color

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.key_down_events(event)
            elif event.type == pygame.KEYUP:
                self.key_up_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_button(mouse_pos)

    def reset_alien_and_ship(self):
        if self.settings.game_active:
            self.game_status.update_game()
        else:
            self.end_game()
            self.create_life_ship()

        self.ship.sprites()[0].ship_centre()
        self.bullets.empty()
        self.aliens.empty()
        self.create_new_alien()

    def check_alien_side_or_hit(self):
        if self.aliens.sprites()[-1].rect.bottom >= self.screen.get_rect().bottom or \
                pygame.sprite.spritecollideany(self.ship.sprites()[0], self.aliens):
            self.reset_alien_and_ship()
            self.game_status.ship_life -= 1
            if self.game_status.ship_life <= 0:
                self.settings.game_active = False
                self.reset_alien_and_ship()
            else:
                self.current_life_ships.remove(self.current_life_ships.sprites()[-1])

    def end_game(self):
        level = self.settings.game_level

        if self.game_status.score > self.settings.max_score[level]:
            self.settings.max_score[level] = self.game_status.score
        self.game_status.reset_game()

    def check_bullet_hit_alien(self):

        collide = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collide:
            deleted_aliens = []
            for alien_group in collide.values():
                deleted_aliens.extend(alien_group)
            for alien in deleted_aliens:
                self.aliens_level_side.remove(alien)
            self.game_status.score += 10
            self.settings.score[self.settings.game_level] = self.game_status.score
            if len(self.aliens.sprites()) == 0:
                self.reset_alien_and_ship()

    def move_level(self):
        status = 0
        if self.aliens_level_side[0].rect.left <= self.screen.get_rect().left:
            status = 1
        elif self.aliens_level_side[-1].rect.right >= self.screen.get_rect().right:
            status = 2
        for alien in self.aliens.sprites():
            if status == 1:
                alien.move_left = False
                alien.move_right = True
            elif status == 2:
                alien.move_left = True
                alien.move_right = False

    def check_bullet_outer(self):
        for bullet in self.bullets:
            if bullet.rect.bottom == self.screen.get_rect().top:
                self.bullets.remove(bullet)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.ship.draw(self.screen)
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)

        if not self.settings.game_active:
            self.draw_button()

        self.current_life_ships.draw(self.screen)

        self.score_board.draw()

        pygame.display.flip()

    def start_game(self):
        self.move_level()
        self.check_bullet_hit_alien()
        self.check_alien_side_or_hit()
        self.ship.update()
        self.bullets.update()
        self.check_bullet_outer()
        self.aliens.update()

    def draw_button(self):
        self.play_button.draw_button()
        self.classic_button.draw_button()
        self.easy_button.draw_button()
        self.harder_button.draw_button()

    def run_game(self):
        while True:
            self.check_events()
            if self.settings.game_active:
                self.start_game()

            self.update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
