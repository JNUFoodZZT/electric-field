class Setting():
    """
    储存羊驼游戏的设置类
    """
    def __init__(self):
        """初始化游戏静态设置"""
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (124,205,124)

        # 嘉然的设置
        self.diana_limit = 3

        # 子弹设置
        self.bullet_width = 30
        self.bullet_height = 12
        self.bullet_color = 139,16,16
        self.bullet_allowed = 3

        # 羊驼设置

        self.fleet_drop_speed = 10


        #动态加速
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化 游戏进行变化设置"""
        self.diana_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alpaca_speed_factor = 1.2

        # direc 为1表示右移， -1 为左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度"""
        self.diana_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alpaca_speed_factor *= self.speedup_scale