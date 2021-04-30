#使用raise语句引发异常
#写一个文件报出异常如何处理？

try:
    f = open('D:/Exceptionfile.txt','w')
    f.write('是的出错了')
    s=1+'1'
    print(f)
except TypeError as res:
    print("出错的原因是："+str(res))
#无论怎么出错，finally都是必须执行的语句
finally:
    f.close()
#捕获类型错误或者文件错误
'''except (OSError,TypeError) :
    print('文件出错了，出错的原因')'''
#自己定义并且让系统提示哪里出错

'''
#with语句，可以考虑你文件没有关闭的话可以主动给你关闭文件,用法如下，或者在此文件没有可读的情况下主动处理
try:
with open('D:/Exceptionfile','w') as f
    for each_line in f
        print(each_line)
except OSError as res
    print("出错的原因是："+str(res))
'''




