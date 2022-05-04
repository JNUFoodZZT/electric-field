import pygame
from setting import Setting
from diana import Diana
from alpaca import Alpaca
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

"""

"""
def run_game():
    # #初始化游戏，创建一个屏幕对象
    # pygame.init()
    # screen = pygame.display.set_mode((1600,900))
    #
    # #设置背景色
    # bg_color = (124,205,124)
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("鸿儒羊驼")


    #创建统计信息
    stats = GameStats(ai_settings)
    # 创建嘉然
    diana = Diana(ai_settings, screen)
    # 创建按钮
    play_button = Button(ai_settings,screen,"Play")
    # 创建计分
    sb = Scoreboard(ai_settings,screen,stats)
    #创建群
    #创建子弹
    bullets = Group()

    #创建羊驼
    alpacas = Group()
    gf.creat_fleet(ai_settings,screen,diana,alpacas)
    #开始游戏主循环
    while True:

        #监视 鼠标和键盘
        gf.check_events(ai_settings,screen,stats,play_button,diana,alpacas,bullets)
        # 重绘屏幕
        gf.update_screen(ai_settings,screen,stats, sb,diana, alpacas,bullets,play_button)
        #移动
        if stats.game_active:
            diana.update()
            bullets.update()
            gf.update_alpacas(ai_settings,stats,screen,diana,alpacas,bullets)
            gf.update_bullets(ai_settings,screen,diana,alpacas,bullets)





run_game()