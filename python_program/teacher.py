#__________________类型转换
# 整数和浮点数转换
#     - 将整数转换为浮点数：float(5)
#     - 将浮点数转换为整数（截断小数部分）：int(3.14)
# 字符串和数值之间的转换
#     - 将数值转换为字符串：str(42)
#     - 将字符串转换为整数：int("123")
#     - 将字符串转换为浮点数：float("3.14")
# 布尔值转换
#     - 将非零数值转换为True，将零数值转换为False：bool(0) 和 bool(42)
# 列表、元组和集合转换
#     - 将列表转换为元组：tuple([1, 2, 3])
#     - 将元组转换为列表：list((1, 2, 3))
#     - 将列表或元组转换为集合：set([1, 2, 3]) 或 set((1, 2, 3))
#字典转换
#     - 将字典的键转换为列表：list({"a": 1, "b": 2}.keys())
#     - 将字典的值转换为列表：list({"a": 1, "b": 2}.values())
#_____________检查类型
# x = 10

# y="hello world"
# c=[1,2,3]
# d=(4,5,6)
# e={7,8,9}
# student = { #建立字典
#    'name': 'Alice', 
#    'age': 25, 
#    'grade': 'A'
# }
# print(type(x))  # 输出：<class 'int'>，表示x的数据类型是整数
# print(type(y))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(student))

# x = 10
# if isinstance(x, int):
#     print("x是整数类型")

s="hello"
print (len(s))
print (s[0])
for letter in s:
    print(letter)

print(type(s))
a=True
print(type(a))
b=None
print(type(b))

print("Hello world!\n")



def greet (name,greeting="hello"):
    print(f"{greeting},{name}")
print(greet("lili"))
print(greet("bob","hi"))

def example(*args,**kwargs):
    print("\nargument(*args):")
    for arg in args:
        print(arg)
    print("\nkeyword argument(**kwargs):")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
example(1,2,3,name="alice",age="30")


#print(*objects,sep='',end='\\n',file=sys.stdout,flush=False)
'''object 多个对象
    sep间隔
    end设定结尾
    file写入的文件对象
        stdout控制台
    flush:输出是否缓存
'''
print([1,2,3])
print((1,2,3))
print({"name":"alice","age":18})

print("hello","world"+"!")
print("hello","world"+"!",sep="-")
print("hello",end="!")
print()

f=open("aaa.txt","w")
print("hello file",file=f)
f.close()

# number=[1,2,3]
# letter=["a","b"，"c"]
# zipped=zip(number.letter)

