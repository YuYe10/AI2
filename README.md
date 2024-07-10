<center><h1>AI 考核二<br/>任务 0</h1></center>

## 1 考核二须知

### 1.1 考核形式

本次考核以 **里程碑形式** 进行，共有 3 个必做任务和 1 个可选任务，分别为 `Assignment 0[0-2]` 和 `Optional00`。

> 里程碑形式：即未完成上一个任务无法获取下一个任务，当你提交完成 _Assignment00_ 并通过检查你将会收到下一个任务，即 _Assignment01_。

### 1.2 诚信声明

_注：做此该声明是希望能通过第三方约束辅助你进行学习。_

在每个任务中你可以使用任何工具辅助你完成该任务，但你 **不被允许直接复制与抄写**，若你借用了如 GPT、CSDN、GitHub 等提供的方案代码或解决办法，请你需要 **在该代码段起始与结束标记来源**，以下是一个例子：

```python
def foo():
  # start: copy from [GPT|url]
  pass # code brick
	# end: copy from [GPT|url]
```

每次提交任务都会有相应的检查，一经发现则 ==**立即失去考核资格**==。

### 1.3 代码样式

1. 请尽量避免使中文，包括但不限于**文件名和注释**，文档 和 PPT 除外。

2. 使用 PyLint 插件并在 [该链接](https://google.github.io/styleguide/pyguide.html) 中下载其配置文件以帮助你格式化代码，你也可以利用这个链接来学习基本的代码规范。

3. 使用 MyPy 插件让你的 Python 用有良好的 [类型提示](https://docs.python.org/zh-cn/3.10/library/typing.html)。

### 1.4 环境工具

1. 请避免使用 Anaconda 和 Miniconda，该工具会污染 bash 等终端环境（因为其会自启动并更改系统环境）。
2. 你可以选用 [pyenv](https://github.com/pyenv/pyenv/tree/master) 及其插件 [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) 来管理所有的 Python 版本和创建的虚拟环境。

3. 你也可以选用系统的包管理软件管理 Python 的版本和使用 Python 原生提供的 venv 模块在每个工作目录下创建虚拟环境。

## 2 任务 0

随着 [Hugging Face](https://huggingface.co/)（以下简称 HF）的发展，LLM 相关的资源都在逐渐汇聚在该社区之中，同时在 ASC24 中也出现了大量依赖 HF 的任务，所以在 **任务 0** 当中你需要围绕 HF 提供的相当多便捷的方式来搭建一个简单的 LM 模型，具体任务如下：

1. 避免使用 VPN，完成对 HF 镜像站的资源获取。
2. 使用我们为你提供的数据集，完成相应的 :hugs: datasets 搭建并通过测试。
3. 利用你在 2 中的 :hugs: datasets 读取数据并使用 :hugs: transformers 搭建 LM 并进行训练达到预期的指标。
4. 整理你的工作并发送至相应的邮箱。

以上是任务的概述，具体的任务书将在对应任务的文件夹中。

本次任务的环境如下：

- Python 3.10
- 基础软件包可以利用 `pip install -r requirements.txt` 安装
- PyTorch 请根据你的环境自行安装

## 3 整理文件
你必须以 **正确** 的格式提交内容，否则视为 **无效提交**，格式如下：

```text
.
├── 1-mirror
│   └── mirror.py
├── 2-dataset
│   └── data.py
└── 3-model
    └── *.py # 所需的 Python 文件
```

请以压缩包的形式发送给指定的地址（请关注具体的消息）并以你的 ```年纪 _姓名``` 命名，如 `23级_张三`。