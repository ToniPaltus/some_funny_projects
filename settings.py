class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует статические настройки игры"""

        #Парамерты экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #Настройки корабля
        self.ship_limit = 3

        #Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (180, 20, 30)
        self.bullets_allowed = 5

        #Настройки пришельцев
        self.fleet_drop_speed = 10

        #Темп ускорения игры
        self.speedup_scale = 1.1
        #Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.inizialize_dynammic_settings()

    def inizialize_dynammic_settings(self):
        """Инициализирует настройки скорости и стоимость пришельцев"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 7
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1  # 1 - вправо, -1 - влево
        self.alien_points = 50 #Подсчет очков
    def increase_speed(self, repeat=1):
        """Увеличивает настройки скорости"""
        for i in range(repeat):
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)