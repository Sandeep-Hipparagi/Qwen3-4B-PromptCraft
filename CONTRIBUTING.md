# Contributing to PromptCraft

Thank you for your interest in contributing to **PromptCraft: Zero-Reasoning System Prompt Engineering**! This document provides guidelines and instructions for contributing.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please treat everyone with respect and courtesy.

## How to Contribute

### Reporting Bugs

- **Check existing issues** before creating a new one
- **Provide a clear description** of the bug
- **Include reproduction steps** and expected vs. actual behavior
- **Attach relevant logs** or error messages
- **Specify your environment** (OS, Python version, dependencies)

### Suggesting Features

- **Describe the feature** clearly and provide use cases
- **Explain the motivation** behind the feature request
- **Provide examples** of how it would work
- **Link related issues** if applicable

### Pull Requests

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Ensure code quality**:
   - Follow PEP 8 style guidelines
   - Use type hints where appropriate
   - Write clear, descriptive commit messages

3. **Run tests**:
   ```bash
   pytest tests/
   ```

4. **Format your code**:
   ```bash
   black . --line-length 100
   isort .
   ```

5. **Push to your fork** and submit a Pull Request:
   - Include a clear description of your changes
   - Reference any related issues
   - Add screenshots or examples if relevant

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sandeep-Hipparagi/Qwen3-4B-PromptCraft.git
   cd Qwen3-4B-PromptCraft
   ```

2. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

3. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

## Coding Standards

- **Python Version**: Python 3.8+
- **Style Guide**: PEP 8
- **Linting**: flake8, isort, black
- **Type Hints**: Required for function signatures
- **Documentation**: Docstrings for all functions and classes

## Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage
- Use pytest for all test cases

## Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions
- Include examples for new features
- Update CHANGELOG.md

## Pull Request Process

1. Update documentation as needed
2. Ensure tests pass: `pytest`
3. Check code formatting: `black . && isort .`
4. Request review from maintainers
5. Address feedback and update PR

## Attribution

Contributors will be credited in:
- CONTRIBUTORS.md (if maintained)
- Release notes
- GitHub contributors page

## Questions?

Feel free to:
- Open a GitHub discussion
- Check existing issues and documentation
- Contact the maintainers

---

**Thank you for contributing to PromptCraft!** 🚀
