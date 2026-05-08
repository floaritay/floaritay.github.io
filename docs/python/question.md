# 注意  

1 输入输出


```python
#(1)数据之间有空格，以一行输入
# input()函数读取一行输入，数据之间以空格分隔。使用split()方法将字符串分割成一个列表
 
numbers = list(map(int, input().split()))# 输入[1457] 输出[1475];输入[1 4 5 7] 输出[1 4 7 5]
numbers = list(map(int, input()))# 输入[1457] 输出[1，4，7，5];输入[1 4 5 7] 输出报错

#(2)每个数据之间用换行符输入：  
# 使用一个循环来逐行读取输入

numbers = []
for _ in range(10):# 假设我们知道要输入10个整数
    # 读取每行输入并转换为整数 
    numbers.append(int(input()))
#或
numbers = [input().strip() for _ in range(10)]
```

2 .join


```python
# join() 是一个字符串方法，用于将序列（如列表、元组等）中的元素连接成一个新的字符串。每个元素之间会插入指定的分隔符（默认为空字符串）
# 格式：separator.join(iterable)
# separator：指定要插入到序列中元素之间的字符串
# iterable：一个可迭代对象，如列表、元组、集合等，其元素都必须是字符串
words = ["Hello", "world", "this", "is", "Python"]
sentence = " ".join(words)#每个元素之间插入一个空格
print(sentence)

# 将每个数字转换为字符串
numbers = [1, 2, 3, 4, 5]
# 使用逗号作为分隔符连接字符串
print(",".join(str(num) for num in numbers))

```

3 map


```python
# 对序列（例如列表、元组等）中的每个元素执行指定的函数，并返回一个新的迭代器，该迭代器包含了函数处理后的结果。
# 格式:map(function, iterable, ...)
# function：这是我们想要对序列中每个元素应用的函数。
# iterable：一个或多个可迭代对象，如列表、元组等。map() 会将函数依次应用于这些可迭代对象中的元素。如果有多个可迭代对象，函数必须能够接收与可迭代对象数量相匹配的参数

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # 需要将map对象转换为列表来查看结果

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = map(lambda x, y: x + y, list1, list2)
print(list(sums))
```

4 lambda


```python
# lambda 是一个关键字，用于创建匿名函数（即没有具体名称的函数）
# lambda 函数可以接受任意数量的参数，但只能有一个表达式。这个表达式的结果就是 lambda 函数的返回值。
# 格式：lambda arguments: expression
# arguments：参数列表，与常规函数定义中的参数列表相同。
# expression：一个关于参数的表达式，其计算结果将作为 lambda 函数的返回值

add = lambda x, y: x + y
print(add(5, 3))  # 输出: 8

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出: [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4, 6]

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)  # 输出: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

5 ord函数 获取ASCLL码

6 解包


```python
a=[1,2]
print(*a)
```

7 strip()


```python
# 去除字符串的首尾空白字符（包括空格、制表符、换行符等）。
# 此外，它还可以接受一个可选参数，用于指定要删除的字符集合。
# 该参数是一个字符串，表示要删除的字符集合。strip()函数的作用是将字符串两端的指定字符删除，并返回删除后的新字符串。
price = "$$99.99$$"
cleaned_price = price.strip("$")
print(cleaned_price)  # 输出: "99.99"
```

# 套一

 1 计算邮资


```python
# 根据邮件的重量和用户是否选择加急计算邮费。
# 计算规则：重量在1000克以内(包括1000克), 基本费8元。超过1000克的部分，每500克加收超重费4元，不足500克部分按500克计算；如果用户选择加急，多收5元

a,b=input().split()#默认输入为字符串
a=int(a)
sum=8
if a>1000:
    a-=1000
    if b=='y':
        if a%500==0:
            sum=sum+((a//500)*4)+5 #//整除，/除是浮点数，5/2=2.5
        elif a%500!=0:
            sum=sum+((a//500+1)*4)+5
    elif b=='n':
        if a%500==0:
            sum=sum+((a//500)*4)
        elif a%500!=0:
            sum=sum+((a//500+1)*4)
        
print(sum)
```

2 统计数字字符个数*


```python
# 输入一行字符，统计出其中数字字符的个数。
input_string=input()
count=0
for ch in input_string:
    if ch in '0123456789':
        count+=1
print(count)
```

3 与7无关的数


```python
# 一个正整数，如果它能被7整除，或者它的十进制表示法中某一位上的数字为7，则称其为与7相关的数。现求所有小于等于n(n<100)与7无关的正整数的平方和。
m=int(input())
num=0
for i in range(1,m+1):
    if i%7!=0:#不被7整除
        if i%10!=7:#个位不为7
            if i//10!=7:#十位不为7
                num=num+i**2
print(num)        

```

4 高考志愿排序*


```python
# 首先按照总分降序排列；当总分相同时，再按照语文分数降序排序；
# 当语文分数也相同时，再按照数学分数降序排序；当数学分数也相同时，再按照英语分数降序排序。
# 所有分数都相同时，再按照录入的顺序排列。
# 给定n（10≤n≤1000）个人的有关信息，按照上述规则排序之后，输出最前面的m（1≤m≤n）个人的序号。  

m,m=map(int,input().split())
student=[]#[(),(),()]形式
for i in range(m):
    chinese,math,english=map(int,input().split())
    sum=chinese+math+english
    student.append((sum,chinese,math,english,i+1))#作为一个整体元组(总分，语，数，英，序号)

student.sort(key=lambda s: ( -s[0], -s[1], -s[2], -s[3], s[4]))#-表示降序

# 输出排序后前m个学生的序号
for i in range(m):
    print(student[i][4], end=' ')  # 输出序号，并用空格分隔
```

5 查找回文数 *


```python
# 回文数是一种特殊的数，从左边读和从右边读是一样的，比如123321就是一个回文数。现在给定一个正整数n（n≤54），
# 编程求出一个回文数，要求该回文数的各位数字之和等于n，且该回文数大于10000，小于等于99999。
# 如果有多个满足条件的回文数，输出最小的这个；如果没有满足条件的回文数，输出"Not found"。
m=int(input())
def is_palindrome(num):
    """检查一个数是否是回文数"""
    s = str(num)
    return s == s[::-1]

def digit_sum(num):
    """计算一个数的各位数字之和"""
    return sum(int(digit) for digit in str(num))

def find_palindrome(n):
    """找出满足条件的回文数"""
    for i in range(10001, 100000):  # 在10001到99999之间查找
        if is_palindrome(i) and digit_sum(i) == n:
            return i
    return "Not found"

result = find_palindrome(m)
print(result)  # 输出 13831

```

6 最小的素数


```python
# 给定n（n≤100）个正整数，所有正整数均≤100,000；求其中最小的那个素数。题目保证至少有一个素数。
m=int(input())
numbers = []
min=100000
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for i in range(m):
    num = int(input())
    numbers.append(num)
for i in range(m):
    if(is_prime(numbers[i])==True):
        if numbers[i]<min:
            min=numbers[i]
print(min)
```

# 套二

1 球弹跳高度的计算 *


```python
# 一球从某一高度h落下(单位米，n≤1,000,000)，每次落地后反跳回原来高度的一半，再落下。编程计算气球在第10次落地时，共经过多少米? 第10次反弹多高
# 输出包含两行，第1行：到球第10次落地时，一共经过的米数。第2行：第10次弹跳的高度。  
# 输出结果保留小数点后4位。
h=float(input())
sum=h
for i in range(9):
    
    h=h/2
    sum=sum+h*2
print(f"{sum:.4f}") #.4是四位有效数，。4f是四位小数
h=h/2
print(f"{h:.4f}")      


```

2 最高的分数*


```python
# 例如有成绩：68 61 25 54 84 96 34，最高分数96
#一共有两行，第一行为整数n（1 ≤ n ≤100），表示参加这次考试的人数。第二行是这n个学生的成绩，相邻两个数之间用空格隔开。所有成绩均为0到100之间的整数。

m=int(input())
student=[]
for i in range(m):
    a=int(input())
    student.append(a)
# student.sort(reverse=True)
# print(student[0])
max_num=max(student)
print(max_num)
#
# num=input()
# scores = list(map(int, input().split()))
# highest_score = max(scores)
# print(highest_score)
```

3 简单排序?


```python
# 输入11个整数，如果第1个数为1，则将其中的第2至11个数升序排列；如果第1个数为0，则降序排列。

scores=list(map(int,input().split())) #输入一行，包含11个整数，用空格符分隔。
if scores[0]==1:
    scores.sort()#升序
if scores[0]==0:
    scores.sort(reverse=True)#降序

# 输入 1 2 3 5 7 9 4 8 6 10 11    
# print(scores[1:11])#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]会带括号

# for i in range(10):
#     print(scores[i+1],end=' ')
for i in range(1,11):
    print(scores[i],end=' ')
# print(' '.join(map(str, scores[1:])))
```

4 阶乘累加和*


```python
# 给定一个正整数n(n≤100)，计算1!+2!+3!+……+n!的和值  
# 例如当n=5时，和值为153；当n=10时，和值为4037913
m=int(input())
sum=0
def fac(a):#阶乘函数
    if a==0:
        return 1
    else:
        return a*fac(a-1)

for i in range(1,m+1):#n=5  range(1,6)=1,2,3,4,5
    sum+=fac(i)
print(sum)
```

5 自然常数e


```python
# 自然常数e（约等于2.718281828459045）可以用奇数公式来计算近似值：1+1/1!+1/2!+1/3!+1/4!+1/5!+……+1/n!。给定一个n值，求出e的值，保留小数点后面10位  
# 例如：当n=5时，求出的e值为2.7166666667

m=int(input())
sum=1#初始为1
def fac(a):#阶乘函数
    if a==0:
        return 1
    else:
        return a*fac(a-1)

for i in range(1,m+1):
    sum+=1/fac(i)
print(sum)
```

6 航班定价（一）


```python
# 某航空公司采用的是按里程分段计算航班价格的模式。航班飞行距离小于等于100公里（含100公里）时，起步价为400元。
# 100公里至500公里（含500公里）的部分，每公里4元；500公里至2000公里（含2000公里）的部分，每公里3元；超过2000公里部分，每公里2元。
# 一个正整数n(0≤n≤40000),表示航班距离
m=int(input())
sum=0
if m<=100:
    sum=400
elif m>100 and m<=500:
    sum=400+(m-100)*4
elif  500<m<=2000:
    sum=400+1600+(m-500)*3
elif m>2000:
    sum=400+1600+4500+(m-2000)*2
print(sum)

```

# 套三

1 计算2的幂


```python
# 非负整数n，求2^n，即2的n次方

m=int(input())
num=2**m
print(num)
```

2 谁考了第k名*


```python
# 在一次考试中，现知道了每个学生的学号和成绩，求考第k名学生的学号和成绩。学生总数不超过200名。若成绩相同，按照录入顺序排名。
# 第一行有两个整数（n和 k），第一个表示学生人数n，第二个表示要求输出的第k名。其后有n行数据，每行包括一个学号（整数）和一个成绩（浮点数），中间用一个空格分隔。
# 输出第k名学生的学号和成绩，中间用空格分隔，成绩保留一个小数位。

m,k=map(int,input().split())
student=[]
for i in range(m):
    a,b=input().split()
    a=int(a)
    b=float(b)
    student.append((a,b))#作为元组
# 按照成绩排序，如果成绩相同则保持原有顺序（因为是从上到下依次添加的）
student.sort(key=lambda x: x[1])
# 输出第k名学生的学号和成绩，成绩保留一个小数位
print(f"{student[k-1][0]} {student[k-1][1]:.1f}")
```

3 求1+2+3+...


```python
# 用递归的方法求1+2+3+……+N的值。

m=int(input())
sum=0
while m>0:
    sum+=m
    m-=1
print(sum)
```

4 阶乘累加和


```python
# 给定一个正整数n(n≤100)，计算1!+2!+3!+……+n!的和值  
# 例如当n=5时，和值为153；当n=10时，和值为4037913

m=int(input())
def fac(n):#阶乘函数
    s=1
    while n>0:
        s*=n
        n-=1
    return s
sum=0
while m>0 :
    sum+=fac(m)
    m=m-1
print(sum)
```

5 出租车计费


```python
# 某市的出租车计费标准如下：起步里程小于等于3km时，起步费13元；超过起步里程小于等于15km以内的部分，单价为2.3元/km。超过15km的部分，单价加收50%的费用。
# 给定一个正整数距离s（s≤1000），求应付的费用，结果保留两位小数。  
# 例如，当s=3时，费用为13.00元；当s=5时，费用为17.60元；当s=18时，费用为50.95元

s=int(input())
float(sum)
if s<=3:
    sum=13
elif 3<s<=15:
    sum=13+(s-3)*2.3
elif 15<s:
    sum=13+(15-3)*2.3+(s-15)*2.3*1.5
print(f'{sum:.2f}')
```

6 各位数字的平方和*


```python
# 给定一个正整数n（1≤n≤10,000,000），求出它的各位数字的平方和  
# 例如n=123，平方和为14  
# 再比如n=235，平方和为38

m=input()
l=len(m)
sum=0
for i in range(l):
    digit=m[i]# 从字符串 n 中提取单个字符
    sum+=int(digit)**2
print(sum)

### 更简洁的方法
# n=input()
# s=sum(int(digit)**2 for digit in n)#这里出错是因为sum 函数被覆盖，有其他变量被命名为 sum，并且被赋予了一个浮点数值。
# print(s)
```

# 套四

1 温度表达转化


```python
# 利用公式C = 5*(F-32)/9进行计算转化，其中C表示摄氏温度，F表示华氏温度。  
# 题目输入华氏温度F，要求输出对应的摄氏温度C，要求精确到小数点后5位
# 输入一行，包含一个实数F，表示华氏温度。（100000000≥F≥ -459.67）
# 输出一行，包含一个实数，表示对应的摄氏温度，要求精确到小数点后5位。
# 例如F=41.0，C=5.00000

f=float(input())
c=5*(f-32)/9
print(f'{c:.5f}')
```

2 判断一个数能否同时被3和5整除


```python
# 判断一个数n 能否同时被3和5整除，如果能同时被3和5整除输出YES，否则输出NO。  
# 例如当n=30，输出：YES  
# 当n=81，输出：NO

m=int(input())
if m%3==0 and m%5==0:
    print('YES')
else:
    print('NO')
```

3 判断闰年


```python
# 判断某年是否是闰年。如果是闰年则输出Y，否则输出N。  
# 能被4整除的年份不一定是闰年，比如1900不是闰年，因为它能被100整除，而不能被400整除。2000年是闰年，因为它能被400整除。1984、1988是闰年，它们都能被4整除而不能被100整除

m=int(input())
if m%4==0:
    if m%100==0:
        if m%400==0:
            print('Y')
        else:
            print('N')
    else:
        print('Y')
else:
    print('N')
```

4 球弹跳高度的计算*


```python
# 一球从某一高度h落下(单位米，h≤1,000,000)，每次落地后反跳回原来高度的一半，再落下。编程计算气球在第10次落地时，共经过多少米? 第10次反弹多高？  
# 输出包含两行，第1行：到球第10次落地时，一共经过的米数。第2行：第10次弹跳的高度。  
# 输出结果保留小数点后4位。

h=float(input())
high_sum=h
for i in range(9):#注意：要减去一次
    h=h/2
    high_sum+=h*2
print(f'{high_sum:.4f}')#第十次落地的总高度
h=h/2#第十次反弹是第十次落地的高度的1/2
print(f'{h:.4f}')

```


```python
import math

height = int(input())
sum = height

for i in range(0, 9):#0,1...8
    sum = sum + height * pow(0.5, i)

print(f"{sum:0.4f}\n{height*pow(0.5,10):0.4f}")
```

5 统计字符数*


```python
# 给定一个由a-z这26个字符组成的字符串，统计其中哪个字符出现的次数最多,如果有多个字符出现的次数相同且最多，那么输出ascii码最小的那一个字符。

def most_frequent_char_and_count(s):
    # 创建一个字典来存储字符及其出现次数
    char_count = {}
    # 遍历字符串，统计每个字符的出现次数
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # 初始化最大次数和对应的字符
    max_count = 0
    most_frequent_char = ''
    # 遍历字典，找到出现次数最多的字符
    for char, count in char_count.items():
        if count > max_count or (count == max_count and ord(char) < ord(most_frequent_char)):#ord() 函数用于获取一个字符的ASCII码值
            max_count = count
            most_frequent_char = char
    # 输出结果：字符和出现次数，中间以空格分隔
    print(f"{most_frequent_char} {max_count}")
input_string = input()
most_frequent_char_and_count(input_string)
```

6 集合的划分*？


```python
# 设S是一个具有n个元素的集合，S＝〈a1，a2，……，an〉，现将S划分成k个满足下列条件的子集合S1，S2，……，Sk且满足：  
# 1．Si≠∅  
# 2．Si∩Sj＝∅ (1≤i，j≤k，i≠j)  
# 3．S1∪S2∪S3∪…∪Sk＝S  
# 则称S1，S2，……，Sk是集合S的一个划分
# 它相当于把S集合中的n个元素a1，a2，……，an放入k个(0 ＜ k ≤ n ＜ 30)无标号的盒子中，使得没有一个盒子为空
# 请你确定n个元素a1，a2，……，an放入k个无标号盒子中去的划分数S(n,k) 
# 输入：n和k
 

def stirling_second_kind(n, k):
    # 创建一个二维数组dp，dp[i][j]表示将i个元素划分到j个无标号盒子中的划分数
    dp = [[0] * (k + 1) for _ in range(n + 1)]  #这个二维列表有 n + 1 行和 k + 1 列，并且所有元素都初始化为 0。用于动态规划算法
    
    # 初始化：将0个元素划分到0个或更多盒子中的方式只有一种（即空划分）
    for j in range(k + 1):
        dp[0][j] = 1 if j == 0 else 0   #如果j == 0，则dp[0][j]被赋值为1；否则，它被赋值为0。即第一行为[[1][0][0]...]
    
    # 填充dp数组
    for i in range(1, n + 1):#第一行已经填充过
        for j in range(1, k + 1):#第一行列为[[1][0][0]...]
            # 两种情况：
            # 1. 将第i个元素放入一个已有的非空盒子中：S(n-1, j)
            # 2. 将第i个元素放入一个新的盒子中（此时该盒子变为非空）：S(n-1, j-1) * j（因为新盒子可以是j种选择中的任意一种）
            dp[i][j] = dp[i - 1][j] * j + dp[i - 1][j - 1]
            # dp[i - 1][j] 表示将 i−1 个元素划分到 j 个盒子的方法数。
            # 因为第 i 个元素可以放入 j 个已有的非空盒子中的任何一个，所以要乘以 j。
            # dp[i - 1][j - 1] 表示将 i−1 个元素划分到 j−1 个盒子的方法数
    
    return dp[n][k]

# 输入n和k
m = int(input())
k = int(input())

# 输出划分数
print(stirling_second_kind(m, k))
```


```python
def fun(n, m):
    if m > n or m == 0:
        return 0
    elif m == n or n == 1 or m == 1:
        return 1
    else:
        return fun(n - 1, m - 1) + m * fun(n - 1, m)


if __name__ == "__main__":
    list_1 = input().split()
    m = int(list_1[0])
    m = int(list_1[1])
    test = [[0] * (m + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(m + 1):
            if i == j:
                test[i][j] = 1
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if i >= j:
                test[i][j] = j * test[i-1][j] + test[i-1][j-1]
            else:
                test[i][j] = 0

    print(test[m][m])
```

# 套六

1 去除重复单词*


```python
# 给定一行由若干单词组成的字符串（总长度不超过1000个字符），单词之间以空格分隔。查找其中所有重复出现过的单词，并将这些单词删除，然后将剩下的单词按照原来的顺序输出。
# 题目保证至少有一个单词不重复。
# 例如给定字符串：This is a set of class templates that have two template parameters the char type char parameters
# 去除掉其中重复出现的单词，如char，parameters，将剩下的单词输出如下：This is a set of class templates that have two template the type

def remove_duplicates(sentence):
    # 拆分字符串为单词列表
    words = sentence.split()# 将输入的字符串按空格分割成单词列表
    # 统计单词频率*
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # 过滤重复单词*
    unique_words = [word for word in words if word_count[word] == 1]#推导式
    # 重新组合字符串*
    result_sentence = ' '.join(unique_words)
    # ' '.join(unique_words) 是一个字符串方法，用于将任何可迭代对象中的元素连接成一个单一的字符串，元素之间用指定的分隔符分隔。在这个例子中，分隔符是一个空格 ' '
    return result_sentence
input_sentence =input()
output_sentence = remove_duplicates(input_sentence)
print(output_sentence)


#核心部分
def remove_duplicates (sentence):
    words=sentence.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    unique_words = [word for word in words if word_count[word]==1]
    result_sentence=' '.join(unique_words)
    return result_sentence
```

2 围圈报数(约瑟夫环)*


```python
# 有ｎ个人依次围成一圈，从第１个人开始报数，数到第ｍ个人出列，然后从出列的下一个人开始报数，数到第ｍ个人又出列，…，
# 如此反复到所有的人全部出列为止。设ｎ个人的编号分别为1，2，…，n，打印出列的顺序。
# 输入格式: n和m。
# 输出格式: 出列的顺序。
# 输入示例:
# 4 17
# 输出示例:
# 1 3 4 2

def josephus_problem(n, m):
    # 初始化一个列表，表示所有人的编号
    people = list(range(1, n + 1))
    # 初始化索引和结果列表
    index = 0
    result = []
    # 当还有人在圈中时
    while people:   # while len(people) > 0:
        # 计算当前出列的人的索引
        index = (index + m - 1) % len(people)
        # 将出列的人添加到结果列表中
        result.append(people.pop(index))   
    return result
m, m = map(int, input().split())
print(" ".join(map(str, josephus_problem(m, m)))) 
print(*josephus_problem(m,m))
# 使用星号*作为前缀传递给print()函数时，你实际上是在执行一个操作，称为“解包”（unpacking）。
# 解包操作会将可迭代对象中的元素作为独立的参数传递给函数。
# 这意味着，如果有一个列表[a, b, c]，并且调用print(*[a, b, c])，它实际上等同于调用print(a, b, c)。


#核心部分
def josephus_problem(n,m):
    a=list(range(1,n+1))
    index=0
    result=[]
    while a:
        index=(index-1+m)%len(a)
        result.append(a.pop(index))
    return result
print(*josephus_problem(m,m))
```

3 通配符（一） *


```python
# Windows操作系统在查找文件时，文件名的匹配支持两种通配符：一种通配符是问号（?），它匹配任意的一个字符；一种通配符是星号（\*），它匹配任意长度的任意字符。
# 例如，有模板串：win\*，它能匹配windows，window，win，wind等正文串，但是不能匹配wifi，will，with，nowindows这些串。
# 再比如有模板串：“pro\*em，它能匹配problem，proem，probem等正文串，但是不能匹配pro，prem，roblem，problems这些串。
# 现在给定一个模板串，它仅含有一个星号通配符，以及若干个正文串，对于可以匹配成功的正文串，应输出Y；否则输出N。
# 输入格式: 第一行是一个模板串，它仅包含一个星号通配符。长度不超过20。串中只有大小写字母和数字以及通配符，没有空格等其它字符。
# 第二行是一个正整数n（1≤n≤100）,表示随后有n个正文串。
# 从第三行起，每行一个正文串，一共有n行，每个正文串的长度都不超过100，串中只有大小写字母和数字，没有空格等其它字符。
#  输入示例:
# go*od
# 6
# good
# gooood
# nogood
# goeods
# pogod
# goeood
#  输出示例:
# YYNNNY

def match_template(template, text):
    # 如果模板串长度小于正文串，则无法匹配，注意*号是匹配0或任意个，所以要-1
    if len(template) - 1 > len(text):
        return False
    # 检查前半部分字符是否匹配
    for i in range(len(template)):
        if template[i] == '*':
            break
        if template[i] != '*' and template[i] != text[i]:
            return False
    # 检查后半部分字符是否匹配
    for i in range(len(template) - 1, -1, -1):# (start,end,step)左闭右开，故此处end=-1，0也可以
        if template[i] == '*':
            break
        if template[i] != '*' and template[i] != text[i - (len(template) - len(text))]:
            return False
    return True

template = input().strip()#strip() 是字符串对象的一个方法，用于移除字符串前后的空白字符（默认行为，但也可以通过参数指定其他字符）
m = int(input().strip())
results = ''
for _ in range(m):# _是为了计数，无关紧要
    text = input().strip()
    if match_template(template, text):
        results += 'Y'
    else:
        results += 'N'
print(results)
```


```python
# 采用字符串方法：(最简便)

def check_match(pattern, text):
    prefix, suffix = pattern.split('*')  # 将模式字符串以星号分割为前缀和后缀
    # 检查正文串是否以prefix开头，并以suffix结尾
    # 在prefix和suffix之间可以有任意字符（包括空字符）
    return text.startswith(prefix) and text.endswith(suffix)

pattern = input().strip()
m = int(input().strip())
texts = [input().strip() for _ in range(m)]#推导式输入列表
results = [check_match(pattern, text) for text in texts]
# 将布尔值转换为'Y'或'N'
output = ''.join('Y' if result else 'N' for result in results)
print(output)
```

# 更多

1 A+B


```python
# 输入两个自然数, 输出他们的和

a,b=map(int,input().split())
print(a+b)
```

2 质数(素数)判断


```python
# 判断一个数是否为质数。质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数

m=int(input())
def is_prime(n):
    if n<2:
        return 'N'
    for i in range(2,n):
        if n%i==0:
            return 'N'
        else:
            return 'Y'
print(is_prime(m))
```

3 求阶乘的和


```python
# 给定正整数n，求不大于n（n≤13）的正整数的阶乘的和（即求1!+2!+3!+...+n!），输出阶乘的和

def jiechen(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a 
m=int(input())
sum=0
for i in range(1,m+1):
    sum+=jiechen(i)
print(sum)
```

4 简单排序*


```python
# 输入11个整数，如果第1个数为1，则将其中的第2至11个数升序排列；如果第1个数为0，则降序排列

m=[int(input()) for _ in range(11)]#换行输入,注意要转换成整数
if m[0]==1:#升序
    m[1:11].sort()
if m[0]==0:#降序
    m[1:11].sort(reverse=True)
for i in range(1,11):
    print(m[i],end=' ')

```

5 长度换算


```python
# 1英寸=2.54厘米
# 给定两个实数表示长度，第一个单位为英寸，第二个单位为厘米。要求将第一个长度换算成厘米输出，将第二个换算成英寸输出。结果保留2位小数
n,m=map(float,input().split())
n=n*2.54
m=m/2.54
print(f'{n:.2f}',end=' ')
print(f'{m:.2f}')

# 【输入样例】
# 25.3 12.4
# 【输出样例】
# 64.26 4.88
```

6 输出成绩档次


```python
# 给定一个分数n（n是0~100之间的整数），输出对应的成绩档次。各档次如下：
# 0~59分： failed
# 60~69分：pass
# 70~79分：medium
# 80~89分：good
# 90~100分：excellence

n=int(input())
if 0<=n and n<=59:
    print('failed')
if 60<=n and n<=69:
    print('pass')
if 70<=n and n<=79:
    print('medium')
if 80<=n and n<=89:
    print('good')
if 90<=n and n<=100:
    print('excellence')
```

7 字符串逆序*


```python
# 给定一个字符串，将其逆序输出。
# 例如，输入“abcd”，输出“dcba”；输入“Hello”，输出“olleH”
# 给定的字符串长度不超过1000，其中只包含大小写字母、数字、英文标点符号以及空格，不包含中文字符；回车符作为结束符，不计算在字符串内。

a=input()
a=a[::-1]
print(a)
```

8 身份证号脱敏*


```python
# 身份证号由18位的字符组成，其中第7位至第14位是持有人的出生日期，现在需要将这8位字符全部替换成“*”以便保护持有人的隐私，请编程实现。
# 例如有身份证号：43060219990515401X，替换之后为：430602********401X

n=input()
# n[6:14]='*'   #在Python中，字符串是不可变的，这意味着不能直接修改字符串中的某个字符或子串。
n = n[:6] + '********' + n[14:]
print(n)
```

9 判断能否被3，5，7整除


```python
# 给定一个整数，判断它能否被3，5，7整除，并输出以下信息：
#   1、能同时被3，5，7整除（直接输出3 5 7，每个数中间一个空格）；
#   2、只能被其中两个数整除（输出两个数，小的在前，大的在后。例如：3 5或者 3 7或者5 7，中间用空格分隔）；
#   3、只能被其中一个数整除（输出这个除数）；
#   4、不能被任何数整除，输出小写字符‘n’，不包括单引号。

# 【输入样例】
# 105
# 【输出样例】
# 3 5 7

n=int(input())
if n%3==0:
    print(3,end=' ')
if n%5==0:
    print(5,end=' ')
if n%7==0:
    print(7,end=' ')
if n%3!=0 and n%5!=0 and n%7!=0:
    print('n')
```

10 敏感信息屏蔽(一)


```python
# 现在给定一个身份证号码，要求屏蔽掉中间的第s~t位字符，其中1≤s≤t≤18，请输出处理后的号码。
# 例如身份证号：43060219990515401X，s=3,t=8，应输出：43******990515401X
# 再比如身份证号：362204199912207217，s=5,t=11，应输出：3622\****2207217
# 再比如身份证号：362204199912207217，s=1,t=5，应输出：*****4199912207217

# 【输入样例】
# 320103200002160776 6 10
# 【输出样例】
# 32010*****02160776

n,s,t=input().split()
s=int(s)
t=int(t)
n=n[:s-1]+'*'*(t-s+1)+n[t:]
print(n)
```

11 质数的和与积


```python
# 【输入格式】
# 一个不大于10000的正整数S，为两个质数的和。
# 【输出格式】
# 一个整数，为两个质数的最大乘积。数据保证有解。
# 【输入样例】
# 50
# 【输出样例】
# 589

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
max_num=0
for i in range(1,int(a/2)+1):#1~25
    b=i
    c=a-i
    if is_prime(b) and is_prime(c):
        if b*c>max_num:
            max_num=b*c
print(max_num)
```

12 身份号码解析


```python
# 我国18位的身份证号码第7-10位为出生年份，第11-12位为出生月份，第13-14位为出生日期，第17位代表性别，奇数为男，偶数为女。
# 给定一个合法的身份证号码，输出用户的出生年月日和性别，年月日为8位如“20220224”，男性是“male”,女性是“female”，输出项之间用空格隔开。
# 例如身份证号为：431121199912238732，出生日期为19991223，性别是male
# 再比如身份证号：460102199705232739，出生日期为19970523，性别是male
# 【输入格式】
# 一个18位的身份证号
# 【输出格式】
# 一行，解析出来的出生日期和性别，中间以空格分隔
# 【输入样例】
# 53212919980527272X
# 【输出样例】
# 19980527 female

n=input()
print(n[6:14],end=' ')
if int(n[16])%2==0:
    print('female')
else:
    print('male')
```

13 合并数据(一)*


```python
# 有两个整数序列，将其合并，去除其中重复元素，得到一个严格单调递增序列。
# 例如有序列2,4,2,1,4和1,5,4,5,5,2，将其合并后得到的递增序列为：1,2,4,5
# 又比如有序列：1,6,3,6,1,1,7 和 3,7,8,7,1,8,5,8，合并后得到的递增序列为：1,3,5,6,7,8
# 【输入格式】
# 一共有4行，第一行是一个整数m（1≤m≤500），表示第一个序列的元素数目。
# 第二行是m个正整数，中间用空格分隔。第三行是一个整数n（1≤n≤500），表示第二个序列的元素数目，第四行是n个正整数，中间用空格分隔
# 【输出格式】
# 一行数据，合并后升序排列的元素，中间以空格分隔
# 【输入样例】
# 6
# 6 2 4 2 1 5
# 8
# 6 7 2 8 6 6 7 1
# 【输出样例】
# 1 2 4 5 6 7 8

m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
a.extend(b)
### set作用自动去重,排序
a=set(a)
print(*a)
```

14 交水费


```python
# 小明家住湘潭，按照湘潭的水费政策实行阶梯水价。第一档水量：月用水量15吨以下（含15吨）；第二档水量：月用水量15吨至22吨（含22吨）；第三档水量：月用水量22吨以上。
# 第一档水价2.58元/吨，第二档水价3.34元/吨，第三档水价4.09元/吨。
# 请你帮小明算一下，他每个月应交的水费。水费是以分为单位的整数。
# 比如用水量15吨，应交水费3870； 若用水量20吨，应交水费5540；若用水量25吨，应交水费7435。

# 【输入样例】
# 24
# 【输出样例】
# 7026

n=int(input())
total=0
if n<=15:
    total+=258*n
if n>15 and n<=22:
    total+=258*15+334*(n-15)
if n>22:
    total+=258*15+334*7+409*(n-22)
print(total)

```

15 成绩排序


```python
# 给定n（1≤n≤100）个学生的姓名和成绩，按照成绩从高到低排序输出。学生的姓名不会重复，如果有成绩相同的，则原来在名单中靠前的同学仍然排列在前面。
# 例如有一个班的成绩如下：
# Deirdr 89
# Sheil 50
# Cynthi 63
# Rene 66
# Emm 46
# Myrn 42
# Nicol 63
# Prudenc 66
# Adel 79
# 排序之后为：
# Deirdr 89
# Adel 79
# Rene 66
# Prudenc 66
# Cynthi 63
# Nicol 63
# Sheil 50
# Emm 46
# Myrn 42
# 注意：Rene排在Prudenc之前，Cynthi排在Nicol之前。


# 【输入样例】
# 7
# Aaro 100
# Colto 65
# Chas 83
# Ada 60
# Josia 94
# Zavie 100
# Dieg 81
# 【输出样例】
# Aaro 100
# Zavie 100
# Josia 94
# Chas 83
# Dieg 81
# Colto 65
# Ada 60

n=int(input())
a=[]
for _ in range(n):
    name,score=input().split()
    score=int(score)
    a.append((name,score))

a=sorted(a,key=lambda x:x[1],reverse=True)
for name,score in a:
    print(f'{name} {score}')

```

16  只选一门课的学生(一)*


```python
# 学校开放了两门选修课，规定每位同学只能选择其中一门。但是有些同学不遵守规定，同时选择了两门课程，现在选课名单汇总出来了，
# 请你根据名单将只选择了一门课程的同学挑选出来，并按照字典顺序升序排列。
# 例如，选择了A课程的同学有：Christia Natha Elija Ale Loga Jame Gabrie，
# 选择了B课程的同学有：Joh Natha Elija Ale Rya Hayde，
# 只选择一门课的同学是：Christia Gabrie Hayde Jame Joh Loga Rya
# 又比如，选择了A课程的同学有：Thoma Camero Col Austi Jesu，
# 选择了B课程的同学有：Thoma Brya Lia Austi Trista，
# 只选一门课的同学是：Brya Camero Col Jesu Lia Trista

# 【输入格式】
# 输入数据一共有4行。第一行是一个正整数m（1≤m≤100）表示选择A课程的同学数目，第二行是所有选择A课程的同学姓名，中间以空格分隔。
# 第三行是一个正整数n（1≤n≤100）表示选择B课程的同学数目，第四行是所有选择B课程的同学姓名，中间以空格分隔。
# 【输出格式】
# 一行，所有只选择一门课程的同学姓名，中间以空格分隔，按照字典顺序升序排列

# 【输入样例】
# 6
# Thoma Austi Lia Sea Trista Brya
# 7
# Brya Camero Austi Lia Hunte Trista Jesu
# 【输出样例】
# Camero Hunte Jesu Sea Thoma

m=int(input())
a=input().split() 
print(a)
n=int(input())
b=input().split() 
c=[]
for i in a:
    if i not in b:
        c.append(i)
for j in b:
    if j not in a:
        c.append(j)
c.sort()
print(*c)
#for i in c:
    #print(i,end=' ')
```


```python
m = int(input())
students_A = set(input().split())
n = int(input())
students_B = set(input().split())

# 找出只选择了一门课程的学生
only_A = students_A - students_B
only_B = students_B - students_A

# 合并两组学生并排序
unique_students = sorted(only_A | only_B)

# 输出结果
print(' '.join(unique_students))
```

17 对称素数


```python
# 有这样一种整数，它自身是素数，翻转过来之后还是个素数，这种数被称为对称素数。
# 比如157是素数，翻转过来之后的751也是素数。
# 给定一个区间[s,t]，其中10≤s≤t≤1,000,000，求出该区间内所有的对称素数的个数。
# 如果一个素数和它对称的素数同时出现在这个区间中，那么仍然应该计算两次，比如[10,99]中17和71就出现了两次（分别是17，71 和71,17）。
# 在[10,20]中，这样的对称素数有3对；在[10,100]中，这样的对称素数有9对。

# 【输入格式】
# 一行，两个正整数s和t，表示区间的起始值和终止值，中间以空格分隔
# 【输出格式】
# 一个正整数，表示该区间内对称素数的数目

# 【输入样例】
# 100 200
# 【输出样例】
# 12

def is_prime(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

s,t=map(int,input().split())
count=0
for i in range(s,t+1):
    j=str(i)
    j=j[::-1]
    j=int(j)
    if is_prime(i) and is_prime(j):
        count+=1
print(count)

```

18 奇偶数双端排序(一)


```python
# 给定一个长度为n（n≤1000）的整数序列，要求将其中所有的奇数按照从大到小的顺序排列在左边，所有的偶数按照从小到大的顺序排列在右边。
# 例如，有序列：801 309 612 739 480 756 207 452 103 918
# 排序完成后为：801 739 309 207 103 452 480 612 756 918
# 再比如序列：16 808 999 54 114 776 252 859 524 362 163 540 354
# 排序完成后为：999 859 163 16 54 114 252 354 362 524 540 776 808

# 【输入格式】
# 输入为两行，第一行是一个正整数n，表示原始序列的长度；第2行是要排列的n个正整数，以空格分隔
# 【输出格式】
# 输出为一行，排序完成后的结果，数据之间用空格分隔

# 【输入样例】
# 9
# 519 894 570 20 926 669 818 811 405
# 【输出样例】
# 811 669 519 405 20 570 818 894 926

n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
b.sort()
c.sort(reverse=True)
c.extend(b)
print(*c)
```

19 完整的选手信息(一)*?


```python
# 有n（1≤n≤50）名选手参加比赛，最后有m（1≤m≤n）名选手获奖。在报名名单中，包含有每位选手的编号和姓名，其中编号是4位数字编号，每位选手的编号都是唯一的，姓名有可能重复。
# 在比赛过程中，选手是匿名参加比赛，比赛名单中只有选手编号而没有姓名。比赛完成后，前m名可以获奖，并且公示出来。
# 由于比赛名单中只含有编号和名次，因此需要将报名名单中的选手姓名合并到公示名单中来，这样公示名单中就含有编号、姓名和名次三项信息。
# 比如有8名选手参赛，报名名单如下：
# 1001 古力
# 1002 张华东
# 1003 陈鹏程
# 1004 宋连军
# 1005 张玉顺
# 1006 翟鹏展
# 1007 申科
# 1008 杨啸天
# 比赛结果如下：
# 1001 8
# 1002 6
# 1003 1
# 1004 2
# 1005 5
# 1006 3
# 1007 4
# 1008 7
# 最后前4名选手可以获奖，公示名单如下：
# 1003 陈鹏程 1
# 1004 宋连军 2
# 1006 翟鹏展 3
# 1007 申科 4

# 【输入格式】
# 第一行是两个整数n和m，其中n表示报名选手的人数，m表示最终获奖的人数，中间以空格分隔。
# 第2行至第n+1行，每行一个报名选手的信息，分别是4位数的选手编号和选手姓名，中间以空格分隔。
# 第n+2行至2n+1行，每行一个选手的比赛结果，分别是选手编号和选手排名，中间以空格分隔。
# 【输出格式】
# 一共有m行数据，每行一个选手的全部信息，分别是选手编号、选手姓名和比赛名次，中间以空格分隔，并按照比赛名次从前往后排列。

# 【输入样例】
# 6 3
# 1001 孙智超
# 1002 王利彤
# 1003 吕金富
# 1004 柯少琦
# 1005 沈福麟
# 1006 尚日强
# 1001 1
# 1002 3
# 1003 6
# 1004 4
# 1005 2
# 1006 5
# 【输出样例】
# 1001 孙智超 1
# 1005 沈福麟 2
# 1002 王利彤 3

n,m=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    num,name=input().split()
    a.append((int(num),name))
for _ in range(n):
    num,range=input().split()
    b.append((int(num),range))

name_dict = {num: name for num, name in a}
final_list = []
for num, rank in sorted(b, key=lambda x: int(x[1])):
    name = name_dict[num]
    final_list.append((num, name, rank))
for i in range(m):
    num, name, rank = final_list[i]
    print(f"{num} {name} {rank}")
```


```python
n, m = map(int, input().split())
# 使用字典记录选手编号和姓名
contestant_dict = {}
for _ in range(n):
    number, name = input().split()
    contestant_dict[number] = name
# 读取比赛结果，并存储在列表中，同时记录排名
results = []
for _ in range(n):
    number, rank = input().split()
    results.append((number, int(rank))) # 元组
# 根据排名对比赛结果进行排序
results.sort(key=lambda x: x[1])
# 选择排名小于等于m的选手，序号是从0开始，所以不需要m+1
winners = results[:m]
# 输出公示名单
for number, rank in winners:
    name = contestant_dict[number]
    print(number, name, rank)
```

20 输出重复单词*!


```python
# 给定一行由若干单词组成的字符串（总长度不超过1000个字符），单词之间以空格分隔。查找其中所有重复出现过的单词，并将这些单词挑选出来，按照原来的顺序输出（只输出一次）。
# 题目保证至少有一个单词重复出现。
# 例如给定字符串：This is a set of class templates that have two template parameters the char type char parameters
# 其中重复出现的单词有“parameters”和“char”，将其按照第一次出现的顺序输出如下：parameters char
# 再例如给定字符串：The iostream library is an object oriented library that provides input and output functionality using streams
# 找到其中的重复单词，输出如下：library

# 【输入格式】
# 一行，一个字符串，只有英文单词，单词间以空格分隔。
# 【输出格式】
# 一行，重复的单词，以空格分隔，其顺序是在原句子中第一次出现的顺序。

# 【输入样例】
# Once a file stream is used to open a file any input or output operation performed on that stream is physically reflected in the file
# 【输出样例】
# a file stream is

a=input().split()
b={}
for i in a:
    if i in b:
        b[i]+=1
    if i not in b:
        b[i]=1
for i in b:
    if b[i]>1:
        print(i,end=' ')
```


```python
# 将字符串分割成单词列表
words = input().split()
# 初始化一个空列表来存储重复的单词
duplicate_words = []
# 遍历单词列表
for word in words:
    # 如果单词出现次数大于1，并且尚未添加到列表中
    if words.count(word) > 1 and word not in duplicate_words:
        duplicate_words.append(word)
# 输出重复的单词，按照它们在原句子中第一次出现的顺序
print(' '.join(duplicate_words))
```

21 汇率计算


```python
# 各种货币之间可以根据市场汇率进行兑换。如果两种货币之间没有直接汇率，可以通过第三方货币进行计算。比如1美元兑换6.9元人民币，1元人民币兑换1.1港币，可以计算出1美元兑换7.59港币。
# 再比如1英镑兑换8.8元人民币，1元人民币兑换0.217澳元，则1英镑可以兑换1.91澳元。
# 现有A、B、C三种货币，给定A兑换B和B兑换C的汇率，求出A兑换C的汇率。

# 【输入格式】
# 一行，两个浮点数，中间以空格分隔。第一个数表示一个单位的A货币兑换多少B货币，第二个数表示一个单位的B货币兑换多少C货币
# 【输出格式】
# 一个浮点数，表示一个单位的A货币兑换多少C货币，保留4位小数。

# 【输入样例】
# 7.01 2.34
# 【输出样例】
# 16.4034

a,b=map(float,input().split())
print(f'{a*b:.4f}')
```

22 去除重复单词 


```python
# 给定一行由若干单词组成的字符串（总长度不超过1000个字符），单词之间以空格分隔。查找其中所有重复出现过的单词，并将这些单词删除，然后将剩下的单词按照原来的顺序输出。题目保证至少有一个单词不重复。
# 例如给定字符串：This is a set of class templates that have two template parameters the char type char parameters
# 去除掉其中重复出现的单词，如“char”“parameters”，将剩下的单词输出如下：This is a set of class templates that have two template the type
# 再例如给定字符串：The iostream library is an object oriented library that provides input and output functionality using streams
# 去除其中的重复单词，输出如下：The iostream is an object oriented that provides input and output functionality using streams

# 【输入格式】
# 一行，一个字符串，只有英文单词，单词间以空格分隔
# 【输出格式】
# 一行，处理之后剩下的单词，以空格分隔

# 【输入样例】
# Once a file stream is used to open a file any input or output operation performed on that stream is physically reflected in the file
# 【输出样例】
# Once used to open any input or output operation performed on that physically reflected in the

a=input().split()
b={}
for i in a:
    if i in b:
        b[i]+=1
    if i not in b:
        b[i]=1
for i in b:
    if b[i]==1:
        print(i,end=' ')
```


```python
# 将字符串分割成单词列表
words = input().split()
# 创建一个空列表来存储只出现一次的单词
unique_words = []
# 遍历单词列表，只添加出现一次的单词
for word in words:
    if words.count(word) == 1:
        unique_words.append(word)
# 将只出现一次的单词列表转换为字符串并输出
print(' '.join(unique_words))
```

23 右高阶素数*


```python
# 有这样一种整数，它自身是素数，它有n位，如果它的低n-1位也是素数，则这种数被称为右高阶素数。
# 比如11001983是素数，它有8位，它的低7位1001983也是素数。
# 类似的数据还有：14951和4951，14969和4969，11001563和1001563等。
# 有一种特殊情况需要注意：10043是素数，它的低5位是0043，尽管43是素数，但由于它只有两位，所以这种不能算右高阶素数。
# 给定一个区间[s,t]，其中10≤s≤t≤1,000,000，求出该区间内所有的右高阶素数的个数。
# 在[100,200]中，这样的右高阶素数有7个；在[200,300]中，这样的右高阶素数有6个。

# 【输入格式】
# 一行，两个正整数s和t，表示区间的起始值和终止值，中间以空格分隔
# 【输出格式】
# 一个正整数，表示该区间内右高阶素数的数目

# 【输入样例】
# 301 400
# 【输出样例】
# 14

def is_prime(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def is_right(a): #10043
    if not is_prime(a):#不是素数
        return False
    l=len(str(a)) #5
    a=a%(10**(l-1)) #10043%10000=43
    if a<(10**(l-2)): #0043<1000
        return False
    if is_prime(a): #仍是素数
        return True

s,t=map(int,input().split())
count=0
for i in range(s,t+1):
    if is_right(i):
        count+=1
print(count)
```

24 奇偶数双端排序(二)


```python
# 给定一个长度为n（n≤1000）的整数序列，要求将其中所有的偶数按照从大到小的顺序排列在左边，所有的奇数按照从小到大的顺序排列在右边。
# 例如，有序列：801 309 612 739 480 756 207 452 103 918
# 排序完成后为：918 756 612 480 452 103 207 309 739 801
# 再比如序列：16 808 999 54 114 776 252 859 524 362 163 540 354
# 排序完成后为：808 776 540 524 362 354 252 114 54 16 163 859 999

# 【输入格式】
# 输入为两行，第一行是一个正整数n，表示原始序列的长度；第2行是要排列的n个正整数，以空格分隔
# 【输出格式】
# 输出为一行，排序完成后的结果，数据之间用空格分隔

# 【输入样例】
# 9
# 519 894 570 20 926 669 818 811 405
# 【输出样例】
# 926 894 818 570 20 405 519 669 811

a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
b.sort(reverse=True)
c.sort()
b.extend(c)
print(*b)
```

# 题库1

1006 计算(a+b)*c的值


```python
# 计算(a+b)*c的值
a,b,c=map(int,input().split())
print((a+b)*c) 
```

1008 温度表达转化


```python
# 利用公式C = 5*(F-32)/9进行计算转化，其中C表示摄氏温度，F表示华氏温度。
# 题目输入华氏温度F，要求输出对应的摄氏温度C，要求精确到小数点后5位。

f=float(input())
c=5*(f-32)/9
print(f'{c:.5f}')
```

1011 打印ASCII码


```python
# 输入一个除空格以外的可见字符（可以用键盘输入的字符），输出其ASCII码。
a=input()
print(ord(a))#ord函数获取ASCII码
```

1326 简单排序*


```python
# 输入10个整数，如果第1个数为1，则将其中的第2至10个数升序排列；如果第1个数为0，则降序排列。
a=list(map(int,input().split()))
if a[0]==1:
    a=sorted(a[1:])
    print(*a)
elif a[0]==0:
    a=sorted(a[1:],reverse=True)#要用sorted方法
    print(*a)

# 1 8 9 5 4 7 6 3 2 0 10
# 0 2 1 5 6 3 4 9 8 7 10

```

1453 矩阵中的最小元素*


```python
# 给定一个5X5的整数矩阵，找出其中最小的元素，输出所在的行号、列号和元素值，其中行号和列号都从0开始。

a = [[None for _ in range(5)] for _ in range(5)]
inputs = list(map(int,input().split()))#列表
for i in range(5):
    for j in range(5):
        a[i][j] = inputs[i * 5 + j]
min_value = float('inf')  # 使用正无穷大作为初始值更安全
i1, ji = 0, 0  # 初始化最小值的行号和列号
for i in range(5):
    for j in range(5):
        if a[i][j] < min_value:
            min_value = a[i][j]
            i1 = i
            ji = j
print(i1, ji, min_value)

# 96 81 40 67 48
# 46 98 65 92 13
# 68 20 25 47 81
# 49 78 73 13 44
# 1 2 79 96 97

# 4 0 1
```

1314 素数求和


```python
# 给定n（n≤100）个正整数，所有正整数均≤1000000；求其中所有素数的和。
# 例如给定序列： 2 3 4 5 6，素数和为：10
# 给定序列： 3 4 5 6 7， 素数和为：15
# 给定序列： 12 19 23 35 68 71， 素数和为： 113

m=int(input())
a=list(map(int,input().split()))
def is_prime(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
             return False
    return True
sum=0
for i in range(m):
    if is_prime(a[i]):
        sum+=a[i]
print(sum)
# 6
# 14 5 69 51 89 31
#输出 125
```

1263 求阶乘的和


```python
# 给定正整数n，求不大于n（n≤13）的正整数的阶乘的和（即求1!+2!+3!+…+n!），输出阶乘的和。

m=int(input())
def jiechen(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
sum=0
for i in range(1,m+1):
    sum+=jiechen(i)
print(sum)
```

1016 判断闰年


```python
m=int(input())
def is_runyear(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return 'Y'
            else:
                return 'N'
        else:
            return 'Y'
    else:
        return 'N'
print(is_runyear(m))
```

1444 特殊数列求和*


```python
# 给定两个均不超过9的正整数，较小的数作为a，较大的数作为n，要求编写程序求 a + aa + aaa +… + aaa…aa(n个a)之和。
# 例如：a =2,n=5时，2 + 22 + 222 + 2222 + 22222 =24690，输出结果24690

a,n=map(int,input().split())
if a>n:
    flag=a
    a=n
    n=flag
m=0
total=0
for i in range(n):
    m+=a*(10**i)
    total+=m
print(total)
```

1445 小明爬楼*


```python
# 假设一段楼梯共n(1≤n≤64)个台阶，小明一步最多能上3个台阶（当然也可以走一个或者两个台阶），小明上这段楼梯一共有多少种方法?
# 例如：n=5时，得到(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 1, 3), (1, 2, 1, 1), (1, 2, 2), 
# (1, 3, 1), (2, 1, 1, 1), (2, 1, 2), (2, 2, 1), (2, 3), (3, 1, 1), (3, 2) 共 13种方法。

m=int(input())
# 我们可以定义一个数组 dp，其中 dp[i] 表示小明上到第 i 个台阶的方法数。
# dp[1] = 1（只有一种方法：上1个台阶）
# dp[2] = 2（有两种方法：上1个台阶两次，或者直接上2个台阶）
# dp[3] = 4（有四种方法：1+1+1, 1+2, 2+1, 3）
# 对于 i > 3 的情况，使用以下递推公式：
# dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# 这个公式表示，小明上到第 i 个台阶的方法数等于他上到第 i-1、i-2 和 i-3 个台阶的方法数之和，因为他可以从这三个位置分别迈一步到达第 i 个台阶。
dp=[0]*(n+1)# 创建长度n+1的列表
dp[1]=1
dp[2]=2
dp[3]=4
if n>3:
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
print(dp[n])
```

1289 身份证号码验证（一）*


```python
# 居民身份证是18位字符的编码，每个人的编码都是唯一的，校验规则如下：
# ∑（ai*wi）mod 11 = 1
# i表示号码字符从左至右包括校验码字符在内的位置序号；ai表示第i位置上的号码字符值；Wi表示第i位置上的加权因子。
# 即将各位上的数值乘上位权之和对11取余，余数为1则表示该编码正确。注意：如果最后一位校验码是“X”或“x”，则代表该校验码的数值为10。
# 各位的权值依次是：7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2，1

# 例如某身份证号码为：370683198901117657，这是正确的编码。
# 又比如身份证号：43038120051120041X，这是正确的编码，
# 还比如身份证号：150402200002010020，这是正确的编码。
# 又如某号码为：470683198902117657，这是错误的编码。

# 输入：第一行是一个数字n（1≤n≤150），表示后面有n个号码需要判断
# 从第二行起，每行一个18位的字符串，表示要判断的身份证号码，一共有n行
# 输出一个整数值，表示正确的身份证号码的个数

def is_right(id_number):
    # 权值列表
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
    # 计算校验和，将'X'或'x'视为10
    total = sum(int(num if num.isdigit() else 10) * weight for num, weight in zip(id_number, weights))
    # 列表推导式，zip 函数生成元组序列
    # for循环遍历 zip 函数生成的元组序列。在每次迭代中，num 将被赋值为id_number中的一个字符，weight 将被赋值为weights中的一个整数
    # num.isdigit() 方法检查 num 是否是一个数字
    return total % 11 == 1

def count_right(id_number):
    # 计算正确的身份证号码数量
    return sum(is_right(id_num) for id_num in id_number)

n = int(input())
id_numbers = [input().strip() for _ in range(n)]
print(count_right(id_numbers))

# 4
# 430321200506200105
# 430321200505070050
# 430302200512290036
# 43038120050824012X

```

1403 IP地址转换（一）


```python
# IP地址是用“.”分割的四段整数，每段值都在0~255之间。一般情况下这四段整数用十进制数表示，如：204.148.21.114。
# 实际上，它也可以用二进制表示，如：11001100.10010100.00010101.01110010。现在给定用二进制表示的IP地址，请转换成十进制表示的IP地址输出。
# 例如给定一个IP地址：11000000.10101000.00000000.00000010，对应的十进制IP值为：192.168.0.2


ip=input().split('.')# 分割二进制IP地址为四段
zhuan_ip=[int(i,2) for i in ip]# 将每段二进制字符串转换为十进制整数
# int(i,2) 这部分代码将i转换为一个十进制整数。这里，int函数的第二个参数2指定了转换的基数，即告诉Python这个字符串是一个二进制数。
decimal_ip='.'.join(map(str,zhuan_ip)) # 将四段十进制整数用'.'连接成十进制IP地址
#注意要转换成字符串再用.join方法
print(decimal_ip)
# 输出: 192.168.0.2
```

1408 查找回文数


```python
# 回文数是一种特殊的数，从左边读和从右边读是一样的，比如123321就是一个回文数。
# 现在给定一个正整数n（n≤54），编程求出一个回文数，要求该回文数的各位数字之和等于n，且该回文数大于10000，小于等于99999。
# 如果有多个满足条件的回文数，输出最小的这个；如果没有满足条件的回文数，输出"Not found"。

# 例如，给定n=16，满足条件的最小回文数是13831。
# 再比如给定n=10，满足条件的最小回文数是10801。

def is_palindrome(num):
    """检查一个数是否是回文数"""
    num = str(num)
    return num == num[::-1]

def digit_sum(num):
    """计算一个数的各位数字之和"""
    return sum(int(digit) for digit in str(num))

def find_palindrome(n):
    """找出满足条件的回文数"""
    for i in range(10001, 100000):  # 在10001到99999之间查找
        if is_palindrome(i) and digit_sum(i) == n:
            return i
    return "Not found"
n=int(input())
print(find_palindrome(n))  # 输出 13831

```

# 题库2

1 星期几 (三)


```python
# 给定一个由年月日描述的日期，求出它是星期几。
# 要解决这个问题，需要求出这一天是当年的第几天，这需要先解决闰年问题。
# 然后可以利用下面这个公式计算某一天星期几：
# s=(y-1)+[(y-1)/4]-[(y-1)/100]+[(y-1)/400]+d

# 式中的y表示年份year，式中的d表示当天是这一年中的第几天，1月1号是第一天。
# 式中的[x]表示高斯函数，为向下取整。例如[3.0]=3，[4.9]=4
# 求出s之后，对7取余，余数为0表示星期天，余数为1~6表示星期一~星期六。

# 例如1949年10月1日，可算得s=2694，对7取余得6，这一天是星期六；
# 例如2000年1月1日，可算得s=2484，对7取余得6，这一天是星期六；
# 例如2024年6月25日，可算得s=2690，对7取余得2，这一天是星期二。

# 给出一个由年月日组成的日期，如“2024 5 27”，表示2024年5月27号，求出它是星期几，输出对应的数字（0表示星期天）

# 输入样例
# 2024 5 27
# 输出样例
# 1

a=list(map(int,input().split()))

def is_runyear(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_in_year(y,m,d):
    day=d
    if m>1:
        day+=31
    if m>2 and is_runyear(y):
        day+=29
    elif m>2 and not is_runyear(y):
        day+=28
    if m>3:
        day+=31
    if m>4:
        day+=30
    if m>5:
        day+=31
    if m>6:
        day+=30
    if m>7:
        day+=31
    if m>8:
        day+=31
    if m>9:
        day+=30
    if m>10:
        day+=31
    if m>11:
        day+=31
    return day

def week(y,day):
    s=(y-1)+int((y-1)/4)-int((y-1)/100)+int((y-1)/400)+day
    return s%7

day=day_in_year(a[0],a[1],a[2])
if week(a[0],day)==0:
    print(7)
else:
    print(week(a[0],day))
```

2 找出符合要求的数字（四）


```python
# 给定n（1≤n≤200）个正整数，找出同时符合下面两个条件的数：
# （1）能被7整除；
# （2）包含数字7。
# 例如有5个数字：63,77,83,66,70，符合要求的数字依次是：77,70。
# 再例如有6个数字：35,49,147,83,175,56，符合要求的数字是：147,175。

# 输入格式
# 两行，第一行是一个正整数n，表示后面有n个数据需要处理。第二行是n个要处理的数据，数据之间以空格分隔。

# 输出格式
# 一行，按照上述要求找到的数据，中间以空格分隔。这些数据的顺序必须与输入顺序一致。
# 如果没有一个符合要求的数据，则输出“none”

# 输入样例
# 5
# 39  52  21  147  86
# 输出样例
# 147

n=int(input())
a=list(map(int,input().split()))
def is_right(a):
        if a%7==0 and  '7' in str(a):
            return True
        else :
            return False       
flag=0
for i in a:
    if is_right(i):
        flag=1
        print(i,end=' ')
if flag==0:
     print('none')
```

3 阿尔法乘积*


```python
# 计算一个整数的阿尔法乘积。对于一个整数x来说，它的阿尔法乘积是这样来计算的：如果x是一个个位数，那么它的阿尔法乘积就是它本身；
# 否则的话，x的阿尔法乘积就等于它的各位非0的数字相乘所得到的那个整数的阿尔法乘积。例如：4018224312的阿尔法乘积等于8，它是按照以下的步骤来计算的：
# 4018224312 → 418224312 → 3072 → 372 → 42 → 4*2 → 8
# 编写一个程序，输入一个正整数（该整数不会超过6,000,000），输出它的阿尔法乘积。

# 输入只有一行，即一个正整数。
# 输入样例
# 4018224312 
# 输出样例
# 8


def alpha(n):
    # 去除整数中的所有零
    while '0' in str(n):
        n = ''.join(filter(lambda x: x != '0', str(n)))#filter过滤函数接受两个参数：一个函数和一个可迭代对象。
        # lambda x: x != '0'是一个匿名函数，它接受一个字符x作为输入，并返回一个布尔值，表示x是否不等于'0'。如果x不等于'0'，lambda函数返回True，否则返回False。
        # filter函数会遍历str(n)中的每个字符，并将lambda函数返回True的字符保留下来，形成一个新的迭代器。
    # 如果n是个位数，则返回n
    if len(str(n)) == 1:#1,2,3...9
        return int(n)
    # 否则，计算各位数字的乘积，并递归调用alpha
    product = 1
    for digit in str(n):
        product *= int(digit)
    
    return alpha(product)


x = int(input().strip())
print(alpha(x))

```

4 棋盘*


```python
# 小蓝拥有 n × n 大小的棋盘，一开始棋盘上全都是白子。
# 小蓝进行了 m 次操作，每次操作会将棋盘上某个范围内的所有棋子的颜色取反 (也就是白色棋子变为黑色，黑色棋子变为白色)。
# 请输出所有操作做完后棋盘上每个棋子的颜色。
# 输入的第一行包含两个整数 n, m，用一个空格分隔，表示棋盘大小与操作数。
# 接下来 m 行每行包含四个整数 x1, y1, x2, y2，相邻整数之间使用一个空格分隔，表示将在 x1 至 x2 行和 y1 至 y2 列中的棋子颜色取反。
# 1 ≤ n, m ≤ 200 ，1 ≤ x1 ≤ x2 ≤ n ，1 ≤ y1 ≤ y2 ≤ m 。
# 输出 n 行，每行 n 个 0 或 1 表示该位置棋子的颜色。如果是白色则输出 0，否则输出 1 。
# 输入样例
# 3 3
# 1 1 2 2
# 2 2 3 3
# 1 1 3 3
# 输出样例
# 001
# 010
# 100


n, m = map(int, input().split())    
# 初始化棋盘为全白（0表示白色）
board = [[0] * n for _ in range(n)]
# 执行m次操作
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())  
    # 将指定范围内的棋子颜色取反
    for i in range(x1 - 1, x2):  # 注意棋盘索引从0开始，所以x1-1
        for j in range(y1 - 1, y2):  # 同理，y1-1
            board[i][j] = 1 - board[i][j]  # 取反操作：0变1，1变0
for row in board:
        print(''.join(map(str, row)))
```

5 发金牌


```python
# 运动会开了 n 天，第 n 天发出金牌 m 枚。第一天发金牌 1 枚，第二天发金牌前一天的两倍加一枚，以后每天都照此办理。
# 开了 n 天，第 n 天发了 m 块金牌。比如 n = 3，得到 7，如 n = 9，得到 511。
# 你能编个简单的小程序求算 m 吗？

# 输入格式
# 输入一个整数 n，表示运动会开的天数。
# 输出格式
# 计算对应发的奖牌数 m。

n=int(input())
m=0
for i in range(n):
    m=2*m+1
print(m)
```

6 勾股数*


```python
# 如果三个正整数 a,b,c，满足 a^2+b^2=c^2 ，而且 1≤a≤b≤c，我们就将 a,b,c 组成的三元组 (a,b,c) 称为勾股数。你能通过编程，数数有多少组勾股数，能够满足 c≤n 吗？

# 输入格式
# 输入一行，为一个整数 n,1 < n < 1000
# 输出格式
# 输出一行，包含一个整数 C，表示有 C 组满足条件的勾股数。
# 例如当n = 5,满足 c≤5 的勾股数只有 (3,4,5) 一组。
# 例如当n = 13,满足 c≤13 的勾股数有 (3,4,5),(6,8,10),(5,12,13) 三组。

n=int(input())
def gougu(n):
    count=0
    for a in range(1,n+1):
        for b in range(a,n+1):
            c_sqa=a**2+b**2
            c=int(c_sqa**0.5)
            if c**2==c_sqa and c<=n:
                count+=1
    return count
print(gougu(n))

```

7 求均值和方差


```python
# 分别计算每一个变量与平均值的差值的平方，然后累加求和再求出平均值。它的统计公式为：
# σ2=∑(X-μ)2/N
# 其中X是每一个变量的值，μ是所有变量的平均值，N是总体数目。
# 例如有5个数据分别是：9 9 2 8 9，它的平均值为7.4，方差值为：7.44
# 再例如有10个数据分别为：4 6 4 4 2 9 6 10 0 8，它的平均值为5.3，方差值为：8.81。
# 题目给定n（1≤n≤100）个正整数，求它们的平均值和方差值，结果保留两位小数

# 输入格式
# 两行，第一个是一个正整数n（1≤n≤100），表示需要处理的数据有n个。第二行是n个正整数，中间用空格分隔，每个正整数都小于1000。
# 输出格式
# 一行，两个浮点数，依次为为求出来的平均值和方差值，保留两位小数，中间以空格分隔。

# 输入样例
# 10
# 6 1 4 2 5 1 7 10 4 1 
# 输出样例
# 4.10 8.09

n=int(input())
m=list(map(int,input().split()))
total=0
for i in range(n):
    total+=m[i]
# total=sum(m)
rev=total/n
total=0
for i in range(n):
    total+=(m[i]-rev)**2
cha=total/n
# cha=(sum((x-rev)**2 for x in m))/n
print(f'{rev:.2f} {cha:.2f}')

```

8 确定进制?


```python
# 6 × 9 = 42对于10进制来说是错误的，但是对于13进制来说是正确的。 即 6(13)​ × 9(13)​ = 42(13)​，而 42(13)​ = 54(10)。
# 现在编写一段程序，读入三个整数p、q和r，然后确定一个进制B（2<=B<=16）使得p × q = r。
# 如果B有很多选择，输出最小的一个。例如p = 186、q = 2、r = 3012，得到 16。

# 输入格式
# 一行，包含三个整数p、q和r。p、q、r的所有位都是数字，而且1<=p、q、r<=1000000
# 输出格式
# 一个整数 B （如果没有合适的B输出0，且2<=B<=16）

# 输入样例
# 12 4 48
# 输出样例
# 9

p,q,r=map(int,input().split())
def find_base(p,q,r):
    for i in range(2,17):
    # int() 函数不能直接从非字符串类型进行带基数的转换。
        try:
            p, q, r = str(p), str(q), str(r)  # 转换为字符串
            p, q, r = int(p, i), int(q, i), int(r, i) # 转换进制
            if p*q==r:
                return i
        except ValueError:
            # 如果转换失败（例如，进制不匹配），跳过该进制
                continue    
    return 0
print(find_base(p,q,r))            

```

9 摆凳子


```python
# 每次从凳子里找最矮的那个，把它跟第一个凳子交换位置，然后在剩下的凳子中找一个最矮的，把它跟剩下的凳子中的第一个交换位置，直到凳子有序为止。
# 例如有三个凳子，高度分别是5、2、9，交换完之后依次是2、5、9。


# 输入
# 第一行输入一个整型变量 n 表示接下来有 n 个数待排序
# 第二行有 n 个数
# 输出
# 排序后的 n 个数

# 输入样例
# 7
# 2 1 4 3 5 7 6
# 输出样例
# 1 2 3 4 5 6 7

n=int(input())
a=list(map(int,input().split()))
a.sort()
print(*a)

```

10 可变精度的输出*


```python
# 给定一个浮点数，按照指定精度输出。
# 例如给定浮点数12.354，指定精度为2，则输出12.35；又比如浮点数52.3684，指定精度为3，则输出52.368；
# 又比如浮点数78.2357，指定精度为3，则输出78.236；再比如浮点数44.123，指定精度5，则输出44.12300。

# 输入
# 两个数，第一个是一个0~100之间的浮点数n，有若干位小数；第二个是一个整数m（1≤m≤6），表示要输出的精度（即小数位数）。#两个数据之间以空格分隔。

# 输出
# 一个浮点数，将n按照上面的规则输出，小数占m位。

# 输入样例
# 78.532  4
# 输出样例
# 78.5320

n,m=input().split()
n=float(n)
m=int(m)
print(f'{n:.{m}f}')### {m} 是一个动态的格式说明符，表示小数点后的位数由变量 m 决定.
```

11 爬树的甲壳虫？


```python
# 甲壳虫想要爬上一颗高度为 n 的树，它一开始位于树根，高度为 0，当它尝试从高度 i − 1 爬到高度为 i 的位置时有 Pi​ 的概率会掉回树根，求它从树根爬到树顶时，经过的时间的期望值是多少。

# 输入
# 输入第一行包含一个整数 n 表示树的高度。
# 接下来 n 行每行包含两个整数 xi , yi，用一个空格分隔，表示Pi = xi/yi
# n ≤ 500，1 ≤ xi < yi ≤ 200。

# 输出格式
# 输出一行包含一个整数表示答案，答案是一个有理数，请输出答案对质数 998244353 取模的结果。
# 其中有理数 \frac{a}{b}对质数 P 取模的结果是整数 c 满足 0 ≤ c < P 且 c · b ≡ a (mod P)。

# 输入样例
# 1
# 1 2
# 输出样例
# 2

def mod_inverse(a, p):
    return pow(a, p-2, p)

def solve():
    n = int(input())
    p = [0] * n
    for i in range(n):
        xi, yi = map(int, input().split())
        p[i] = xi * mod_inverse(yi, 998244353) % 998244353

    E = [0] * (n+1)
    E[n] = 0
    for i in range(n-1, -1, -1):
        E[i] = (1 + E[i+1] + p[i] * (E[0] - E[i+1])) % 998244353

    return E[0]

print(solve())

```

12 第n小的质数


```python
# 输入一个正整数n，求第n小的质数。2是第1个质数，3是第2个质数，依次类推

# 输入
# 一个不超过10000的正整数n。
# 输出
# 第n小的质数。

# 输入样例
# 10
# 输出样例
# 29

n=int(input())
count=0
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
while count<n:
    for i in range(1000000000):
        if is_prime(i):
            count+=1
        if count==n:
            break
print(i)
```
