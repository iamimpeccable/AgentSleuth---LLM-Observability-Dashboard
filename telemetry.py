
import time
import uuid


def run_with_telemetry(generator, prompt):
    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    try:
        result = generator(
            prompt,
            max_new_tokens=100
        )

        latency_seconds = time.perf_counter() - start_time
        response = result[0]["generated_text"]

        # Count tokens using the model's tokenizer.
        input_tokens = len(
            generator.tokenizer.encode(prompt)
        )

        full_tokens = len(
            generator.tokenizer.encode(response)
        )

        output_tokens = max(0, full_tokens - input_tokens)

        record = {
            "request_id": request_id,
            "prompt": prompt,
            "response": response,
            "latency_seconds": round(latency_seconds, 2),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "status": "success"
        }

    except Exception as error:
        latency_seconds = time.perf_counter() - start_time

        record = {
            "request_id": request_id,
            "prompt": prompt,
            "response": None,
            "latency_seconds": round(latency_seconds, 2),
            "input_tokens": None,
            "output_tokens": None,
            "status": "error",
            "error_message": str(error)
        }

    return record
