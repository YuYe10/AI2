''' start: copy from SiderAI'''
import os
import pandas as pd

# 修改本地工作路径
os.chdir('G:/AI/AI2/2-dataset/data')

# 读取数据集
data = pd.read_parquet("data/data.parquet")
''' This is a test output
    num_rows = len(data)
    is_null_value = data.isnull().values.any()
    num_categories = len(data["label"].unique())
'''
num_information_in_each_category = data["label"].value_counts()
''' This is a test output
    print('num_rows:', num_rows, 'is_null_value:', is_null_value, '\n')
    print('num_categories:', num_categories, \
        'num_information_in_each_category:', \
            num_information_in_each_category, '\n')
'''
# 按照类别进行排序
data_sorted = data.sort_values('label')

# 计算每个类别数据量
min_category_count = min(num_information_in_each_category)
data_grouped = data.groupby("label")
data_balanced = data_grouped.apply(lambda x: x.sample(min_category_count)).reset_index(drop=True)

# 按 90%-10% 比例拆分数据集
train_size = int(0.9 * min_category_count)
train_data = data_balanced.groupby("label").head(train_size)
test_data = data_balanced[~data_balanced.index.isin(train_data.index)]

# 保存训练集和测试集为 parquet 文件
os.makedirs("data", exist_ok=True)
train_data.to_parquet("data/train.parquet", index=False)
test_data.to_parquet("data/test.parquet", index=False)
''' end: copy from SiderAI'''
