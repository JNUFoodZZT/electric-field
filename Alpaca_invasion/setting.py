class Setting():
    """
    储存羊驼游戏的设置类
    """
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (124,205,124)

        # 嘉然的设置
        self.diana_speed_factor = 2

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 139,16,16
        self.bullet_allowed = 3

        # 羊驼设置
        self.alpaca_speed_factor = 1.5
        self.fleet_drop_speed = 10
        # direc 为1表示右移， -1 为左移
        self.fleet_direction = 1