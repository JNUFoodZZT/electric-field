class GameStats():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        """初始化"""
        self.ai_settings =  ai_settings
        self.reset_stats()
        #游戏开始处于关闭状态
        self.game_active = False


    def reset_stats(self):
        """初始化信息"""
        self.diana_left = self.ai_settings.diana_limit
        self.score = 0
