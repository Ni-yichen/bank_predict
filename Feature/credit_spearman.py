import pandas as pd
from scipy import stats


if __name__ == '__main__':
    # 读取数据
    data = pd.read_csv('credit_to_train.csv')

    # 计算相关系数并进行相关性检验
    for col in data.columns:
        if col != 'credit_level':  # 排除credit_level本身

            unique_data = data[[col, 'credit_level']]

            # 单独处理特殊情况
            if len(unique_data[col].unique()) <= 1:
                print(f"{col}: 相关系数：NaN, p-value：NaN")
            else:
                coef, p_value = stats.spearmanr(unique_data[col], unique_data['credit_level'])
                print(f"{col}: 相关系数：{coef}, p-value： {p_value}")
