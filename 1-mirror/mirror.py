''' Download from huggingface.co'''  
import os
os.environ['HF_ENDPOINT'] = 'https://huggingface.co'

from datasets import load_dataset  
from evaluate import load  
from transformers import AutoModelForQuestionAnswering  
from huggingface_hub.utils.logging import get_logger, set_verbosity_debug

# implement your logging function here

logger = get_logger(__name__)  
set_verbosity_debug()
logger.debug("Started Download")  
# NB: you need to set DEBUG mode with logging module 
dataset = load_dataset("squad")  
  
logger.debug(f"Datasets: {dataset}")  
  
print(dataset)
'''  
model = AutoModelForQuestionAnswering.from_pretrained(  
    "distilbert/distilbert-base-uncased", trust_remote_code=True  
)  

# evaluation metric cannot be downloaded from hf-mirror  
mse = load("evaluate-metric/mse")  
'''