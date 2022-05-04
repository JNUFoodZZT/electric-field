import pygame.font

class Scoreboard():
    """显示信息"""

    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #字体
        self.text_color = (255,255,255)
        pygame.init()
        self.font = pygame.font.SysFont('',40)
        #准备初始得分
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        # 分数位于右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)