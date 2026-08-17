"""Main PromptCraft generator module."""

from typing import List, Optional, Dict
import logging

logger = logging.getLogger(__name__)


class PromptGenerator:
    """Generate system prompts using PromptCraft model."""

    def __init__(self, model_path: str, **kwargs):
        """
        Initialize the prompt generator.

        Args:
            model_path: Path to the GGUF model file
            **kwargs: Additional configuration options
        """
        self.model_path = model_path
        self.config = kwargs
        self.model = None
        logger.info(f"Initializing PromptGenerator with model: {model_path}")

    def generate(
        self,
        description: str,
        constraints: Optional[List[str]] = None,
        **kwargs,
    ) -> str:
        """
        Generate a system prompt from a description.

        Args:
            description: Natural language description of desired prompt
            constraints: Optional list of constraints
            **kwargs: Additional generation parameters

        Returns:
            Generated system prompt
        """
        raise NotImplementedError("Subclasses must implement generate()")

    def batch_generate(self, descriptions: List[str]) -> List[Dict]:
        """
        Generate multiple prompts.

        Args:
            descriptions: List of descriptions

        Returns:
            List of generated prompts with metadata
        """
        results = []
        for desc in descriptions:
            try:
                prompt = self.generate(desc)
                results.append({"description": desc, "prompt": prompt, "success": True})
            except Exception as e:
                logger.error(f"Error generating prompt for {desc}: {e}")
                results.append(
                    {
                        "description": desc,
                        "prompt": None,
                        "success": False,
                        "error": str(e),
                    }
                )
        return results
