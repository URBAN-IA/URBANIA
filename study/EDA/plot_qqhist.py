import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# 예제 데이터 생성
np.random.seed(0)
normal_data = np.random.normal(loc=0, scale=1, size=1000)  # 정규분포 데이터
non_normal_data = np.random.exponential(scale=1, size=1000)  # 비정규분포 데이터

# 데이터프레임 생성
data = pd.DataFrame({'Normal': normal_data, 'NonNormal': non_normal_data})

def plot_distribution(data):
    for column in data.columns:
        plt.figure(figsize=(12, 6))

        # 히스토그램
        plt.subplot(1, 2, 1)
        plt.hist(data[column], bins=30, edgecolor='k', alpha=0.7)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')

        # Q-Q 플롯
        plt.subplot(1, 2, 2)
        stats.probplot(data[column], dist="norm", plot=plt)
        plt.title(f'Q-Q Plot of {column}')

        plt.tight_layout()
        plt.show()

plot_distribution(data)
