'''Load dataset script'''
import datasets
import pyarrow.parquet as pq
from datasets import DownloadManager, DatasetInfo

class DefaultDataset(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="default",
            version=datasets.Version("1.0.0"),
        ),
    ]

    def _info(self) -> DatasetInfo:
        """
            info方法, 定义数据集的信息,这里要对数据的字段进行定义
        :return:
        """
        return datasets.DatasetInfo(
            description="DefaultDataset",
            features=datasets.Features({
                    "text": datasets.Value("string"),
                    "label":datasets.Value("int8"),
                }),
            supervised_keys=None,  
        )

    def _split_generators(self, dl_manager: DownloadManager):
        """
            返回datasets.SplitGenerator
            涉及两个参数: name和gen_kwargs
            name: 指定数据集的划分
            gen_kwargs: 指定要读取的文件的路径, 与_generate_examples的入参数一致
        :param dl_manager:
        :return: [ datasets.SplitGenerator ]
        """
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, 
                    gen_kwargs={"filepath": "2-dataset/data/train.parquet",
                    },
                ),
            datasets.SplitGenerator(name=datasets.Split.TEST,
                    gen_kwargs={"filepath": "2-dataset/data/test.parquet",
                    },
                ),
            ]

    def _generate_examples(self, filepath):
        """
            生成具体的样本, 使用yield
            需要额外指定key, id从0开始自增就可以
        :param filepath:
        :return:
        """
        # Yields (key, example) tuples from the dataset
        # 读取 Parquet 文件  
        table = pq.read_table(filepath)  
        # 转换为 pandas DataFrame  
        df = table.to_pandas()  

        # 遍历 DataFrame 生成样本  
        for idx,row in df.iterrows():  
            yield idx, {
                    "text": row["text"],  # 使用 DataFrame 行中的文本  
                    "label": row["label"],  # 使用 DataFrame 行中的标签 
                }  
