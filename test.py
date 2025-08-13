from transformers import pipeline
import torch
from config import HF_MODEL_ID, HF_REVISION

print("Model ID:", HF_MODEL_ID)
print("Model revision: ", HF_REVISION)


pipe = pipeline(
    "text-generation",
    model=HF_MODEL_ID,
    revision=HF_REVISION,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Explain quantum mechanics clearly and concisely."},
]

outputs = pipe(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])
