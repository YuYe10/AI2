''' Loading Dataset'''
import os
from datasets import load_dataset, Features, BuilderConfig

# 修改本地工作路径
os.chdir('G:/AI/AI2/2-dataset/data')

# 定义特征
FEATURES = Features({
     'text':'string',
    'label':'int8',
})

BUILDER_CONFIG = BuilderConfig({ 
    'name': 'default', 
    'version': '1.0.0', 
    'train': 'train.parquet',
    'test': 'test.parquet'
})

# 获取数据集
dataset_dict = load_dataset('parquet', features=FEATURES, name='deafult',  data_files={'train': \
'train.parquet', 'test': 'test.parquet'}, version='1.0.0', data_dir='G:/AI/AI2/2-dataset/data')

print(dataset_dict)
