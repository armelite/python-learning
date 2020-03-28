#i/usr/bin/env/ python3 
#-*- coding:utf-8 -*-
import math
'''
print('中文测试正常')
t = (['apple','huawei','xiaomi'],[1000,2000,500],['hongkong','shanghai',
'guangzhou'])
print(t)

name = input('please enter your name:')
print('hello,',name)
age = int(input('please enter your age:'))
#print(age)
if age >= 18:
   print('hello,%s,your age is %d,so you are a adult!'%(name,age))
elif age>=12:
   print('hello,%s,your age is %d,so you are a teenager'%(name,age))
elif age>=6:
    print('hello,%s,your age is %d,so you are a kid'%(name,age))
else:
    print('hello,%s,your age is %d,so you are a baby'%(name,age))
'''

def my_abs(x):
  if not isinstance(x,(int,float)):
   raise TypeError('bad type')
  if x>=0:
   return x
  else:
   return -x
#a = int(input('please enter a number:'))
#print(my_abs(a))


def power(x,n=2):
  s =1
  while n >0:
     n = n -1 
     s = s*x 
  return s 

def product(*numbers):
    sum = 1
    for n in numbers:
       sum =sum*n
    return sum 
 
'''
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
 #       print('here')
 #       a = bool(product())
 #       print(a)
         product()
         print('测试成功!')
    except TypeError:
        print('测试失败!')
'''        
        
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):

    if n == 1:
        print('move', a, '-->', c)

    else:
        move(n-1, a, c, b)

        move(1, a, b, c)

        move(n-1, b, a, c)
'''
#测试 
move(4, 'A', 'B', 'C')
'''

#利用切片操作，实现一个trim()函数，去除字符串首尾空格
def trim(s):
   for i in range(len(s)):
      if s[:1]==' ':
         s=s[1:]
      elif s[-1:]==' ':
         s=s[:-1]
   return s 
'''
# 测试:
if trim('hello  ') != 'hello':
    print('01测试失败!')
elif trim('  hello') != 'hello':
    print('02测试失败!')
elif trim('  hello  ') != 'hello':
    print('03测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('04测试失败!')
elif trim('') != '':
    print('05测试失败!')
elif trim('    ') != '':
    print('06测试失败!')
else:
    print('测试成功!')
'''
#使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
 if L==[]:
  return(None,None)
 else:
  min = L[0]
  max = L[0]
 for x in L:
   if x <= min:
      min = x 
   elif x > max:
      max = x 
 return(min,max)      
'''
# 测试
if findMinAndMax([]) != (None, None):
    print('01测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('02测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('03测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('04测试失败!')
else:
    print('测试成功!')
'''
#菲波那切数列(fibonacci)
def fib(max):
   n,a,b = 0,0,1
   s = [b]
   while n<max:
     yield b #generator 执行到yield就中断，进入下一次运算
     a,b = b,a+b
     n = n+1
     s.append(b)
   return s