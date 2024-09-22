''' Download from hf-mirror.com'''
from datasets import load_dataset
from evaluate import load
from transformers import AutoModelForQuestionAnswering

from huggingface_hub.utils import logging

# implement your logging function here
# NB: you need to set DEBUG mode with logging module

# you only need to download the dataset


'''
model = AutoModelForQuestionAnswering.from_pretrained(
    "distilbert/distilbert-base-uncased", trust_remote_code=True
)

# evaluation metric cannot be downloaded from hf-mirror
mse = load("evaluate-metric/mse")
'''
