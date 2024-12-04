import torch
from torch import nn
from transformers.models.llama.modeling_llama import *
from transformers import (AutoTokenizer, AutoModelForCausalLM, AutoConfig, LlamaForCausalLM, DataCollatorForLanguageModeling, Trainer, TrainingArguments)
from datasets import load_dataset
from huggingface_hub import login
import wandb
from huggingface_hub import create_repo, HfApi
import datasets

from settings import settings
from config import config

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "ai4bharat/Airavata"

config = config.config_100m

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16).to(device)

