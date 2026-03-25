# 1.append方法
a=[]
for _ in range(3):#输入不足3个会报错,每个数据间换行
    a.append(int(input()))
print(a)

# 2
b=[input() for _ in range(3)]#每个数据间换行
print(b)

# 3 list
scores=list(map(int,input().split()))# 输入一行，用空格符分隔。