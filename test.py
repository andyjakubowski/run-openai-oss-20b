from transformers import pipeline
from config import HF_MODEL_ID, HF_REVISION

print("Model ID:", HF_MODEL_ID)
# Pin the model revision to ensure reproducibility and prevent unexpected downloads once the model is in the HF cache
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
