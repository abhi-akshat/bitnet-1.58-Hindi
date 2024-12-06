from transformers import AutoTokenizer
from datasets import load_dataset
import huggingface_hub
from huggingface_hub import login

from scripts.config import model_name
from settings import settings

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
tokenizer.pad_token = tokenizer.eos_token

HF_TOKEN = settings.HF_TOKEN
login(token=HF_TOKEN)
ds = load_dataset("Hindi-data-hub/odaigen_hindi_pre_trained_sp")

CONTEXT_LENGTH = 256

def tokenize(element):
    outputs = tokenizer(
        element["content"],
        truncation=False,
        max_length=CONTEXT_LENGTH,
        return_overflowing_tokens=True,
        return_length=True,
    )
    # Combine all tokens
    combined = []
    for tokenized_doc in outputs['input_ids']:
        combined += tokenized_doc + [tokenizer.eos_token_id]
    # Chunk
    input_batch = []
    for i in range(0, len(combined) - CONTEXT_LENGTH, CONTEXT_LENGTH):
        input_batch.append(combined[i:i+CONTEXT_LENGTH])
    return {"input_ids": input_batch}

tokenized_data = ds.map(
    tokenize, batched=True, remove_columns=ds["train"].column_names,
)

tokenized_data.save_to_disk("tokenized_data")



