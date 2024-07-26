''' Loading Dataset'''
import os
from datasets import load_dataset, BuilderConfig

# 修改本地工作路径
os.chdir('G:/AI/AI2/2-dataset/data')

# 定义特征
FEATURES = {
     'text':'string',
    'label':'int8',
}

BUILDER_CONFIG = BuilderConfig(name='default', version='1.0.0',)

# 获取数据集
dataset = load_dataset('parquet', data_files={'train': 'train.parquet', 'test': 'test.parquet'})

print(dataset)
