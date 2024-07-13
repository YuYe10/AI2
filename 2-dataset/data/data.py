''' Loading Dataset'''
import pandas as pd
from datasets import Dataset

# 读取第一节中分割的数据 train.parquet 和 test.parquet
train_data = pd.read_parquet("2-dataset/data/train.parquet")
test_data = pd.read_parquet("2-dataset/data/train.parquet") 

# 将 pandas DataFrame 转换为字典
train_dict = train_data.to_dict(orient='list')
test_dict = test_data.to_dict(orient='list')

# 定义特征
FEATURES = {
    "text": "string",
    "label": "int8"
}

# 创建数据集
train_dataset = Dataset.from_dict(train_dict, features=FEATURES)
test_dataset = Dataset.from_dict(test_dict, features=FEATURES)

# 定义数据集配置
BUILDER_CONFIG = {
    "name": "default",
    "version": "1.0.0",
}

# 创建包含train和test数据集的字典
dataset_dict = {
    'train': train_dataset,
    'test': test_dataset,
}

# 将数据集对象转换为包含builder配置的数据集对象
dataset = Dataset(dataset_dict, info=BUILDER_CONFIG)
