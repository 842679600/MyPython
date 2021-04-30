#对象=属性+方法，类名是大写字母开头
#面象对象的特征1.封装（信息屏蔽技术）2.继承 3.多态（名字一样，但是类不一样）
#OOA面向对象分析，oop面向对象编程 ood：面向对象设计
#slef 相当于c+的指针，每个类都是需要self第一个参数

msg=''
class Python_first_class():
    def fisrtdef(self,name):
        self.name = name
        print('你好'+self.name)

x=Python_first_class()

x.fisrtdef('pp')
#什么是继承
class Mylist(list):
    pass

List1=Mylist()
List1.append(1)
List1.append(3)
List1.append(1)
print(List1)
#_init_ Python中的魔法方法
class Ball:
    def __init__(self,name):
        self.name=name
    def kick(self):
        print("该死的谁踢我啊"+self.name)
x=Ball('小白熊')
x.kick()

#y=Ball()会报错，提示需要加入参数name
