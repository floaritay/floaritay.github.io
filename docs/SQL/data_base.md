# 语法描述

[]表示可选参数  
()表示必选分组或参数列表  
<>表示占位符,需替换为实际值  
|表示“或”，即多个选项中选其一  
...表示前面的元素可重复多次  
*通配符  

# 数据库的建立，删除

## 建立与查看数据库
CREATE DATABASE database_name;


```python
create database library;
show databases;
-- 查看MySQL中已存在的所有数据库
```

## 选择数据库，创建数据表，显示数据表结构
选择数据库  
use 数据库名  

创建数据表  
CREATE TABLE [IF NOT EXISTS] 表名 (  
    列名1 数据类型 [约束条件],  
    列名2 数据类型 [约束条件],  
    ...  
    [表级约束条件]  
) [表选项];  

显示数据表结构  
describe 数据表名；  

| 类别       | 类型             | 字节/说明                           |
|------------|------------------|-------------------------------------|
| **数值类型** | TINYINT          | 1                                  |
|            | SMALLINT         | 2                                   |
|            | INT              | 4                                   |
|            | BIGINT           | 8                                   |
|            | FLOAT            | 4                                   |
|            | DOUBLE           | 8                                   |
|            | DECIMAL(M,D)     | 变长                                | 
| **字符串类型** | CHAR(n)       | 字符                                 | 
|            | VARCHAR(n)       | 可变长度文本                          | 
|            | TEXT             | 长文本                                 | 
|            | TINYTEXT         | 短文本                                 | 
|            | LONGTEXT         | 超长文本                               | 
|            | BLOB             | 二进制大对象（如图片、文件）                                  
| **日期时间类型** | DATE             | YYYY-MM-DD                      |
|            | TIME             | HH:MM:SS                            |
|            | DATETIME         | YYYY-MM-DD HH:MM:SS                 |
| **其他类型** | ENUM('值1','值2')  | 枚举类型（限制字段取值范围）        |        
|            | SET('值1','值2') | 集合类型（支持多选）                   |     

ZEROFILL 表示前导零填充数值类型值以达到列的显示宽度  
auto_increment表示对于数值型字段自动增加  
not null表示不允许该字段值为null  
Primary Key constraint(主键约束)要求主键列的数据唯一，并且不允许为空             


```python
use library
-- 读者数据库
create table dz( 
    dzzh  int(3) zerofill auto_increment primary key,
    -- 读者证号
    xm varchar(8) not null,
    -- 姓名
    xb enum('男','女') default '男',
    -- 性别
    sf enum('研究生','工作人员','教研人员') default '研究生'
    -- 身份
);
describe dz;

```

## 修改数据表名称
ALTER TABLE   <旧表名> RENAME [TO]  <新表名> ;


```python
use library;   
alter table dz rename to reader;  
describe reader;  
```

## 数据表中添加字段
ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] [FIRST | AFTER 已存在字段名]


```python
use library;
alter table reader add dhhm varchar(11);
-- 电话号码
describe reader;
```

## 修改数据表的字段名称
ALTER TABLE <表名> CHANGE <旧字段名> <新字段名> <数据类型>；


```python
use library;
alter table reader change dhhm mobile varchar(11);
describe reader;
```

## 修改数据表的字段类型
ALTER TABLE <表名> MODIFY <字段名>  <数据类型>；


```python
use library;
alter table reader modify dhhm varchar(12);
describe reader;
```

## 删除与查看数据表
drop table 数据表名;  
SHOW TABLES;


```python
use library;
drop table reader;
show tables;
```

## 删除数据库
drop database 数据库名；  


```python
drop database library;
show databases;
```

# 数据表

## 修改数据表
ALTER TABLE <表名>   
[ADD <新列名><数据类型>[约束]]  
[ADD <表级约束>]  
[DROP <列名>[CASCADE|RESTRICT]]  
[DROP CONSTRAINT <表级约束>[CASCADE|RESTRICT]]  
[RENAME COLUMN <列名> TO <新列名>]  
[ALTER COLUMN <列名> TYPE <数据类型>]  

## 插入数据
INSERT  INTO  <表名>  (<字段1>[,<字段2>…])VALUES (<表达式1>[,<表达式2>…])


```python
use library;
insert into reader (xm,dhhm) values('林团团',13507311234);
select * from reader;
```

## 修改数据
UPDATE <表名>  SET<字段1>=<表达式1>  [,<字段2>=<表达式1>……]  [WHERE <条件>]


```python
use library;
update reader set dhhm=17718991989 where xm='林团团';
select * from reader;
```


```python
use library;
update reader set dhhm=13315667745,sf='工作人员' where xm='陈洁';
select * from reader;
```


```python
use library;
update reader set dzzh=dzzh+10;
-- 将每位读者reader的读者证dzzh号加十
select * from reader;
```

## 删除数据
delete from <表名> [where <条件>];


```python
use library;
delete from reader where xm='陈洁';
-- 删除读者reader数据表中的陈洁xm
select * from reader;
```


```python
use library;
delete from reader where sf='研究生';
-- 删除读者reader中的所有研究生sf
select * from reader;
```


```python
use library;
truncate reader;
-- 删除所有读者reader
select * from reader;
```

# 数据查询

## 按条件查询所有字段
select * from 数据表 where 查询条件


```python
-- jdxx数据表字段为sf(省份)--cs(城市)--qxmc--name
use province;
select * from jdxx where qxmc='开福区';
-- 查询街道信息(jdxx)数据表的开福区(qxmc)的所有字段
select * from jdxx where qxmc='开福区'||qxmc='岳麓区';
-- 查询街道信息(jdxx)数据表的开福区和岳麓区(qxmc)的所有字段
select * from jdxx where cs='长沙市'&&name='西湖街道';
-- 查询街道信息(jdxx)数据表的长沙市(cs)的西湖街道（name)所有字段
```

## 查询唯一值
distinct  <字段名>去掉重复的查询结果


```python
use province
select distinct qxmc from jdxx where sf='湖南省';
-- 查询湖南省（sf)所有的区县名称(qxmc)，每个区县只出现一次
select distinct qxmc from jdxx where cs='长沙市';
-- 查询长沙市（cs)所有的区县名称(qxmc)，每个区县只出现一次
```

## 统计查询
统计查询函数  
  SUM  
  计算数值列的和  
  AVG   
  计算数值列的平均值  
  MAX  
  计算列（数值、日期、字符）的最大值  
  MIN  
  计算列（数值、日期、字符）的最小值  
  COUNT  
  计算查询结果的数目  


```python
use province;
-- 查询湖南省的街道个数
-- 查询长沙市的街道个数
-- 查询湖南省的区县个数
-- 查询长沙市的区县个数
select count(name) from jdxx where sf=' 湖南省';
select count(name) from jdxx where cs='长沙市';
select count(distinct qxmc) from jdxx where sf='湖南省';
select count(distinct qxmc) from jdxx where cs='长沙市';
-- name为最后一个字段,不会重复,所以qxmc要加distinct
```

## 分组查询
select 表达式列表 from 数据表 where 条件 group by 分组字段 having 分组条件  
表达式列表可以为分组字段，也可以是统计函数  
注意分组条件和条件的区别  


```python
use province;
-- 统计每个省的名称和街道数目
-- 显示街道数目大于200个的城市和街道数目
-- 显示长沙市每个区县的街道数目
select sf,count(*) from jdxx group by sf;

select cs,count(*) from jdxx group by cs having count(*)>200;

select qxmc,count(*) from jdxx where cs='长沙市' group by qxmc;
```

## 数据排序
Order by <字段名1> ASC|DESC,  
       <字段名2> >ASC|DESC……  
首先按照<字段名1>的顺序排列记录  
若多条记录的<字段名1>值相同，则按<字段名2>的顺序排列  
ASC升序 DESC降序 默认升序  

使用limit  位置偏移量 <行数> 指定查询结果的数量  
位置偏移量指示从第几行开始显示，0表示从第1行开始，若省略默认为0，<行数>指定返回的记录条数  


```python
use province;
-- jdtj数据表字段为sf--cs--qxmc--jdgs(街道个数)

-- 显示jdtj数据表中街道个数最多的10个的所有字段
-- 显示jdtj数据表中街道个数最少的10个的所有字段
-- 按街道个数从高到底，街道个数相同的按省份升序排序显示jdtj数据表中街道个数大于35的所有字段
select * from jdtj order by jdgs desc limit 10;
select * from jdtj order by jdgs asc limit 10;
select * from jdtj where jdgs>35 order by jdtj desc,sf asc; 
```

## 多表查询(连接查询)

from 数据表1 join 数据表2 on 连接条件  
数据表1和数据表2为需要连接的数据表  
on后面是连接的条件 通常是关键字段的值相同  

内连接是最常见的多表查询类型，它返回两个表中都有匹配的行。  
左连接返回左表（数据表1 ）的所有行，即使右表（数据表2）中没有匹配的行  
交叉连接返回两个表的笛卡尔积，即每个表的每一行与另一个表的每一行相组合  

三个表的查询  
From 数据表1 ,数据表2 ,数据表3   
where 连接条件1 and 连接条件2  


```python
use library;
-- 根据读者(reader)和借阅(borrow)数据表，查询王颖珊的借阅记录，包括条形码txm、借阅日期jyrq、还书日期hsrq
select txm,jyrq,hsrq from reader join borrow on borrow.dzzh=reader.dzzh where xm='王颖珊'; 
-- 根据图书(book)和借阅(borrow)数据表，查询李白全集被借阅的情况：包括读者证号dzzh、借阅日期jyrq、还书日期hsrq
select dzzh,jyrq,hsrq from book join borrow on borrow.txm=book.txm where sm='李白全集'; 
-- 根据读者(reader)、图书(book)和借阅(borrow)数据表查询没有被归还的借阅信息：包括读者证号dzzh、姓名xm、电话dhhm、条形码txm、书名sm、借阅日期jyrq
-- 提示：通过isnull(表达式)可以判断表达式是否NULL值
select reader.dzzh,xm,dhhm,book.txm,sm,jyrq from book join borrow on book.txm=borrow.txm join reader on borrow.dzzh=reader.dzzh where isnull(hsrq);
```


```python
use library
-- 统计每本书借阅的次数,显示书名和借阅次数（借阅次数命名为jycs),按借阅次数降序排列,借阅次数相同的按书名降序排列
-- （提示：borrow数据表的一条数据对应一次借阅
select sm,count(sm) as jycs from borrow left join book on book.txm=borrow.txm group by sm order by jycs desc,sm desc;
-- 统计借阅次数在2次以上的图书的借阅的次数,显示书名和借阅次数，按借阅次数降序排列,借阅次数相同的按书名降序排列
select sm,count(sm) as jycs from borrow left join book on book.txm=borrow.txm group by sm having(jycs>=2) order by jycs desc,sm desc; 
-- 统计每个出版社的图书的借阅次数,显示出版社的名称和借阅次数，按借阅次数降序排列,借阅次数相同的按出版社降序排列
select cbs,count(cbs) as jycs from borrow left join book on book.txm=borrow.txm group by cbs order by jycs desc,cbs desc;
-- 统计每位读者借阅的次数,显示姓名和借阅次数,按借阅次数降序排列，借阅次数相同的按姓名降序排列
select xm,count(xm) as jycs from borrow left join reader on reader.dzzh=borrow.dzzh group by xm order by jycs desc,xm desc;
-- 统计研究生读者借阅的次数,显示姓名和借阅次数，按借阅次数降序排列，借阅次数相同的按姓名降序排列
select xm,count(xm) as jycs from borrow left join reader on borrow.dzzh=reader.dzzh where sf='研究生' group by xm order by jycs desc,xm desc;
-- 注意：order by <表达式1>,<表达式2>
-- 表示首先按第一个表达式的值排序，第一个表达式的值相同的再按第二个表达式的值排序
```

## 子查询
在SELECT语句中，一个查询语句完全嵌套在另一个查询语句的WHERE或HAVING的条件短语中，称为子查询或嵌套查询。  
通常把条件短语中的查询成为子查询，父查询则使用子查询的查询结果作为查询条件。  


```python
use library;
-- 查询与李白全集同一个出版社的图书的书名（不包括李白全集）
select sm from book where cbs='上海古籍出版社' and sm<>'李白全集';
-- 查询高于图书的平均售价(sj)的图书的书名和售价
select sm,sj from book where sj>(select avg(sj) from book);
-- 查询售价最高的图书的条形码、书名和售价
select txm,sm,sj from book where sj=(select max(sj) from book);
-- 查询售价最低的图书的条形码、书名和售价
select txm,sm,sj from book where sj=(select min(sj) from book);
```


```python
use library;
-- 查询曾经借过图书的读者的读者证号和姓名
select dzzh,xm from reader where reader.dzzh in (select dzzh from borrow);
-- 查询曾经没有被借阅的图书的条形码和书名
select txm,sm from book where book.txm not in (select txm from borrow);
-- 查询与孙思旺借过相同图书的读者的读者证号和姓名，按读者证号升序排列
select dzzh,xm from reader where reader.dzzh in (select dzzh from borrow where txm in (select txm from borrow where borrow.dzzh=(select dzzh from reader where xm='孙思旺'))) and dzzh <>'006' order by dzzh;
-- 查询借阅过李白全集的读者所借过的其他图书的书名按书名升序排列
select sm from book where book.txm in (select txm from borrow where borrow.dzzh in(select dzzh from borrow where borrow.txm=(select txm from book where sm='李白全集'))) and sm<>'李白全集' order by sm;
```

# 运算符

## null
<表达式><=>null或者<表达式>is null 可以判断某个表达式是否为null。如果<表达式>为null，返回1，否则返回0.


```python
use library;
-- 查询借阅(borrow)数据表中没有归还的记录的所有字段的值。
-- 当还书日期(hsrq)为null值，表示图书尚未归还。
select * from borrow where hsrq is null;
```

## between and in
<表达式> between<值1> and <值2>
表示判断表达式的值是否大于等于值1并且小于等于值2
如果符合条件，返回1，否则返回0

<表达式> in <值1,值2,值3……>
表示判断表达式的值是否与值1、值2、值3等中的任意一个相同。
如果相同，返回1，否则返回0
<表达式> not in <值1,值2,值3……>


```python
use library
-- 查询高于图书的售价(sj)大于等于10并且小于等于20的的图书的条形码(txm)、书名(sm)和售价(sj)。
select txm,sm,sj from book where sj between 10 and 20;
-- 查询图书的出版社(cbs)不是上海古籍出版社且不是中华书局的图书的条形码(txm)、书名(sm)和出版社(cbs)
select txm,sm,cbs from book where cbs not in ('上海古籍出版社','中华书局');
```

## like
通配符匹配
<表达式> like 匹配字符串
如果匹配返回1，不匹配返回0
在like 的匹配字符串中，
“%” (百分号)  代表任意长度（长度可以为0）的字符串
“_ ”(下横线)  代表任意单个字符


```python
use library;
-- 查询图书的书名(sm)中包含诗的图书的条形码(txm)、书名(sm)
select txm,sm from book where sm like '%诗%';
-- 查询图书的书名(sm)中以诗开头的图书的条形码(txm)、书名(sm)
select txm,sm from book where sm like '诗%';
```

## and or
and
逻辑与
例如a AND b，如果a和b两个都非0，返回1，否则只要有一个为0，返回0

or
逻辑或
例如a OR b，如果a和b中两个都是0时，返回0，否则只要有一个非0，则返回1
注意：and的优先级大于OR,必要时可以通过括号改变计算顺序


```python
use library;
-- 查询读者(reader)数据表中所有男性(xb)身份（sf)是研究生的记录的所有字段的信息
select * from reader where xb='男' and sf='研究生';
-- 查询读者(reader)数据表中所有男性(xb)身份（sf)是研究生和工作人员的所有字段的信息
select * from reader where xb='男' and (sf='研究生' or sf='工作人员')
```

# 函数

## 数值函数
四舍五入的函数  
ROUND(X,D)  
返回X，其值保留到小数点后D位，而第D位的保留方式为四舍五入。  
若D的值为0,则对小数部分四舍五入。  
若将D设为负值，保留X值小数点左边的D位  

TRUNCATE(X,D)  
返回被舍去至小数点后D位的数字X。  
若D的值为0,则不带有小数部分。  
将D设为负数,则截X小数点左起第D位开始后面所有低位的值   

工作人员gzry数据表  
gyu(雇员号)-gyxm(雇员姓名)-csrq(出生日期)-xl(学历)-gz(工资)-bm(部门)-dh(电话)  


```python
use sale;
-- 显示雇员姓名gyxm和扣费kf（工资gz的0.5%），要求四舍五入到个位。
select gyxm,round(gz*0.05,0) as kf from gzry; 
-- 显示雇员姓名gyxm和扣费kf(工资的0.5%)，要求舍去小数部分（不是四舍五入）
select gyxm,truncate(gz*0.05,0) as kf from gzry;
```

## 字符串函数一
concat
concat(<字符串1>,<字符串2>,<字符串3>)
将各个字符串连接起来

rpad
rpad(<字符串>,<长度>,<填充字符>)
返回字符串，右面用填充字符填补，直到指定长度的字符串

left
LEFT(<字符串>,<长度>)
返回字符串的最左边的指定长度的字符

char_length
char_length(<字符串>)
返回字符串的长度，即字符个数


```python
use sale
-- 查询员工信息（命名为ygxx)，使用字符串函数连接部门（不足4位宽度的部分右边填充全角空格）、姓名（不足4位宽度的部分右边填充全角空格）、电话，按部门升序排列。
select concat(rpad(bm,4,' '),rpad(gyxm,4,' '),dh) as ygxx from gzry order by bm;
-- 查询gzry数据表中姓王且名字为双字的员工的姓名和电话
-- (即王某某)
select ygxm,dh from gzry where left(gyxm,1)='王' and char_length(gyxm)=3;
```

## 字符串函数二
  
insert(<字符串>,<位置>,<长度>,<插入的字符串>)   
返回一个字符串，将字符串中指定位置的指定长度的字符删除，插入指定的字符串。  

space(<整数>)  
返回指定整数的空格  

mid(<字符串>,<指定位置>,<指定长度>)  
返回字符串从指定位置开始的指定长度的字符串  

right(<字符串>,<指定长度>)  
返回字符串右边的指定长度的字符串  

replace(<字符串>,<源字符串>,<目标字符串>)   
返回一个字符串，将字符串中所有的源字符串用目标字符串代替。  

顾客数据表gk  
hyh()-name()-sex()-tel()-dept()  


```python
use sale;
-- 显示每位顾客的姓名，两个字的中间插入两个空格，三个字的直接显示,列名为xm
select insert (name,2,0,space(2*(3-char_length(name)))) as xm from gk;
-- 显示每位顾客的姓名和电话（dh)，电话按照999-9999-9999的格式显示
select name,concat(left(tel,3),'-',mid(tel,4,4),'-',right(tel,4)) as dh from gk;
-- 将顾客数据表中单位(dept)中的新一佳用佳惠替换
update gk set dept=replace(dept,'新一佳','佳惠');
select name,dept from gk;
```

## 日期函数
year(日期)
返回日期的年号

month(日期)
返回日期的月号

datediff(日期1,日期2)
返回两个日期相差的天数


```python
use sale;
-- 查询2015年各月份（列名yf)的实际付款的和(列名sjje)
select month(xsrq) as yf,sum(sjfk) as sjje from xsd where year(xsrq)=2015 group by month(xsrq);
use library;
-- 根据图书馆规定，借阅期限是30天，超过30天需要按书籍售价的1%每天收取罚款.
-- 查询dzzh和罚款（fk列）
select dzzh,sj*0.01*(datediff(hsrq,jyrq)-30) as fk from borrow,book where book.txm=borrow.txm and datediff(hsrq,jyrq)>30;
```

## 条件函数

if(关系表达式,值1,值2)  
当条件表达式为真，返回值1，否则返回值2  

case <表达式> when <条件1> then <值1>  
when <条件2> then <值2>  
……  
else <值n+1>  
end   
若表达式的值为条件1则返回值1，否则若表达式的值为条件2则返回值1……若都不相同则返回值n+1  


```python
use sale;
-- 显示员工的姓名和费用（fy列），其中工资（gz)在2000以下的交50元，否则交100元。
select gyxm,if(gz<2000,50,100) as fy from gzry;
-- 显示员工的姓名和津贴(jt)，其中部门(bm)是销售部津贴1000，办公室津贴800,采购部津贴500，仓库津贴300。
select gyxm,case bm when '销售部' then 1000 when '办公室' then 800 when '采购部' then 500 else 300 end as jt from gzry;
```

# 索引

## 建立数据表的同时并建立索引

CREATE  TABLE  table_name 
    ([col_name data_type]
    [PRIMARY|UNIQUE][|INDEX|KEY]     
    [index_name] (index_col_name [length])
    [ASC | DESC]) 
table_name数据表的名称
primary主索引
unique唯一索引
index_name索引名
index_col_name索引列的名称

显示索引

 SHOW 
{INDEX|INDEXES|KEYS}
{FROM|IN}   [db_name .]table_name 
[[FROM|IN] db_name ]
[\G ]


```python
-- 在sale数据库中，建立供应商数据表
-- gys，包括供应商号gysh 字符型4位、公司名称 可变长字符型20位、电话 可变长字符型11位、地址 可变长字符型20位
-- 联系人 可变长字符型4位、手机 字符型11位 字段，同时根据供应商号字段建立主索引
-- 按行的方式显示gyh数据表的索引
use sale;
create table gys (
    gysh char(4),
    gsmc varchar(20),
    dh varchar(11),
    dz varchar(20),
    lxr varchar(4),
    sj char(11),
    primary key (gysh)
    );
show index from gys;
```

## 在已有的数据表建立索引


```python
use sale
-- 在xsdmx数据表根据销售单编号xsdh和序号xh两个字段建立主索引xsdxh
alter table xsdmx add primary key(xsdh,xh);
-- 在xsdmx数据表根据商品编号sph字段建立普通索引sphsy
create index sphsy on xsdmx (sph);
-- 在商品sp数据表根据商品名spm字段建立唯一索引spmsy
create unique index spmsy on sp (spm);

show index in xsdmx\g;
show index in sp\g;
```

## 删除索引
DROP INDEX
 index_name
ON table_name


```python
-- 删除sp商品数据表的索引spmsy
use sale;
drop index spmsy on sp;
show index in sp\g;
```

# 数据完整性

## 通过主索引设置实体完整性
对于已经存在的数据表，通过alter table 命令建立主索引  
alter table <数据表名> add primary key 索引名(字段名)  


```python
-- 对于图书数据表book（已经建立并插入记录），根据条形码（txm)、建立一个主索引,保证数据表中每本书的条形码是唯一的，即实体完整性
use library;
alter table book add primary key txm(txm);
insert into book(txm,sm) values("P0000001","苏东坡全集");
```

## 通过check设置域完整性
对于已经存在的数据表  
alter table <数据表名> add constraint <约束名> check <约束条件>  
可以设置数据表的域完整性  


```python
-- 对于图书数据表book（已经建立并插入记录），对于价格字段sj设置约束sjgd,要求价格必须大于0且小于等于5000
use library;
alter table book add constraint sjgd check(sj between 0 and 5000);
insert into book(txm,sm,sj) values("P0000099","四库全书一",8000);
```

## 参照完整性
alter table <子表> add  
[CONSTRAINT <外键名>]  
FOREIGN KEY <字段名>    
REFERENCES <主表> <主键列>  
on delete restrict|cascade|set null  
on update delete restrict|cascade|set null  

在设置参照完整性后  
当主表中没有相关数据时，子表中无法插入对应的记录    
如果delete设置为cascade   
在删除主表数据的时候，子表的数据将同时被删除   
如果delete设置为restrit   
子表中存在数据时，主表的数据将无法删除  
如果delete设置为set null    
在删除主表数据的时候，子表的数据被设置为null值    
(该列可以设置为null值的情况下)    

如果update设置为cascade    
在修改主表的关键字段的值的时候，子表中相关数据的字段的值将同时被修改     
如果update被设置为restrit    
子表中存在数据时，主表的相关数据的关键字段的值将无法修改  
如果update设置为set null    
在修改主表的关键字段的值的时候，子表中相关数据的字段的值将被设置为null   
(该列可以设置为null值的情况下)   


```python
-- 在借阅表和读者表设置参照完整性
-- 当删除读者表的数据时，借阅表的相关记录一起删除
-- 当修改读者表的读者证号时，借阅表的相关记录的读者证号一起被修改
use library;

alter table borrow add constraint dzzh foreign key (dzzh) references reader(dzzh)
on delete cascade
on update cascade;

delete from reader where dzzh="001";
update reader set dzzh="111" where dzzh="002";
select * from borrow;
```


```python
-- 当借阅表有某个条形码的记录，就不能删除图书表中相关的图书，也不能修改图书表中相关图书的条形码。
use library

alter table borrow add foreign key(txm) references book(txm) 
on delete restrict
on update restrict;

delete from book where txm="P0000001";
```

## 建立数据表并设置参照完整性


```python
-- 建立期刊qk数据表和期刊借阅qkjy数据表
-- 期刊qk数据表有6个字段，如下所示
-- 期刊条码qktxm varchar 10
-- 期刊名称qkmc varchar 20
-- 刊号kh varchar 10
-- 卷号jh varchar 10
-- 出版单位cbdw varchar 20
-- 价格jg decimal4,1字段
-- 期刊借阅qkjy数据表有4个字段，如下所示
-- 读者证号dzzh tinyint 3 unsigned zerofill
-- 期刊条码qktm varchar 10
-- 借阅日期jyrq date
-- 还书日期 hsrq date
-- 在建立期刊借阅数据表时，与读者表建立关联。
-- 当修改读者表的读者证号，借阅期刊表的相关会删除。当删除读者表的读者证号，借阅期刊表的相关记录会删除。
-- 在建立期刊借阅数据表时，同时与期刊表建立关联。不允许修改和删除期刊数据表的相关数据。
-- 注意：期刊数据表需要根据期刊号建立主索引
use library;

create table qk (
    qktxm varchar(10) primary key,
    qkmc varchar(20),
    kh varchar(10),
    jh varchar(10),
    cbdw varchar(20),
    jg decimal(4,1)
) ;
create table qkjy (
    dzzh tinyint(3) unsigned zerofill,
    qktxm varchar(10),
    jyrq date,
    hsrq date,
    foreign key(dzzh) references reader(dzzh) 
    on delete cascade
    on update cascade,
    foreign key(qktxm) references qk(qktxm)
    on delete restrict
    on update restrict
);

show create table qkjy;

```

## 删除参照完整性
alter table <数据表名> drop foreign key <外键名>  


```python
-- 删除借阅数据表和图书数据表的外键，名字为borrow_ibfk_1
use library;

alter table borrow drop foreign key borrow_ibfk_1;
 
show create table borrow;
```

# 视图

## 建立基于单表的视图，在视图中插入、删除和修改记录


```python
use sale;
-- 建立视图ckyg,查询gzry数据表中部门bm为仓库的员工的所有字段的信息
create view ckyg as select * from gzry where bm='仓库';
-- 在视图ckyg中,插入gyh雇员号为019,姓名gyxm为李盛,部门bm为仓库的数据
insert into  ckyg (gyh,gyxm,bm) values (019,'李盛','仓库');
-- 在视图ckyg中,删除姓名为赵国庆的数据
delete from ckyg where gyxm='赵国庆';
-- 在视图ckyg中,将王文武的电话改为13319660678
update ckyg set dh='13319660678' where gyxm='王文武';
select * from gzry;
```

## 根据多个数据表建立视图


```python
-- 根据工作人员gzry、销售单xsd、顾客gk数据表建立视图
-- 打开sale数据库
-- 建立xsdxx视图，包含销售单号xsdh、雇员号gyh、雇员姓名gyxm、会员号hyh、会员姓名name、销售日期xsrq、实际付款sjfk字段。
use sale;

create view xsdxx as select xsd.xsdh,xsd.gyh,gzry.gyxm,xsd.hyh,gk.name,xsd.xsrq,xsd.sjfk from xsd left join gzry on gzry.gyh=xsd.gyh left join gk on xsd.hyh=gk.hyh; 

select * from xsdxx;
```

## 根据视图建立视图


```python
-- 根据xsdxx视图建立视图xsdhytj,显示会员号hyh，姓名name和实际付款sjfk的合计金额(命名为hjje)
-- 按合计金额的降序排列
use sale
create view xsdhytj as select hyh,name,sum(sjfk) as hjje from xsdxx group by hyh,name order by hjje desc;
-- 根据xsdxx视图建立视图xsdgytj,显示雇员号gyh，姓名xm和实际付款sjfk的合计金额(命名为hjje)
-- 按合计金额的降序排列
create view xsdgytj as select gyh,gyxm,sum(sjfk) as hjje from xsdxx group by gyh order by hjje desc;

select * from xsdhytj;
select * from xsdgytj;
```

## 更新视图


```python
use sale;
-- 在视图xsdxx中，将工作人员gyxm王强的销售日期xsrq2015-6-3的会员名name刘海东的订单的实际付款sjfk设置为800
update xsdxx set sjfk=800 where gyxm='王强' and xsrq='2015-6-3' and name='刘海东';

select * from xsdhytj;
select * from xsdgytj;
```
