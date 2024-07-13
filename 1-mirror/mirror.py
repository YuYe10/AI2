''' Download from hf-mirror.com'''
from datasets import load_dataset
from evaluate import load
from transformers import AutoModelForQuestionAnswering

from huggingface_hub.utils import logging

logger = logging.get_logger("G:/AI/squad")
# implement your logging function here
# NB: you need to set DEBUG mode with logging module
logger.debug("This is a debug log")

# you only need to download the dataset
squad = load_dataset("G:/AI/squad", split="train[:5000]")
print(squad)

'''
model = AutoModelForQuestionAnswering.from_pretrained(
    "distilbert/distilbert-base-uncased", trust_remote_code=True
)

# evaluation metric cannot be downloaded from hf-mirror
mse = load("evaluate-metric/mse")
'''
