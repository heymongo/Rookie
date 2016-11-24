# -*- coding: utf-8 -*-

#def my_abs(x):
#    if x >=0:
#        return x
#    elif x<0:
#        return -x


#n1 = 255
#n2 = 1000
#print(hex(n1))
#print(hex(n2))

#def my_abs(x):
#    if not isinstance(x, (int, float)):
#        raise TypeError('bad operand type')
#    if x >= 0:
#        return x
#    else:
#        return -x
#print my_abs(0)

#def power(x):
#    return x*x
#print power(5)

#def power(x,n):
#    s=1
#    while n>1:
#        n=n-1
#        s=s*x
#    return  s
#print power(2,11)


#def power(x,n):
#    s=1
#    while n > 0:
#        n = n - 1
#        s = s * x
#    return s

#print power(10,5)


#def calc(*numbers):
#    sum=0
#    for n in numbers:
#        sum = sum + n * n
#    return sum

#print calc(3,11)

#print calc()

#nums = [1,2,3]
#print calc(nums[0], nums[1], nums[2])
#print calc(*nums)

#def person(name,age,**kwargs):
#    if 'city' in kwargs:
#        pass
#    if 'job' in kwargs:
#        pass
#    print('name:',name,'age:',age,'other:',kwargs)

#print person('jack',24,city='beijing',job='shangren')

#def fact(n):
#    if n==1:
#        return 1
#    return n * fact(n-1)
#print fact(3)

#L = ['M','s','t','f','K']
#print L[0:2]

#print L[:2]


#M = list(range(11))

#print M[7:10]
#print M[10:11]

#print M[:10]#从第一位至第十位数字
#print M [10:20]#从数字10至最后一位
#print M [20:30]

#A='hello'
#print A[0]
#print A[-1]
#print 'hello'[1]

#hee=raw_input('year: ')[3]
#print hee
#---------------------------------------------------------------------------------------------------------------------
#根据给定的年月日以数字形式打印出日期
#Months = [
#'January','February','March','April','May',
#'June','July','August','September','October',
#'November','December']

#以1~31的数字作为结尾的列表

#endings = ['st','nd','rd'] + 17 * ['th']\
 #   + ['st','nd','rd'] + 7 * ['th']\
  #  + ['st']

#year = raw_input('Year:')
#month = raw_input('Months(1-12):')
#day = raw_input('Day(1-31):')
#month_number = int(month)
#day_number = int(day)
#月份和天数减1，以获得正确的索引
#month_number = Months[month_number-1]
#ordinal = day +  endings[day_number-1]
#print month_number + ' ' + ordinal + ',' + year
#------------------------------------------------------------------------------------------------------------------------
#迭代 Python中，迭代通过for...in 来完成
#for i in range(5):
#    print i
#    i += 3
#    print i
#    print '一轮结束'

#d = {'a': 1,'b': 2,'c': 3}
#for key in d:
 #   print (key)
#for value in d.values():
#    print value
#for k,v in d.items():
#    print k ,v

#for ch in 'abc':
#    print (ch)
#print '----------------------------------------------------'
from collections import Iterable
print isinstance('abc', Iterable)#str是否可迭代

print isinstance([1,2,3], Iterable)# list是否可迭代

print isinstance(123,Iterable)#整数是否可迭代

#for i ,value in enumerate(['a','b','c']):
 #   print(i,value)

#for x, y in ((1, 1), (2, 4), (3, 9)):
 #   print(x, y)


#for i, value in enumerate(['A', 'B', 'C']):
 #    print(i, value)

#列表生成

print list(range(1,10))#python2.x 中要返回1~10的列表，需要list（range（1,11)),python3.x 中可以正常输出


l=[]
for x in range(1,11):
    l.append(x*x)
print l

print[x*x for x in range(1,11)] #取1~10的平方

print[x*x for x in range(1,11) if x%2==0]#取1~10偶数的平方


















