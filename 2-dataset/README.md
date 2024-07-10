# :hugs: datasets 搭建

## 目标

1. 实现读取 parquet 数据集，并将其拆成 train 和 test 两类
2. 编写 `data/data.py` 文件并通过测试

## 动机

1. 此任务是为了熟悉如何编写读取数据的相关脚本

## 帮助链接

1. Datasets 文档：https://huggingface.co/docs/datasets/index
2. Pandas 文档：https://pandas.pydata.org/docs

## 测试

### 拆分数据集

`data/data.parquet` 的结构：

|text|label|
|:-:|:-:|
|待分类的文本|类别|

你可以利用 `.ipynb` 文件来帮助你的可视化的了解你的数据集，同时更好的拆分

在拆分之前你需要先回答几个问题：

1. 其有几行数据？
2. 其中有没有空值？
3. 有几种类别？
4. 每种类别都各有几条数据？

当你能够充分回答完成上述问题后，你需要按照 train-90%, test-10% 的比例进行拆分为两个文件：`data/train.parquet` 和 `data/test.parquet`，其中各类别数量必须均分，即类别0、1、2 ... 的数量均相等。

**注：你应该充分使用 `pandas` 来帮助你完成，而不是使用 `built-in` 工具**

当你拆分完成后执行如下命令：

```bash
python test_data.py
```

测试通过则会提示以下信息：

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.083s
```

### 读取数据集

该部分应该参考 HF 的 datasets 的官方文档完成读取脚本 `data/data.py` 的编写。（不测试具体的数据内容，所以你应该严格使用在第一节内容分割完成的数据）

必要的内容为：
- 至少拥有一个 `BUILDER_CONFIG` 且其名称为 `default` 版本为 `1.0.0`
- 在名称为`default` 的配置下拥有两个 `Dataset` 分别为 `train` 和 `test`
- `Features` 有两个分别为：`text` - `string` 和 `label` - `int8`

完成读取脚本的编写后执行以下命令：

```bash
python test_dataset.py
```

测试通过则会提示以下信息：

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.083s
```