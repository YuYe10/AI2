from datasets import load_dataset
from evaluate import load
from transformers import AutoModelForQuestionAnswering

from huggingface_hub.utils import logging

logging.set_verbosity(logging.DEBUG)
logger = logging.get_logger("datasets")
# implement your logging function here
# NB: you need to set DEBUG mode with logging module

logger.debug("GET")
# you only need to download the dataset
squad = load_dataset("G:/AI/AI2/squad", split="train[:5000]")
print(squad)

'''
model = AutoModelForQuestionAnswering.from_pretrained(
    "distilbert/distilbert-base-uncased"
)

# evaluation metric cannot be downloaded from hf-mirror
mse = load("evaluate-metric/mse")
'''
