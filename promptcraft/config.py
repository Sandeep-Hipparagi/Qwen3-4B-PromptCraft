"""Configuration management for PromptCraft."""

import os
from typing import Any, Dict
from pathlib import Path
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration manager for PromptCraft."""

    def __init__(self, config_file: str = None):
        """
        Initialize configuration.

        Args:
            config_file: Path to YAML configuration file
        """
        self.config = {}
        if config_file and os.path.exists(config_file):
            with open(config_file, "r") as f:
                self.config = yaml.safe_load(f) or {}
        self._load_env_vars()

    def _load_env_vars(self):
        """Load environment variables into config."""
        env_mapping = {
            "MODEL_PATH": "model.model_path",
            "HF_REPO_ID": "model.hf_repo_id",
            "N_CTX": "inference.n_ctx",
            "N_THREADS": "inference.n_threads",
            "N_GPU_LAYERS": "inference.n_gpu_layers",
            "TEMPERATURE": "inference.temperature",
            "TOP_P": "inference.top_p",
            "MAX_TOKENS": "inference.max_tokens",
            "LOG_LEVEL": "logging.level",
            "CACHE_ENABLED": "cache.enabled",
            "DEBUG": "debug",
        }

        for env_key, config_key in env_mapping.items():
            value = os.getenv(env_key)
            if value:
                self._set_nested(config_key, value)

    def _set_nested(self, key: str, value: Any):
        """Set a nested configuration value."""
        keys = key.split(".")
        current = self.config
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.

        Args:
            key: Dot-separated configuration key
            default: Default value if key not found

        Returns:
            Configuration value
        """
        keys = key.split(".")
        current = self.config
        for k in keys:
            if isinstance(current, dict):
                current = current.get(k)
            else:
                return default
        return current if current is not None else default

    def to_dict(self) -> Dict:
        """Get configuration as dictionary."""
        return self.config.copy()


# Default configuration instance
_default_config = None


def get_config() -> Config:
    """Get the default configuration instance."""
    global _default_config
    if _default_config is None:
        config_path = Path(__file__).parent.parent / "config" / "default_config.yaml"
        _default_config = Config(str(config_path))
    return _default_config
