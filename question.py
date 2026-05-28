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

b = []   #创建一个空列表,有顺序、可修改、允许重复元素。
b = ()   #创建一个空元组,有顺序、不可修改、允许重复元素，单元素元组必须加逗号，不然识别为int。
b = {}   #创建一个空字典,有键值对组成，键必须唯一，值可以重复。
b = set([1,2,3]) #创建一个空集合,无序、不可修改、元素唯一。
print(b)
