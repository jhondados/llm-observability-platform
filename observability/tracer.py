"""LLM observability with OpenTelemetry."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import time, tiktoken
from functools import wraps

def setup_tracing(endpoint: str = "http://otel-collector:4317"):
    provider = TracerProvider()
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
    trace.set_tracer_provider(provider)
    return trace.get_tracer("llm-platform")

tracer = setup_tracing()

def trace_llm_call(model: str = "gemini-1.5-pro"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(f"llm.{func.__name__}") as span:
                start = time.perf_counter()
                result = func(*args, **kwargs)
                latency = (time.perf_counter() - start) * 1000
                enc = tiktoken.encoding_for_model("gpt-4")  # proxy tokenizer
                prompt = str(args[0]) if args else ""
                input_tokens = len(enc.encode(prompt))
                span.set_attributes({"llm.model": model, "llm.latency_ms": latency,
                    "llm.input_tokens": input_tokens, "llm.cost_usd": input_tokens * 0.0000025})
                return result
        return wrapper
    return decorator
