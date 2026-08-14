<img width="1400" height="349" alt="1785490203883" src="https://github.com/user-attachments/assets/98f9a734-2591-44c4-8428-8cc35f336bfc" />

# PromptCraft: Zero-Reasoning System Prompt Engineering

[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-yellow)](https://huggingface.co/Sandeep4235/Qwen3-4B-PromptCraft-GGUF)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Abstract
PromptCraft is a specialized 4B parameter model fine-tuned from the Qwen3 architecture. It is engineered specifically for **Zero-Reasoning System Prompt Generation**, ensuring that complex system instructions are generated with production-grade constraints without leaking internal chain-of-thought or `<think>` tags.

## Model Architecture & Deployment
- **Base Model:** Qwen3-4B
- **Fine-tuning Method:** Parameter-Efficient Fine-Tuning (LoRA) via Unsloth
- **Quantization:** GGUF (Q4_K_M) for optimized edge deployment
- **Primary Hosting:** [Hugging Face Model Hub](https://huggingface.co/Sandeep4235/Qwen3-4B-PromptCraft-GGUF)

## Methodology
### Training Objective
The model was trained to solve the 'Reasoning Leak' problem in modern LLMs. By distilling 2,050+ high-entropy instruction pairs, PromptCraft focuses on immediate implementation artifacts over conversational filler.

### Architectural Constraints
1. **Executive Summary**: Structural logic of the prompt.
2. **Implementation Artifact**: The core system instructions.
3. **Edge Case Matrix**: Identification of failure modes and mitigations.

## Usage
To run the quantized version locally via `llama.cpp`:

```bash
./llama-cli -m Qwen3_4B_PromptCraft_GGUF_Q4_K_M.gguf \
  -p "<|im_start|>user
Transform this into a system prompt: 'FastAPI validation layer'
<|im_end|>
<|im_start|>assistant
"
```

## Citation
If you use this model in your research or production workflows, please attribute the work to **BluePatterns AI**.
