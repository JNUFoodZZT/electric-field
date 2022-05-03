import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹"""

    def __init__(self,ai_settings,screen,diana):
        """在飞船处创建子弹对象"""
        super().__init__()
        self.screen = screen

        # 在（0，0）处创造子弹，再设置正确位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = diana.rect.centerx
        self.rect.centery = diana.rect.centery
        self.rect.top = diana.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数点
        self.y -= self.speed_factor
        #更新表示子弹位置的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕显示子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
