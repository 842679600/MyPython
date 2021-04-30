#{}表示字典，映射类型[]列表类型（）元组类型，字典由key，value组成
#字典表现类型{x：y}前面是key，后面是value，调用的话是value=字典[key]
#当索引不好用的时候就是字典的作用了
'''
pw=['最帅','是的']
print(pw.index('最帅'))
'''

'''
字典的例子
bio={1:'彭伟',2:'帅不帅？',3:'必须帅'}

print(bio[1])
print(bio[2])
print(bio[3])
'''
'''
#通过系统关键字dict创建一个字典
dict=dict(((11,'hello'),(22,'world')))
print(dict)
'''
'''
#通过系统关键字dict创建一个字典(这种key不能为字符串，而且排序是按照首字母排序的)

dict2=dict(彭伟='很帅啊',彭子译='更帅啊')
print(dict2)
'''
'''
第三种创建方式
dict2= {}
dict2['彭伟']='一个很拽的男人'
print(dict2)
'''
bio={1:'彭伟',2:'帅不帅？',3:'必须帅'}
print(bio.values())
print(bio.keys())
#清空，最好别直接使用bio={}，因为如果你向别人赋值的话，
# 你清空了，你使用bio={}，但是人家在你之前bio1=bio的话。bio1的值还存在不会情空，所以最好使用clear（）
bio.clear()
print(bio)
bio2=bio.fromkeys(range(20),'234')
print(bio2.get(3))
#打印一个元组
for i in bio2.items():
    print(i)

print(19 in bio2 )
print(20 in bio2 )

bio3={'玥兮':'女儿'}
#相当于把bio3添加进bio2，更新
bio2.update(bio3)
print(bio2)
