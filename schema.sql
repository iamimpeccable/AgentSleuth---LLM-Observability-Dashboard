
CREATE TABLE IF NOT EXISTS llm_requests (
    request_id UUID PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    model_name VARCHAR(100) NOT NULL,
    prompt_id VARCHAR(20),
    category VARCHAR(50),
    prompt TEXT NOT NULL,
    response TEXT,
    latency_seconds NUMERIC(10, 2),
    input_tokens INTEGER,
    output_tokens INTEGER,
    status VARCHAR(20) NOT NULL,
    error_message TEXT
);