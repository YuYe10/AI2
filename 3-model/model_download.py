import os
os.environ['HF_ENDPOINT'] = "https://hf-mirror.com"
# huggingface-cli download --resume-download gpt2 --local-dir gpt2  --local-dir-use-symlinks False
from huggingface_hub import snapshot_download

model_name = "gpt2"
# while True 是为了防止断联
while True:
    try:
        snapshot_download(
            repo_id=model_name, # 在local-dir指定的目录中所见及所得
            ignore_patterns=["*.bin"],  # 忽略下载哪些文件
            local_dir=model_name,   
            resume_download=True,
            local_dir_use_symlinks = False,
        )
        break
    except:
        pass
