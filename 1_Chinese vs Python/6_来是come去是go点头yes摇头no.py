"""
字典 = {"来":"come","去":"go","点头":"yes","摇头":"no"}
增加的解释 = {"吃":"eat"}
字典.update(增加的解释)
print(字典)

字典["点头"]="ok"
print(字典)
"""

法师属性={"攻击属性":"火",'血量':"HP 300",'蓝量':"SP 1000"}
print("现在法师攻击属性是："+法师属性["攻击属性"])
print("现在法师血量是："+法师属性["血量"])
print("现在法师蓝量是："+法师属性["蓝量"])

法师属性["攻击属性"]="冰"
print("现在法师攻击属性是："+法师属性["攻击属性"])