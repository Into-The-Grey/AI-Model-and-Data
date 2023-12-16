import os
import sys
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import PreTrainedTokenizerFast
from transformers import PreTrainedTokenizer

def download_model(model_name: str, save_directory: str):
    # Download and cache the model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path=model_name)
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_name)

    # Save the model and tokenizer to the specified directory
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory=save_directory)

# Call the download_model function
download_model(
    model_name="EleutherAI/gpt-j-6B",
    save_directory="/mnt/AI Model \Data/Model Weights & Code",
)