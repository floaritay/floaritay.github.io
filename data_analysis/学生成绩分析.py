# 一份学生成绩数据集，包含学生的姓名、年级、成绩和出勤率。
# 任务要求
# 1.查看数据集的基本信息（如列名、数据类型、缺失值情况等）。
# 2. 计算成绩的基本统计信息：平均成绩、最高成绩、最低成绩。
# 3. 找出成绩高于 85 分的学生，并打印他们的详细信息。
# 4. 按照出勤率从低到高对学生进行排序，查看出勤率最低的学生。
# 5. 增加一列，表示学生是否通过考试（及格分数为 60 分）。
# 6. 增加一列，用来给学生成绩进行等级划分（A: ≧90 分，B: 80-89 分，C: 70-79 分，D: 60-69 分）。
# 7. 按年级对学生成绩进行分组，计算每个年级的平均成绩。

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 中文字体设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 生成学生成绩数据集
np.random.seed(42)  # 设置随机种子，确保结果可重现

# 创建学生数据
students_data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九', '吴十', '郑十一', '王十二',
             '冯十三', '陈十四', '褚十五', '卫十六', '蒋十七', '沈十八', '韩十九', '杨二十'],
    '年级': np.random.choice(['一年级', '二年级', '三年级'], size=18),
    '成绩': np.random.randint(50, 100, size=18),  # 成绩范围50-99
    '出勤率': np.round(np.random.uniform(0.6, 1.0, size=18), 2)  # 出勤率范围0.6-1.0
}

df = pd.DataFrame(students_data)
print("原始学生成绩数据集:")
print(df)
print("\n" + "="*50)

# 2. 查看数据集的基本信息
print("1. 数据集基本信息:")
print(f"数据形状: {df.shape}")
print(f"列名: {list(df.columns)}")
print("\n数据类型:")
print(df.dtypes)
print("\n缺失值情况:")
print(df.isnull().sum())
print("\n数据集前5行:")
print(df.head())
print("\n" + "="*50)

# 3. 计算成绩的基本统计信息
print("2. 成绩基本统计信息:")
print(f"平均成绩: {df['成绩'].mean():.2f}")
print(f"最高成绩: {df['成绩'].max()}")
print(f"最低成绩: {df['成绩'].min()}")
print(f"成绩标准差: {df['成绩'].std():.2f}")
print("\n成绩描述性统计:")
print(df['成绩'].describe())
print("\n" + "="*50)

# 4. 找出成绩高于85分的学生
high_scorers = df[df['成绩'] > 85]
print("3. 成绩高于85分的学生:")
if not high_scorers.empty:
    print(high_scorers)
else:
    print("没有找到成绩高于85分的学生")
print("\n" + "="*50)

# 5. 按出勤率从低到高排序，查看出勤率最低的学生
df_sorted_by_attendance = df.sort_values('出勤率')
print("4. 按出勤率从低到高排序:")
print(df_sorted_by_attendance[['姓名', '年级', '成绩', '出勤率']])
print(f"\n出勤率最低的学生: {df_sorted_by_attendance.iloc[0]['姓名']}, "
      f"出勤率: {df_sorted_by_attendance.iloc[0]['出勤率']}")
print("\n" + "="*50)

# 6. 增加一列，表示学生是否通过考试（及格分数为60分）
df['是否及格'] = df['成绩'] >= 60
print("5. 添加是否及格列后的数据:")
print(df[['姓名', '年级', '成绩', '出勤率', '是否及格']])
print("\n及格人数:", df['是否及格'].sum())
print("不及格人数:", len(df) - df['是否及格'].sum())
print("\n" + "="*50)

# 7. 增加一列，用来给学生成绩进行等级划分
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

df['等级'] = df['成绩'].apply(assign_grade)
print("6. 添加成绩等级列后的数据:")
print(df[['姓名', '年级', '成绩', '出勤率', '是否及格', '等级']])
print("\n各等级人数统计:")
print(df['等级'].value_counts().sort_index())
print("\n" + "="*50)

# 8. 按年级对学生成绩进行分组，计算每个年级的平均成绩
grade_avg_scores = df.groupby('年级')['成绩'].mean()
print("7. 按年级分组的平均成绩:")
for grade, avg_score in grade_avg_scores.items():
    print(f"{grade}: {avg_score:.2f}分")

print("\n按年级分组的详细统计:")
grade_stats = df.groupby('年级').agg({
    '成绩': ['count', 'mean', 'max', 'min'],
    '出勤率': 'mean'
}).round(2)
print(grade_stats)
print("\n" + "="*50)

# 额外分析：不同等级的学生分布可视化
print("8. 学生成绩等级分布:")
import matplotlib.pyplot as plt


# 绘制成绩等级分布饼图
plt.figure(figsize=(12, 4))
    
# 子图1：成绩等级分布
plt.subplot(1, 2, 1)
grade_counts = df['等级'].value_counts().reindex(['A', 'B', 'C', 'D', 'F'], fill_value=0)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
plt.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('学生成绩等级分布')
    
# 子图2：各年级平均成绩
plt.subplot(1, 2, 2)
grades = list(grade_avg_scores.index)
avg_scores = list(grade_avg_scores.values)
plt.bar(grades, avg_scores, color='skyblue')
plt.title('各年级平均成绩')
plt.ylabel('平均成绩')
plt.xticks(rotation=45)
    
plt.tight_layout()
plt.show()


# 最终数据集概览
print("\n最终数据集概览:")
print(df)



