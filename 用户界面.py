import easygui as g
import sys
'''import sys
while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏^_^')
    msg =('请问你希望在鱼C工作室学习到什么知识呢？')
    title='小游戏互动'
    choies=['石头','剪刀','布']
    choice=g.choicebox(msg,title,choies)
    g.msgbox('你的选择是：'+str(choice),'结果')
    msg='你希望重新选择吗？'
    title='请选择：'
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)'''
#各种演示
#g.egdemo()
msg='你好'
title='这是一个有礼貌的盒子'
Choies=[1,2,3,4]
chioe=g.choicebox(msg,title,Choies)
g.msgbox('你的选择是：'+str(chioe),'结果')
msg='你想吃一道美味的菜吗？'
title='请做出你的选择'
chioe2=['想','不想']
if g.ccbox(msg,title,chioe2):

        msg = '你想吃以下哪种菜呢'
        title = '请做出你的选择'
        chioe2 = ['鱼', '肉']
        if g.ccbox(msg, title, chioe2):
                g.msgbox('你的选择是：' + str(chioe2), '结果')
else:
    sys.exit(0)
