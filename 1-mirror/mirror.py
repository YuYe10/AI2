# coding=utf-8  
# Copyright 2020 Optuna, Hugging Face  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
#     http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  

''' Download from hf-mirror.com'''  

from datasets import load_dataset  
from evaluate import load  
from transformers import AutoModelForQuestionAnswering  
from huggingface_hub.utils.logging import get_logger, set_verbosity_debug  

# implement your logging function here

logger = get_logger(__name__)  
set_verbosity_debug()
logger.debug("Starting to download the dataset...")  
# NB: you need to set DEBUG mode with logging module 
dataset = load_dataset("squad")  
  
logger.debug(f"Dataset loaded: {dataset}")  
  
print(dataset)
'''  
model = AutoModelForQuestionAnswering.from_pretrained(  
    "distilbert/distilbert-base-uncased", trust_remote_code=True  
)  

# evaluation metric cannot be downloaded from hf-mirror  
mse = load("evaluate-metric/mse")  
'''