import time as t

class MathTime():
    def __init__(self):
        print("请先启动计时器！")
        self.datimez=['年','月','日','时','分','秒']

        self.begin = 0
        self.end=0
        self.lasted = []

    def __str__(self):
        return self.sumSecond

    __repr__=__str__

    def start(self):

        self.sumSecond='请先运行stop（）'
        print('我已经开始了。。。。。')
        self.begin=t.localtime()

    def __add__(self, other):
        self.sumSecond = '总共运行了'
        addtime=[]
        for index in range(6):
            addtime.append(self.lasted[index]+other.lasted[index])
            if addtime[index]:
                self.sumSecond+=(str(addtime[index])+self.datimez[index])
        return self.sumSecond

    def stop(self):
        if not self.begin:
            print('请先运行start（）')
        else:
            self.end = t.localtime()
            x2 = self.clus()
            print(x2)
            print('计时结束')


    def clus(self):
        self.lasted = []
        self.sumSecond='总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.sumSecond+=str(self.lasted[index])+self.datimez[index]
        return self.sumSecond
        #为下一轮计时做准备
        self.begin = 0
        self.end = 0



