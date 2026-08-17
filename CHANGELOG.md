# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-17

### Added
- Initial release of PromptCraft: Zero-Reasoning System Prompt Engineering
- Qwen3-4B-PromptCraft GGUF quantized model
- Support for llama.cpp inference
- Parameter-Efficient Fine-Tuning (LoRA) via Unsloth
- 2,050+ high-entropy instruction pairs training dataset
- Architectural constraints framework:
  - Executive Summary: Structural logic of the prompt
  - Implementation Artifact: Core system instructions
  - Edge Case Matrix: Failure mode identification and mitigations
- Comprehensive documentation and examples
- Apache 2.0 License
- Model hosting on Hugging Face Model Hub

### Planned
- Python package installation via pip
- Web UI for interactive prompt generation
- API server for prompt generation
- Extended model variants (7B, 14B)
- Fine-tuning scripts for custom datasets
- Integration with popular LLM frameworks

---

## Version Format

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes and improvements

## How to Report Changes

Please follow these guidelines:
1. Keep each change brief and clear
2. Group related changes under the same category
3. Link to relevant GitHub issues or PRs when applicable
4. Use past tense for descriptions
