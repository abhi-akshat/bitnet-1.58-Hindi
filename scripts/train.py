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
import argparse
parser = argparse.ArgumentParser()
param = parser.add_argument("--param", type=str, required=True)
args = parser.parse_args().param

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "ai4bharat/Airavata"

config = config.getConfig(args)
MODEL_CONFIG = config['MODEL_CONFIG']
HEADS = config['HEADS']
DIMENSIONS = config['DIMENSIONS']
LAYERS = config['LAYERS']
INTERMEDIATE_SIZE= config['INTERMEDIATE_SIZE']
CONTEXT_LENGTH = config['CONTEXT_LENGTH']
NEW_MODEL = config['NEW_MODEL']

# print(f"Model config: {MODEL_CONFIG}")
# print(f"Model heads: {HEADS}")
# print(f"Model dimensions: {DIMENSIONS}")
# print(f"Model layers: {LAYERS}")
# print(f"Model intermediate size: {INTERMEDIATE_SIZE}")
# print(f"Model context length: {CONTEXT_LENGTH}")
# print(f"New model: {NEW_MODEL}")

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16).to(device)

