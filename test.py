import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot_income_curves(days=200000):
    # 设置中文字体
    font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

    # 模拟选择1和选择2的收益
    choice1 = np.full(days, 100)
    choice2 = np.random.choice([600, 50], size=days, p=[0.1, 0.9])

    # 计算累计收益
    cumulative_choice1 = np.cumsum(choice1)
    cumulative_choice2 = np.cumsum(choice2)

    # 创建绘图
    fig, axes = plt.subplots(5, 4, figsize=(20, 15))
    fig.suptitle('选择1和选择2的收益曲线', fontproperties=font, fontsize=20)

    # 绘制每个格子的收益曲线
    for i in range(5):
        for j in range(4):
            ax = axes[i, j]
            start = (i * 4 + j) * 10000
            end = start + 10000
            ax.plot(range(start, end), cumulative_choice1[start:end], label='选择1')
            ax.plot(range(start, end), cumulative_choice2[start:end], label='选择2')
            ax.set_title(f'第{start+1}天到第{end}天', fontproperties=font)
            ax.set_xlabel('天数', fontproperties=font)
            ax.set_ylabel('累计收益', fontproperties=font)
            if i == 0 and j == 0:
                ax.legend(prop=font)

    # 调整布局
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('income_curves.png')

if __name__ == "__main__":
    plot_income_curves()