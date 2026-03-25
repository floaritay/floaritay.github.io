# 案例实践：电影评分数据分析与处理
# 开发一个电影推荐系统，系统需要分析用户对不同电影的评分。用户可以对每部电影进行评分（1-10 分），并且可能会有缺失的评分。
# 任务要求
# 1.数据生成 
# 使用 NumPy 创建一个包含 50 个用户对 5 部电影的评分数据的二维数组。评分应遵循正态分布，均值在 5 分左右，标准差为 2 分。确保每个评分在 1 到 10 之间。
# 2. 评分分析
# 计算每部电影的平均评分，忽略未评分的电影（缺失值）。
# 计算每位用户的平均评分。
# 3. 电影评分排名
# 对每部电影的平均评分进行排序，输出从高到低的电影排名。
# 4. 缺失值处理
# 随机为某些评分设置缺失值（使用 NaN），并在计算时确保能够正确处理这些缺失值。
# 5. 结果输出
# 输出生成的评分数据、每部电影的平均评分、每位用户的平均评分，以及电影的排名。

import numpy as np
import random

def movie_rating_analysis():
    # 设置随机种子以确保结果可重现
    np.random.seed(888)
    random.seed(777)
    
    # 数据生成
    num_users = 50
    num_movies = 5
    
    # 生成符合正态分布的评分数据
    ratings = np.random.normal(loc=5.0, scale=2.0, size=(num_users, num_movies))
    
    # 将评分限制在1到10之间
    ratings = np.clip(ratings, 1, 10)
    
    # 为某些评分设置缺失值(NaN)，约20%的数据设为缺失
    num_missing = int(num_users * num_movies * 0.2)
    for _ in range(num_missing):
        user_idx = random.randint(0, num_users - 1)
        movie_idx = random.randint(0, num_movies - 1)
        ratings[user_idx][movie_idx] = np.nan
    
    # 电影名称
    movie_names = ["复仇者联盟", "阿凡达", "泰坦尼克号", "星球大战", "哈利波特"]
    
    # 评分分析
    # 计算每部电影的平均评分（忽略NaN值）
    movie_avg_ratings = []
    for i in range(num_movies):
        valid_ratings = ratings[:, i][~np.isnan(ratings[:, i])]
        if len(valid_ratings) > 0:
            avg_rating = np.mean(valid_ratings)
        else:
            avg_rating = 0.0  # 如果某部电影没有任何评分，则平均分为0
        movie_avg_ratings.append(avg_rating)
    
    # 计算每位用户的平均评分（忽略NaN值）
    user_avg_ratings = []
    for i in range(num_users):
        valid_ratings = ratings[i][~np.isnan(ratings[i])]
        if len(valid_ratings) > 0:
            avg_rating = np.mean(valid_ratings)
        else:
            avg_rating = 0.0  # 如果某用户没有任何评分，则平均分为0
        user_avg_ratings.append(avg_rating)
    
    # 电影评分排名
    # 创建电影名称和平均评分的配对列表
    movie_rating_pairs = list(zip(movie_names, movie_avg_ratings))
    
    # 按平均评分降序排列
    sorted_movie_ratings = sorted(movie_rating_pairs, key=lambda x: x[1], reverse=True)
    
    # 4. 结果输出
    print("\n1. 生成的评分数据（前10位用户）：")
    print("用户\\电影\t复仇者联盟\t阿凡达\t泰坦尼克号\t星球大战\t哈利波特")
    print("-" * 60)
    for i in range(min(10, num_users)):
        row_str = f"用户{i+1}\t\t"
        for j in range(num_movies):
            if np.isnan(ratings[i][j]):
                row_str += "N/A\t\t"
            else:
                row_str += f"{ratings[i][j]:.2f}\t\t"
        print(row_str)
    
    print(f"\n... 总共{num_users}位用户对{num_movies}部电影进行了评分")
    print(f"缺失评分数: {int(np.sum(np.isnan(ratings)))}, 占总数据比例: {np.sum(np.isnan(ratings))/(num_users*num_movies)*100:.2f}%")
    
    print("\n2. 每部电影的平均评分：")
    for i in range(num_movies):
        print(f"{movie_names[i]}: {movie_avg_ratings[i]:.2f}分")
    
    print("\n3. 每位用户的平均评分（前10位）：")
    for i in range(min(10, num_users)):
        print(f"用户{i+1}: {user_avg_ratings[i]:.2f}分")
    
    print(f"\n... 总共{num_users}位用户的平均评分")
    
    print("\n4. 电影评分排名（从高到低）：")
    for rank, (name, avg_rating) in enumerate(sorted_movie_ratings, start=1):
        print(f"第{rank}名: {name} ({avg_rating:.2f}分)")
    
    # 额外统计信息
    print("\n5. 统计摘要：")
    print(f"总体平均评分: {np.nanmean(ratings):.2f}")
    print(f"最高评分: {np.nanmax(ratings):.2f}")
    print(f"最低评分: {np.nanmin(ratings):.2f}")
    print(f"评分标准差: {np.nanstd(ratings):.2f}")
    
    return ratings, movie_avg_ratings, user_avg_ratings, sorted_movie_ratings

# 执行函数
if __name__ == "__main__":
    result = movie_rating_analysis()



