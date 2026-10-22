
from transformers import pipeline
from telemetry import run_with_telemetry
from database import save_record
from prompts import all_prompts

records = []

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct"
)

for item in all_prompts:
    prompt = item["prompt"]
    record = run_with_telemetry(generator, prompt)
    record["prompt_id"] = item["prompt_id"]
    record["category"] = item["category"]
    record["model_name"] = "Qwen/Qwen2.5-1.5B-Instruct"
    record.setdefault("error_message", None)
    records.append(record)

    try:
        save_record(record)
        print(
           f"Saved {record['prompt_id']} "
           f"({record['category']}) to PostgreSQL"
        )
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
