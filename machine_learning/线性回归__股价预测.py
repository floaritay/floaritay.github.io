from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error,r2_score
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

#加载数据
file_path=r'machine_learing\\prices.csv'
df=pd.read_csv(file_path)
 
# 数据预处理
df=df.loc[df['symbol']=='WLTW']# 选取股票
df.fillna(value=0,inplace=True)# 填补缺失值  

# 标签和特征
X=df[['open','high','low','volume']]  # 放弃了时间列
y=df['close']

# #确保日期是datetime类型
# df['date']=pd.to_datetime(df['date'])
# df.set_index('date',inplace=True)
# #使用数据集的最后一列作为标签，前几列作为特征
# X=df.iloc[:,:-1] # 除最后一列外的所有列
# y=df.iloc[:,-1] # 最后一列
# #选择只包含数值类型的列作为特征
# X=df.select_dtypes(include=[np.number])

# 划分数据集和测试集
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
train_size=int(len(X)*0.8)
X_train,X_test=X[:train_size],X[train_size:]
y_train,y_test=y[:train_size],y[train_size:]

# 创建线性回归模型
lr=LinearRegression(n_jobs=-1)
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)

# 评价输出模型性能两个指标(均方误差和决定系数)
mse = mean_squared_error(y_test, y_pred)
print("均方误差(Mean Squared Error):", mse)
r_squared = lr.score(X_test, y_test)
print("决定系数 (R-squared):", r_squared)

# 绘制图像
plt.figure(figsize=(12,6))
plt.plot(y.index,y.values,label='ActualPrice')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('All Actual Prices')
plt.legend()
plt.show()
#绘制最后100个样本的真实值和预测值的比较图(样本数量可以更改)
plt.figure(figsize=(12,6))
plt.plot(y_test.index[-100:],y_test.values[-100:],label='ActualPrice')
plt.scatter(y_test.index[-100:],y_pred[-100:],color='r',label='PredictedPrice')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Last Actual and Predicted Prices')
plt.legend()
plt.show()

