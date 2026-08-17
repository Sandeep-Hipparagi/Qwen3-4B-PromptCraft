"""
Advanced usage example for PromptCraft model.

This example demonstrates advanced features including:
- Batch prompt generation
- Constraint-based prompt generation
- Custom configuration
"""

from typing import List, Dict
from llama_cpp import Llama


class PromptCraftGenerator:
    """Advanced PromptCraft prompt generator."""

    def __init__(self, model_path: str, **llama_kwargs):
        """
        Initialize the generator.

        Args:
            model_path: Path to the GGUF model file
            **llama_kwargs: Additional kwargs for Llama initialization
        """
        default_kwargs = {
            "n_ctx": 2048,
            "n_threads": 8,
            "n_gpu_layers": -1,
        }
        default_kwargs.update(llama_kwargs)
        self.model = Llama(model_path=model_path, **default_kwargs)

    def generate_prompt(
        self,
        description: str,
        constraints: List[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 2048,
    ) -> str:
        """
        Generate a system prompt with optional constraints.

        Args:
            description: Natural language description
            constraints: List of constraints to apply
            temperature: Generation temperature (0.0-1.0)
            max_tokens: Maximum tokens to generate

        Returns:
            Generated system prompt
        """
        constraint_text = ""
        if constraints:
            constraint_text = "\n\nConstraints:\n" + "\n".join(
                f"- {c}" for c in constraints
            )

        prompt = f"""<|im_start|>user
Generate a comprehensive system prompt for: '{description}'{constraint_text}
<|im_end|>
<|im_start|>assistant
"""

        response = self.model(
            prompt,
            max_tokens=max_tokens,
            stop=["<|im_end|>"],
            temperature=temperature,
            top_p=0.9,
        )

        return response["choices"][0]["text"].strip()

    def batch_generate(
        self, descriptions: List[str], **kwargs
    ) -> List[Dict[str, str]]:
        """
        Generate multiple prompts.

        Args:
            descriptions: List of descriptions
            **kwargs: Additional kwargs for generate_prompt

        Returns:
            List of generated prompts with metadata
        """
        results = []
        for desc in descriptions:
            prompt = self.generate_prompt(desc, **kwargs)
            results.append({"description": desc, "prompt": prompt})
        return results


def main():
    """Run advanced usage example."""
    # Initialize generator
    generator = PromptCraftGenerator("Qwen3_4B_PromptCraft_GGUF_Q4_K_M.gguf")

    # Example 1: Simple prompt generation
    print("Example 1: Simple Prompt Generation")
    print("=" * 60)
    prompt = generator.generate_prompt("API rate limiter with sliding window")
    print(prompt)

    # Example 2: Prompt with constraints
    print("\n\nExample 2: Prompt with Constraints")
    print("=" * 60)
    constraints = [
        "Must handle edge cases",
        "Should be production-ready",
        "Include error handling",
    ]
    prompt = generator.generate_prompt(
        "Database connection pool",
        constraints=constraints,
    )
    print(prompt)

    # Example 3: Batch generation
    print("\n\nExample 3: Batch Prompt Generation")
    print("=" * 60)
    descriptions = [
        "Caching layer with TTL",
        "WebSocket connection handler",
        "Message queue consumer",
    ]
    results = generator.batch_generate(descriptions)
    for result in results:
        print(f"\nDescription: {result['description']}")
        print(f"Prompt: {result['prompt'][:200]}...")


if __name__ == "__main__":
    main()
