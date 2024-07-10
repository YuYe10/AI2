# 从镜像源下载

## 目标

1. 实现 HF 程序包的日志输出；
2. 手动从镜像源下载依赖并使用在 `from_pretrained` 和 `load*` 中。

## 动机

1. 此任务是为了避免在赛场上无法使用 VPN 的情况；
2. 通过输出日志，更好的定位 HF 程序包的运行情况。

## 帮助链接

1. HF 镜像站：https://hf-mirror.com
2. HF 镜像站下载教程：https://zhuanlan.zhihu.com/p/663712983
3. 申请 Access Token：https://huggingface.co/settings/tokens
4. HF 文档: https://huggingface.co/docs

**推荐使用 [hfd](https://gist.github.com/padeoe/697678ab8e528b85a2a7bddafea1fa4f) 进行手动下载，好处是有多线程支持且稳定。**

## 测试

### 实现 HF 程序包的日志输出

在实现完成日志输出后，运行以下命令：

```bash
python mirror.py
```

你需要查看是否有如下输出，红框位置分别表示使用的 **下载源** 和是否使用了 `Token`

![remote 日志输出](../asset/1-mirror/remote-logging-info.png)

### 手动从镜像源下载依赖并使用在 `from_pretrained` 和 `load*` 中

**注：优先设置环境变量 `HF_ENDPOINT` 且须关闭 VPN**

你只需要完成下载 `mirror.py` 中所使用的数据集 `squad`

当你下载完成之后再次运行命令：

```bash
python mirror.py
```

你只会看到如下输出：

```text
Dataset({
    features: ['id', 'title', 'context', 'question', 'answers'],
    num_rows: 5000
})
```
