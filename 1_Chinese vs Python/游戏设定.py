class 主角():
    def __init__(self,血量,技能,等级,姓名):
        self.血量=血量
        self.技能=技能
        self.等级=等级
        self.姓名=姓名

    血量 = 100
    等级 = 0
    姓名 = ""
    技能 = {"普通攻击":"1级"}

    def 升级到十级增加技能(self,增加技能):
        self.技能.update(增加技能)
        print("恭喜你获得新技能：重击（等级1）")

"""
class 怪物():
    def __init__(self):
"""
