import pygame

class Diana():

    def __init__(self,ai_settings,screen):
        """初始化嘉然位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载嘉然图像、获取外形
        self.image = pygame.image.load('images/diana.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #新嘉然位于屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #center中储存小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.diana_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.centerx -= self.ai_settings.diana_speed_factor
        if not self.moving_up and self.centery < 950:
            self.centery += self.ai_settings.diana_speed_factor
        if not self.moving_down and self.centery > 50:
            self.centery -= self.ai_settings.diana_speed_factor




        #根据center更新rect
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        """指定位置绘制嘉然"""
        self.screen.blit(self.image,self.rect)

    def center_diana(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom