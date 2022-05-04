import pygame.font


class Button():

    def __init__(self,ai_settings,screen,msg):
        """初始化按钮"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #加载嘉然图像、获取外形
        self.cover_image = pygame.image.load('images/cover.bmp')
        self.cover_rect = self.cover_image.get_rect()
        self.screen_rect = screen.get_rect()

        #设置按钮尺寸等
        self.width, self.height = 200,50
        self.button_color = (0,20,0)
        self.text_color = (255,255,255)
        pygame.init()
        self.font = pygame.font.SysFont('',48)

        #创建对象
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，使其在按钮上"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.cover_rect.bottom = self.rect.bottom

    def draw_button(self):
        # 绘制按钮
        self.screen.blit(self.cover_image, self.cover_rect)
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
