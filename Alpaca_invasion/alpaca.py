import pygame
from pygame.sprite import Sprite

class Alpaca(Sprite):
    """表示单个外星人"""
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载羊驼图像，设置属性
        self.image = pygame.image.load('images/alpaca.bmp')
        self.rect = self.image.get_rect()

        #初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #实时位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def update1(self):
        """移动"""
        self.x += (self.ai_settings.alpaca_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """边缘处返回 True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True