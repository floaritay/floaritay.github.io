# 目录


---
F (汽车厂)  
F_ID (PK)  
F_Name  
F_Location  
  
M (汽车销售店)  
M_ID (PK)  
M_Name  
M_Location  
  
D (汽车)  
D_ID (PK)  
D_Name  
D_TireBrand  
D_IsNewEnergy  
  
FMD (供应记录)  
F_ID (FK)  
M_ID (FK)  
D_ID (FK)  
Supply_Date (PK的一部分，或与其他字段组合成PK)  
Supply_Quantity  


```python
SELECT M_Name
FROM FMD
JOIN F ON FMD.F_ID = F.F_ID
JOIN M ON FMD.M_ID = M.M_ID
WHERE F_Name = '武汉神龙' AND M_Location = '天津';
```


```python
SELECT M_Name, FMD.D_ID
FROM FMD
JOIN D ON FMD.D_ID = D.D_ID
JOIN M ON FMD.M_ID = M.M_ID
WHERE Supply_Date = '2014-03-15' AND D_TireBrand = '米其林';
```


```python
CREATE VIEW ShanghaiNewEnergySupply AS
SELECT 
    F_Name AS 厂名,
    M_Name AS 店名,
    D_Name AS 车名,
    Supply_Quantity AS 数量
FROM FMD
JOIN F ON FMD.F_ID = F.F_ID
JOIN M ON FMD.M_ID = M.M_ID
JOIN D ON FMD.D_ID = D.D_ID
WHERE F.F_Location = '上海' AND D.D_IsNewEnergy = TRUE;
```

1.数据库管理员：决定数据库中的信息内容和结构、决定数据库的存储结构和存取策略、定义数据的安全性要求和完整性约束条件、监控数据库的使用和运行  
2.系统分析员：负责应用系统的需求分析和规范说明、与用户及DBA协商，确定系统的硬软件配置、参与数据库系统的概要设计  
3.数据库设计人员：参加用户需求调查和系统分析、确定数据库中的数据、设计数据库各级模式  
4.应用程序员：设计和编写应用系统的程序模块、进行调试和安装  
5.最终用户：偶然用户、简单用户、复杂用户  

F (FNO,FNAME,CITY);                 FNO是主码  
M (MNO,MNAME,TYRE,ISNEWENERGY);     MNO是主码  
D (DNO,DNAME,CITY);                 DNO是主码  
FMD (FNO,MNO,MNO,DATE,QTY);         (FNO,MNO,MNO)组合是主码，FNO,MNO及MNO分别是外码  

（1）查询所有接受过“武汉神龙”汽车厂供货的天津的汽车销售店名称  
（2）查询在日期“2014-03-15”接受了采用“米其林”品牌轮胎的汽车供应的汽车销售店名称和汽车号  

根据设计的数据库，用SQL语句建立一个视图，该视图反映如下信息：  
所在地位于上海的汽车厂供应的所有新能源车信息，其中包括厂名、店名、车名以及相应的数量    


```python


SELECT DISTINCT D.DNAME
    FROM F, M, D, FMD
    WHERE  F.FNO = FMD.FNO 
       AND M.MNO = FMD.MNO 
       AND D.DNO = FMD.DNO
       AND D. CITY = '天津'
       AND F. FNAME = '武汉神龙'
       
SELECT D.DNAME, M.MNO
    FROM F, M, D, FMD
    WHERE  F.FNO = FMD.FNO 
        AND M.MNO = FMD.MNO 
        AND D.DNO = FMD.DNO
        AND M. TYRE = '米其林'
        AND FMD.DATE = '2013-03-15'

CREATE VIEW V1 AS
 SELECT F.FNAME,M.MNAME,D.DNAME,FMD.QTY
 FROM F,M,D,FMD
 WHERE  F.FNO = FMD.FNO 
      AND M.MNO = FMD.MNO 
      AND D.DNO = FMD.DNO
      AND M. ISNEWENERGY = TRUE
      AND F.CITY = '上海'
```
