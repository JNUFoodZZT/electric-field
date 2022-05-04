import sys
import pygame
from bullet import Bullet
from alpaca import Alpaca
from time import sleep


def check_keydown_events(event,ai_settings,screen,diana,bullets):
    """按键"""
    if event.key == pygame.K_RIGHT:
        diana.moving_right = True
    elif event.key == pygame.K_LEFT:
        diana.moving_left = True
    elif event.key == pygame.K_UP:
        diana.moving_up = True
    elif event.key == pygame.K_DOWN:
        diana.moving_down = True
    elif event.key == pygame.K_SPACE:
        #创建子弹
        fire_bullets(ai_settings, screen, diana, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,diana):
    """松开"""
    if event.key == pygame.K_RIGHT:
        diana.moving_right = False
    elif event.key == pygame.K_LEFT:
        diana.moving_left = False
    elif event.key == pygame.K_UP:
        diana.moving_up = False
    elif event.key == pygame.K_DOWN:
        diana.moving_down = False

def check_events(ai_settings,screen,stats,play_button,diana,alpacas,bullets):
    """相应鼠标与键盘"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            # 移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,diana,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,diana)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,diana,alpacas,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,diana,alpacas,bullets,mouse_x,mouse_y):
    """单击开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置
        stats.reset_stats()
        stats.game_active = True
        #清空子弹和羊驼
        alpacas.empty()
        bullets.empty()
        #新羊驼和蒂娜
        creat_fleet(ai_settings,screen,diana,alpacas)
        diana.center_diana()

def update_screen(ai_settings,screen,stats,sb,diana,alpacas,bullets,play_button):
    """更新屏幕信息"""
    # 每次循环时都重绘制屏幕

    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    diana.blitme()
    alpacas.draw(screen)
    sb.show_score()
    #非活动态显示按钮
    if not stats.game_active:
        play_button.draw_button()
    #显示计分
    # 显示最新屏幕
    pygame.display.flip()

def fire_bullets(ai_settings,screen,diana,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, diana)
        bullets.add(new_bullet)

def update_bullets(ai_settings,screen,diana,alpacas,bullets):
    #更新消失子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alpaca_collisions(ai_settings,screen,diana,alpacas,bullets)

def check_bullet_alpaca_collisions(ai_settings,screen,diana,alpacas,bullets):
    # 检查是否击中羊驼
    collisions = pygame.sprite.groupcollide(bullets, alpacas, False, True)
    if len(alpacas) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        creat_fleet(ai_settings, screen, diana, alpacas)

def update_alpacas(ai_settings,stats,screen,diana,alpacas,bullets):
    #到达边缘
    check_fleet_edges(ai_settings,alpacas)
    # alpacas.update1()
    for alpaca in alpacas.sprites():
        alpaca.update1()

    #碰撞
    if pygame.sprite.spritecollideany(diana,alpacas):
        diana_graduated(ai_settings,stats,screen,diana,alpacas,bullets)
    check_alpaca_bottom(ai_settings,stats,screen,diana,alpacas,bullets)

def get_alpacas_num(ai_settings,alpaca_width):
    available_space_x = ai_settings.screen_width - 2 * alpaca_width
    number_alpacas_x = int(available_space_x / (2 * alpaca_width))
    return number_alpacas_x

def creat_alpaca(ai_settings,screen,alpacas,alpaca_number,row_number):
    alpaca = Alpaca(ai_settings,screen)
    alpaca_width = alpaca.rect.width
    alpaca.x = alpaca_width + 2 * alpaca_width * alpaca_number
    alpaca.rect.x = alpaca.x
    alpaca.rect.y = alpaca.rect.height + 2* alpaca.rect.height * row_number
    alpacas.add(alpaca)

def get_num_rows(ai_settings,diana_height,alpaca_height):
    """多少行羊驼"""
    available_space_y = (ai_settings.screen_height- (3* alpaca_height) - diana_height)
    num_rows = int(available_space_y / (2 * alpaca_height))
    return num_rows

def creat_fleet(ai_settings,screen,diana,alpacas):
    """创建外星人群"""
    alpaca = Alpaca(ai_settings,screen)
    number_alpacas_x = get_alpacas_num(ai_settings,alpaca.rect.width)
    num_rows = get_num_rows(ai_settings,diana.rect.height,alpaca.rect.height)
    #第一行羊驼
    for num_row in range(num_rows):
        for alpaca_number in range(number_alpacas_x):
            creat_alpaca(ai_settings,screen,alpacas,alpaca_number,num_row)

def check_fleet_edges(ai_settings,alpacas):
    """羊驼到达边缘"""
    for alpaca in alpacas.sprites():
        if alpaca.check_edges():
            change_fleet_direction(ai_settings,alpacas)
            break

def change_fleet_direction(ai_settiongs,alpacas):
    """羊驼下移"""
    for alpaca in alpacas.sprites():
        alpaca.rect.y += ai_settiongs.fleet_drop_speed
    ai_settiongs.fleet_direction *= -1

def diana_graduated(ai_settings,stats,screen,diana,alpacas,bullets):
    """响应碰撞"""
    if stats.diana_left > 0:
        stats.diana_left -= 1
        #清空羊驼和子弹
        alpacas.empty()
        bullets.empty()
        #暂停
        sleep(1)
        #新
        creat_fleet(ai_settings,screen,diana,alpacas)
        diana.center_diana()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_alpaca_bottom(ai_settings,stats,screen,diana,alpacas,bullets):
    """检查羊驼到底"""
    screen_rect = screen.get_rect()
    for alpaca in alpacas.sprites():
        if alpaca.rect.bottom >= screen_rect.bottom:
            #同处理方法
            diana_graduated(ai_settings,stats,screen,diana,alpacas,bullets)
            break
