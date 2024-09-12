''' Loading Dataset'''
from datasets import load_dataset, BuilderConfig


# 定义特征
FEATURES = {
     'text':'string',
    'label':'int8',
}

BUILDER_CONFIG = BuilderConfig(name='default', version='1.0.0',)

# 获取数据集
dataset = load_dataset('parquet', data_dir="2-dataset/data", data_files={'train': 'train.parquet', 'test': 'test.parquet'})

print(dataset)
