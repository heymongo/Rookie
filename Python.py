# -*- coding: utf-8 -*-
#已运行OK 的默认注释
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
#from collections import Iterable
#print isinstance('abc', Iterable)#str是否可迭代

#print isinstance([1,2,3], Iterable)# list是否可迭代

#print isinstance(123,Iterable)#整数是否可迭代

#for i ,value in enumerate(['a','b','c']):
 #   print(i,value)

#for x, y in ((1, 1), (2, 4), (3, 9)):
 #   print(x, y)


#for i, value in enumerate(['A', 'B', 'C']):
 #    print(i, value)

#列表生成

#print list(range(1,10))#python2.x 中要返回1~10的列表，需要list（range（1,11)),python3.x 中可以正常输出


#l=[]
#for x in range(1,11):
 #   l.append(x*x)
#print l

#print[x*x for x in range(1,11)] #取1~10的平方

#print[x*x for x in range(1,11) if x%2==0]#取1~10偶数的平方

#print [m + n for m in 'ABC' for n in'XYZ']

#import os
#[d for d in os.listdir('.')]
#print['.emacs','.ssh','.Trash','Desktop']

#-------------------------------------------------------------------------------------------------------------------------
##迭代(Iteration)

#d = {'a':1,'b':2,'c':3}
#for value in d.iteritems():
#    print value


#from collections import Iterable
#print isinstance('x',Iterable)

#for i ,value in enumerate(['a','b','c']):
#    print i,value

#for x,y in[(0,1),(1,2),(2,3)]:
#    print x,y
#--------------------------------------------------------------------------------------------------------------------------
##列表生成式
#print range(0,10)
##生成器
#l = [ x * x for x in range(10)]
#print l

#创建一个生成器
#g = ( x * x for x in range(10))
#generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
#print g.next()
#print g.next()
#print g.next()

#当然，上面这种不断调用next()方法实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
#g = ( x * x for x in range(10))
#for n in g:
#    print n

#fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
#def fib(max):
#    n, a, b = 0, 0, 1
#    while n < max:
#        print b
#        a, b = b, a + b
#        n = n + 1
#print fib(10)

#def fib(max):
#    n,a,b = 0,0,1
#    while n<max:
#        yield b
#        a,b = b,a + b
#        n = n + 1

#print fib(60)


#def odd():
#    print 'step 1'
#    yield 1
#    print 'step 2'
#    yield 2

#o = odd()
#print o.next()
#print o.next()

#for n in fib(6):
#    print n
#------------------------------------------------------------------------------------------------------------------------
#函数式编程
#高阶函数
#调用函数print abs(-10)
#输出函数本身print abs
#将结果赋值给变量，然后输出变量:
#x = abs(-11)
#print x

#将变量指向一个函数:
#f=abs
#print f(-33)

#f = abs
#print f

#把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数了:
#abs = 10
#print abs(-10)

#def add(x,y,f):
#    return f(x) +f(y)
#print add(-5,6,abs)
#当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：
#x ==> -5
#y ==> 6
#f ==> abs
#f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
#编写高阶函数，就是让函数的参数能够接收别的函数．把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#map/reduce
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
#def f(x):
#     return x * x
#print map(f, [1,2,3,4,5,6])

#l = []
#for n in []:
#    l.append(f(n))
#print l
#把list所有数据转为字符串
#print map(str, [1,2,3,4,5])

#reduce(f, [*1,*2,,*3,*4]) = f(f(f(*1,*2,*3), *4))
#序列求和
#def add(x,y):
#    return x + y
#print reduce(add,[1,3,5,7,9])
#把序列[1,3,5,7,9]变成整数13579
#def fn(x,y):
#    return x*10+y
#print reduce(fn,[1,3,5,7,9])
#将字符串转化成整数
#def str2int(s):
#    def fn(x,y):
#        return x*10+ y
#    def char2num(s):
#        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#    return reduce(fn,map(char2num, s))


#def standard(L):
#    return  map(str.title,L)

#print standard(['aMAND','BBAY','systerm'])
#求积
#def prod(L):
#    def lay(x,y):
#        return x*y
#    return reduce(lay,L)
#print prod([1,2,3,4])

#Python内建的filter()函数用于过滤序列.和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 1.在一个list中删掉偶数，只保留奇数，如下：n%2==1取奇数，n%2==0取偶数
def is_odd(n):
    return n % 2 == 0
print filter(is_odd, [1,2,4,5,6,7,9,10])

#去除序列中的空字符串。ps：字符串本身带空格的不支持去掉，例如'A  '
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A ', '', ' ','aa',None])








