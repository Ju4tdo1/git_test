a = 2
b = 3
list1 = [1, 2, 3]
print(list1[0])
lis = [1, 2, 3]
print(lis[1])
complex_num = 1 + 2j
print(complex_num)
print(a/b)
print('666 %s%s' % ('你','吃大粪去吧'))

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.1f%%' %r)

classmate = ['小明', '小红', '小刚']
classmate.remove('小红')
print(classmate)

b = ['小明', '小红', '小刚']   #创建一个空列表,有顺序、可修改、允许重复元素。
print('列表:',b[0])

b = ('小明','小红','小刚',)    #创建一个空元组,有顺序、不可修改、允许重复元素，单元素元组必须加逗号，不然识别为int。
print('元组:',b[0])

b = set([1,2,3])              #创建一个空集合,无序、可增减元素、元素唯一。 单key
s = {1, 2, 3}                 #集合（单个元素）
print('集合:',s)

b = {                         #创建一个空字典,有键值对组成，键必须唯一，值可以重复。 key:value
    'name': '小明',
    'age': 18,
    'hight': 1.75,
    'weight': 70
}  
print('字典:',b['name'])

score = 'B'   #条件语句：if...else...，根据条件执行不同代码块。
if score >= 'A':
    print('score is not A.')


score = 'B'   #条件语句：if...elif...else...，根据不同条件执行不同代码块。
if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')


age = 7
match age:     #条件语句：match...case...，根据不同条件执行不同代码块，类似于switch...case...。
    case x if x < 10:
        print(f'< 10 years old: {x}')      #f-string格式化字符串，使用{}括起来的变量会被替换为对应的值。
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

sum = 0
for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    sum = sum + x
print(sum)


#这些if，for，while，后面都要加冒号，表示代码块的开始，代码块内的语句要缩进。
sum = 0
for x in (range(1, 11, 2)):   #range()函数生成一个整数序列，参数分别是起始值、结束值（不包含）和步长。
    sum = sum + x
print(sum)

