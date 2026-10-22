
import os
import uuid
import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def save_record(record):
    query = """
        INSERT INTO llm_requests (
            request_id,
            model_name,
            prompt_id,
            category,
            prompt,
            response,
            latency_seconds,
            input_tokens,
            output_tokens,
            status,
            error_message
        )
        VALUES (
            %(request_id)s,
            %(model_name)s,
            %(prompt_id)s,
            %(category)s,
            %(prompt)s,
            %(response)s,
            %(latency_seconds)s,
            %(input_tokens)s,
            %(output_tokens)s,
            %(status)s,
            %(error_message)s
        );
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, record)



if __name__ == "__main__":
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                version = cursor.fetchone()
                print("Connected successfully!")
                print(version[0])

        test_record = {
            "request_id": str(uuid.uuid4()),
            "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
            "prompt_id": None,
            "category": None,
            "prompt": "What is an LLM?",
            "response": "An LLM is a large language model.",
            "latency_seconds": 2.50,
            "input_tokens": 6,
            "output_tokens": 8,
            "status": "success",
            "error_message": None
        }

        save_record(test_record)
        print("Test record saved successfully!")

    except Exception as error:
        print("Database operation failed:", error)

