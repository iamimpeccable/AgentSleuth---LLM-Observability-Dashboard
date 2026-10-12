
from transformers import pipeline
from telemetry import run_with_telemetry
from database import save_record

questions = [
    "What is an LLM?",
    "Explain retrieval augmented generation (RAG) simply.",
    "What is the difference between AI and machine learning?",
    "Why is monitoring latency important in an LLM application?",
    "Explain Python dictionaries with a simple example."
]

records = []

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct"
)

for prompt in questions:
    record = run_with_telemetry(generator, prompt)
    records.append(record)
    record["model_name"] = "Qwen/Qwen2.5-1.5B-Instruct"
    record.setdefault("error_message", None)

    try:
        save_record(record)
        print("Saved to PostgreSQL!")
    except Exception as error:
        print(f"Database save failed: {error}")

    print(f"\nRequest: {record['request_id']}")
    print(f"Prompt: {record['prompt']}")
    print(f"Latency: {record['latency_seconds']} seconds")
    print(f"Input tokens: {record['input_tokens']}")
    print(f"Output tokens: {record['output_tokens']}")
    print(f"Status: {record['status']}")

    if record["status"] == "error":
        print(f"Error: {record['error_message']}")

print(f"\nTotal records collected: {len(records)}")
