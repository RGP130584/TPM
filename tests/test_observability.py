from tpm.observability.ai_metrics.models import AITokenMetrics


def test_ai_metrics():
    metrics = AITokenMetrics(
        context_size=1000,
        prompt_tokens=50,
        completion_tokens=100,
        total_tokens=150,
        cost_estimation=0.003,
    )
    assert metrics.total_tokens == 150
    assert metrics.cost_estimation == 0.003
