#列表操作
a=[1,2,3]
lenth=len(a)
for i in range(lenth):
    print(a[i])
a.append(4)
for j in a:
    print(j)
print(a[2])
print(a[0:5:1])
print(a[0:5:2])
#推导式
b=[x**2 for x in a]
print(b)
#元组转列表
color=("red","blake","green")
s_color=sorted(color)
print(s_color)
#元组的值给变量
rgb_color = ("red","blake","green")
yellow, green, blue = rgb_color
print(yellow, green, blue)
#集合的交集，并集与检查元素是否在集合中
set1={1,2,3,4,5}
set2={2,5,8,9}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)
is_4_in_set1=4 in set1
print(is_4_in_set1)
#字典
dict={
    "name":'lili',  ##单双引号都可以
    "age":11,       ##注意是冒号  使用分隔符逗号
    'work':"student"
}
print(dict['name'])#访问
dict['nation']='china'#添加与修改
print(dict)
nation=dict.pop("nation")#删除并提取值
print(dict)
print(nation)
for key in dict:#遍历键
    print(key)
for value in dict.values():#遍历值
    print(value)
for key,value in dict.items():#遍历键值对
    print(key,value)
#类型转换
c=int(input("your number is :"))#只接受整数，不是整数报错
print(c)
d=int("42")
print(d)
e=int(3.14)
print(e)
print(tuple(a))
print(list(color))
print(set([1,2,3]))


#print
print('{:_<20}'.format("hello world"))
print('{:_>20}'.format("hello world"))
print('{:+}'.format(123))
print('{:06d}'.format(22))
#if_elif_else
#age=int(input())
age=25
gender='male'
if age>=18:
    if gender=='male':
        print('{:-<10}'.format("成年男性"))
    else:
        print(f"{'成年女性':-<10}")
elif age<18:
    print(f"{"未成年人":-<10}")
#for
fruits=['apple','banana','pear']
for i in fruits:
    print(i)
for j in range(5):
    print(j)
#while
a=5
while a>0:
    print(a)
    a-=1
num=100
while num>0:
    if num%7==0:
        print(f"{num:_<4}")
    num-=1
#break continue else
for i in range(10):
    if i==5:
        break
    print(i)
for i in range(10):
    if i%2==0:
        continue
    print(i)
for i in range(3):
    print(f"{i:2}")
else:
    print("循环正常结束")
#函数
def add(a,b):
    return a+b
result=add(5,2)
print(result)
def greeting(name,greet='hello'):
    print(f"{greet},{name}!")
greeting("Alice")
greeting("Amy","hi")
def pet(type,name):
    print(f"I have a {type} named {name}")
pet(name="peter",type="dog")
def function(*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():#.items()
        print(f"{key}:{value}")
function(1,2,3,name="Amy",age=30)
def student_id(a):
    if a==1:
        return "Amy",20
    if a==2:
        return "Bob",18
    else:
        return "unkown",0
name,age=student_id(1)
print(f"{name}:{age}")
#类
class Person:
    #类属性
    #方法
    def __init__(self,name,age):# 每个类的实例方法的参数都需要self开头。
        self.name=name#实例属性
        self.age=age
b=Person("Amy",30)
print(b.name,b.age)
class Mathunion:
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def mul(cls,a,b):
        return a*b
print(Mathunion.add(2,3))
print(Mathunion.mul(2,3))

