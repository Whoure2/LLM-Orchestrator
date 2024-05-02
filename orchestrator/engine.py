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
\n# Maintenance log 1\n# Maintenance log 2\n# Maintenance log 3\n# Maintenance log 4\n# Maintenance log 5\n# Maintenance log 6\n# Maintenance log 7\n# Maintenance log 8\n# Maintenance log 9\n# Maintenance log 10\n# Maintenance log 13\n# Maintenance log 14\n# Maintenance log 15\n# Maintenance log 16\n# Maintenance log 18\n# Maintenance log 19\n# Maintenance log 20\n# Maintenance log 23\n# Maintenance log 25\n# Maintenance log 26\n# Maintenance log 27\n# Maintenance log 28\n# Maintenance log 29\n# Maintenance log 31\n# Maintenance log 32\n# Maintenance log 33\n# Maintenance log 35\n# Maintenance log 36\n# Maintenance log 37\n# Maintenance log 38\n# Maintenance log 39\n# Maintenance log 40\n# Maintenance log 41\n# Maintenance log 43\n# Maintenance log 44\n# Maintenance log 45\n# Maintenance log 46\n# Maintenance log 47\n# Maintenance log 48\n# Maintenance log 49\n# Maintenance log 53\n# Maintenance log 54\n# Maintenance log 55\n# Maintenance log 58\n# Maintenance log 59\n# Maintenance log 60\n# Maintenance log 61\n# Maintenance log 62\n# Maintenance log 63\n# Maintenance log 64\n# Maintenance log 65\n# Maintenance log 66\n# Maintenance log 67\n# Maintenance log 68\n# Maintenance log 69\n# Maintenance log 70\n# Maintenance log 71\n# Maintenance log 73\n# Maintenance log 74\n# Maintenance log 76\n# Maintenance log 77\n# Maintenance log 79\n# Maintenance log 80\n# Maintenance log 81\n# Maintenance log 82\n# Maintenance log 83\n# Maintenance log 84\n# Maintenance log 85\n# Maintenance log 86\n# Maintenance log 88