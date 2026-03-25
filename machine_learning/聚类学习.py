import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.metrics import silhouette_score,adjusted_rand_score,homogeneity_score

# # 从sklearn中获取鸢尾花数据集
# iris=datasets.load_iris()
# X=iris.data[:,:2] # 取前两个维度（萼片长度、萼片宽度)

# 从sklearn中获取葡萄酒数据集
wine=datasets.load_wine()
X=wine.data[:,1:3] # 取第二，三个维度（酒精、苹果酸)

# 计算肘部法则确定最佳K值
# 在肘部法则中，随着K值的增加，畸变程度会逐渐减小
# 但当K值增大到一定程度后，畸变程度的下降幅度会显著减缓，形成一个“肘部”形状
# 最佳的K值通常选择在“肘部”位置，此时增加K值对降低畸变程度的效果不明显，但可以避免过度细分导致的过拟合问题
def find_best_k(X,max_k):
    distortions=[] # 用于存储每个K值对应的畸变程度
    for k in range(1,max_k+1):
        kmeans=KMeans(n_clusters=k,random_state=42) # 创建 KMeans 对象 n_clusters=k
        kmeans.fit(X)
        distortions.append(kmeans.inertia_) # inertia_表示每个簇的平方距离之和，即畸变程度
        # 畸变程度越低越好，因为它表示数据点与其簇中心更加接近，聚类效果更好
    #绘制肘部法则图像
    plt.plot(range(1,max_k+1),distortions,marker='o')
    plt.xlabel('Numberofclusters')
    plt.ylabel('Distortion')
    plt.title('ElbowMethod')
    plt.show()

# 计算评价指标
def evaluate_cluster(estimator,X):
    labels=estimator.labels_ # 从estimator中获取聚类标签labels
    silhouette_avg=silhouette_score(X,labels) # 轮廓系数
    rand_score=adjusted_rand_score(wine.target,labels) # 调整兰德指数
    homogeneity=homogeneity_score(wine.target,labels) # 同质性得分
    print("SilhouetteScore:",silhouette_avg)
    print("AdjustedRandScore:",rand_score)
    print("HomogeneityScore:",homogeneity)
# 绘制K均值结果
def plot_kmeans_result(estimator):
    label_pred=estimator.labels_ # 获取聚类标签
    centroids=estimator.cluster_centers_ # 获取聚类中心
    plt.figure()
    colors=['red','green','blue']
    markers=['o','*','+']
    for i  in range(len(colors)):
        x=X[label_pred==i]
        plt.scatter(x[:,0],x[:,1],c=colors[i],marker=markers[i],label='Cluster%d'%i) # plt.scatter 函数用于绘制散点图
        # x[:, 0] 和 x[:, 1] 分别表示数据点的两个特征(萼片长度和萼片宽度)
        # c=colors[i] 设置数据点的颜色。
        # marker=markers[i] 设置数据点的标记形状。
        # label='Cluster %d' % i 为每个聚类设置图例标签
    plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=100,linewidths=3,c='black',label='Centroids')
    # 绘制聚类中心，使用黑色 'x' 标记
    # s=100 设置标记的大小
    # linewidths=3 设置标记的线宽
    # c='black' 设置标记的颜色
    # label='Centroids' 为聚类中心设置图例标签
    plt.xlabel('Sepallength')
    plt.ylabel('Sepalwidth')
    plt.legend(loc='upper left')
    plt.title('K-MeansClusteringResult')
    plt.show()

# 寻找最佳K值
find_best_k(X,10)
# 聚类
best_k=3 # 根据肘部法则图像得到的最佳k值
kmeans=KMeans(n_clusters=best_k,random_state=42)
kmeans.fit(X)
# 评价聚类性能
evaluate_cluster(kmeans,X)
# 获取聚类标签和聚类中心
cluster_labels=kmeans.labels_
cluster_centers=kmeans.cluster_centers_
# 输出每个数据点的聚类标签
print("ClusterLabels:")
print(cluster_labels)
# 输出聚类中心
print("ClusterCenters:")
print(cluster_centers)
# 绘制聚类结果
plot_kmeans_result(kmeans)
