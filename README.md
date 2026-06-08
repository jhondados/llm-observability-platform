# 🔭 LLM Observability Platform

[![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-✓-blue)](.) [![LangSmith](https://img.shields.io/badge/LangSmith-✓-orange)](.) [![Traces](https://img.shields.io/badge/Traces-10M%2Fday-green)](.)

> **Full-stack LLM monitoring** processing **10M traces/day**. Tracks token costs, latency, quality scores, hallucinations and prompt injections. Integrates with LangSmith, Arize AI and custom Grafana dashboards.

## 📊 What Gets Tracked
- **Token economics**: cost per session, per user, per feature — real-time
- **Quality**: faithfulness, relevancy, groundedness scored automatically
- **Safety**: prompt injection detection (99.1%), PII leakage prevention
- **Performance**: P50/P95/P99 latency, timeout rates, retry counts
- **Drift**: quality degradation alerts when metrics drop > 10%

## 🏗️ Architecture
```
LLM Calls → OpenTelemetry SDK → Collector → ClickHouse (traces)
                                          → Grafana (dashboards)
                                          → PagerDuty (alerts)
                                          → LangSmith (debugging)
```
