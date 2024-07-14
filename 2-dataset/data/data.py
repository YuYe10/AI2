''' Loading Dataset'''
import os
from datasets import load_dataset, Features

# 修改本地工作路径
os.chdir('G:/AI/AI2/2-dataset/data')

# 定义特征
FEATURES = Features({
    "text": "string",
    "label": "int8"
})

# 读取第一节中分割的数据 train.parquet 和 test.parquet
dataset = load_dataset("parquet", data_files={'train': 'train.parquet', \
    'test': 'test.parquet'})

# 定义数据集配置
BUILDER_CONFIG = {
        "name": "default" ,
        "version": "1.0.0",
        "test": dataset['test'],
        "train": dataset['train'],
    
}

# 保存数据集
dataset.save_to_disk("~")
print(dataset)
