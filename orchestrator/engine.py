import json
import requests

class LLMOrchestrator:
    """Orchestrates complex multi-step tasks across different LLM providers."""
    def __init__(self, api_key, provider="openai"):
        self.api_key = api_key
        self.provider = provider
        self.context_history = []

    def add_to_context(self, role, content):
        self.context_history.append({"role": role, "content": content})
        if len(self.context_history) > 10:
            self.context_history.pop(0)

    def generate_response(self, prompt):
        self.add_to_context("user", prompt)
        response = f"Generated response for: {prompt[:20]}..."
        self.add_to_context("assistant", response)
        return response

    def evaluate_output(self, reference, hypothesis):
        ref_tokens = reference.lower().split()
        hyp_tokens = hypothesis.lower().split()
        lcs_matrix = [[0] * (len(hyp_tokens) + 1) for _ in range(len(ref_tokens) + 1)]
        for i in range(1, len(ref_tokens) + 1):
            for j in range(1, len(hyp_tokens) + 1):
                if ref_tokens[i-1] == hyp_tokens[j-1]:
                    lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
                else:
                    lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
        lcs = lcs_matrix[len(ref_tokens)][len(hyp_tokens)]
        return (2 * lcs) / (len(ref_tokens) + len(hyp_tokens)) if (len(ref_tokens) + len(hyp_tokens)) > 0 else 0
\n# Maintenance log 1\n# Maintenance log 2\n# Maintenance log 3\n# Maintenance log 4\n# Maintenance log 5\n# Maintenance log 6\n# Maintenance log 7\n# Maintenance log 8