from transformers import pipeline
from constants import MODEL_ID
from settings import settings

def main():
    print("Model ID:", MODEL_ID)
    # Pin the model revision to ensure reproducibility and prevent unexpected downloads once the model is in the HF cache
    print("Model revision: ", settings.model_revision)

    pipe = pipeline(
        "text-generation",
        model=MODEL_ID,
        revision=settings.model_revision,
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


if __name__ == "__main__":
    main()
