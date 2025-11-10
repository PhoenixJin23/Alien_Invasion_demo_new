import pygame.font


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self,ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game = ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        #self.stats=ai_game.stats # 可能存在的问题：保存了旧的stats引用
        #显示得分信息时使用的字体设置
        self.text_color=(255, 255, 255)
        self.font=pygame.font.SysFont(None,48)
        #准备初始得分图像
        self.prep_score()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        # 关键修改：每次都从ai_game获取最新的stats
        score = self.ai_game.stats.score  # 直接访问最新的分数
        rounded_score = round(score, -1)#round表示取整，-1表示向小数点前1位取整，aka取10的整倍数
        score_str="{:,}".format(rounded_score)#字符串格式化，:,给数字添加千位分隔符
        self.score_image=self.font.render(score_str,True,self.text_color,None)
        #在屏幕右上角显示得分
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20#距离屏幕最右侧20像素的位置
        self.score_rect.top=20#距离顶端也是20像素的距离
        print(f"更新记分牌，真实分数: {score}")

    def show_score(self):
        #在游戏上显示得分
        self.screen.blit(self.score_image,self.score_rect)