"""
Basic usage example for PromptCraft model.

This example demonstrates how to use the PromptCraft model to generate
system prompts from natural language descriptions.
"""

from llama_cpp import Llama


def load_model(model_path: str) -> Llama:
    """
    Load the PromptCraft GGUF model.

    Args:
        model_path: Path to the GGUF model file

    Returns:
        Loaded Llama model instance
    """
    return Llama(
        model_path=model_path,
        n_ctx=2048,
        n_threads=8,
        n_gpu_layers=-1,  # Use GPU if available
    )


def generate_system_prompt(model: Llama, description: str) -> str:
    """
    Generate a system prompt from a natural language description.

    Args:
        model: Loaded Llama model instance
        description: Natural language description of the desired prompt

    Returns:
        Generated system prompt
    """
    prompt = f"""<|im_start|>user
Transform this into a system prompt: '{description}'
<|im_end|>
<|im_start|>assistant
"""

    response = model(
        prompt,
        max_tokens=2048,
        stop=["<|im_end|>"],
        temperature=0.3,
        top_p=0.9,
    )

    return response["choices"][0]["text"].strip()


def main():
    """Run basic usage example."""
    # Load model
    print("Loading PromptCraft model...")
    model = load_model("Qwen3_4B_PromptCraft_GGUF_Q4_K_M.gguf")

    # Example prompts
    examples = [
        "FastAPI validation layer",
        "Python error handler with retry logic",
        "RESTful API authentication system",
    ]

    # Generate system prompts
    for example in examples:
        print(f"\n{'='*60}")
        print(f"Input: {example}")
        print(f"{'='*60}")

        system_prompt = generate_system_prompt(model, example)
        print(f"Generated Prompt:\n{system_prompt}")


if __name__ == "__main__":
    main()
