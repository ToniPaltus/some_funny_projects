import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/spaceShip.png')
        self.rect = self.image.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x) #Сохранение вещественной координаты центра корабля
        self.y = float(self.rect.y) #Сохранение вещественной координаты центра корабля

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
    def update(self):
        """Обновляет позицию корабля с учетом флагов"""
        #Обновляется атрибут х, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.x -= self.settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            if self.moving_up:
                self.y -= self.settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_down:
                self.y += self.settings.ship_speed_factor

        self.rect.x = self.x   #Обновление атрибута rect на основании self.x
        self.rect.y = self.y
    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)