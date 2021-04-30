#__new__(cls[,... ])默认执行，当在不可变的类重写的时候会用到
#__init__不能用return
#__del__ 当对象垃圾回收机制销毁所有对象的时候才会使用
#工厂函数=类对象 所有属性方法都是函数
class New_Method(str):
    def __new__(cls, string):
        string=string.lower()
        return str.__new__(cls, string)

new_Method=New_Method("New Method shi shen")

print(new_Method)
