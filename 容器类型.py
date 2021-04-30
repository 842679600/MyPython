#如果你希望定制的容器是不可变的话，你只需要重写__len()__和__gettiem()方法
#如果你希望定制的容器是可变的话，你需要重写__len()__和__gettiem()你还需要定义__settiem()__和__delitem__（）
#定制的容器是不可变的,而且每访问一次。就加1
'''
class Listcount:
    def __init__(self,*args):
        self.valus=[x for x in args]
        self.count={}.fromkeys(range(len(self.valus)),0)
        print(self.count)
    def __len__(self):
        return len(self.valus)
    def __getitem__(self, keys):
        self.count[keys]+=1
        print(self.count)
        return self.valus[keys]
        '''
