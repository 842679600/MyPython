#文件的写入跟读取
'''
f=open('D:/文件写入.txt','w')
f.write('彭伟是真的帅')
f.write('\npeng')
f.write('\nwei')
f.write('\nzhen')
f.write('\nshuai')
#写入了之后必须要关闭

f.close()'''

def savefiles(myself,youself,count):
    boy_name = 'D:/boy' + str(count) + '.txt'
    boy_list = open(boy_name, 'w')
    boy_list.writelines(myself)
    gril_name = 'D:/gril' + str(count) + '.txt'
    gril_list = open(gril_name, 'w', encoding='UTF-8')
    gril_list.writelines(youself)
    boy_list.close()
    gril_list.close()



f=open('D:/文件写入.txt','r',encoding='UTF-8')
myself=[]
youself=[]
count=1
for each in f:
    if each[:6]!='======':
        (role,each_line)=each.split('：',1)
        if role=='彭伟':
            myself.append(each_line)
        if role=='王祝':
            youself.append(each_line)
    else:
        #创建文件，分别保存
        savefiles(myself, youself, count)
        count += 1
        myself = []
        youself = []

savefiles(myself,youself,count)

#0代表从哪开始截取到10字符，seek（）这个方法表示在文件中移动文件指针
#print(f.seek(20,0))
#read（）读取，不设置读取到哪默认读取全部，然后再使用read（）读取将读取空，因为第一个read（）
#已经读取到最后了。所以第二个只能读取空
#print(f.read())
#print(f.seek(0,0))
#print(f.read())
