# AIFL-Documentation

An AI Interchange Format Language (AIFL) for seamless communication between AI agents.

## Overview

AIFL-Documentation is a project aimed at creating a standardized language and protocols for AI agents to communicate effectively. It includes parsers, executors, and communication protocols to facilitate interoperability among diverse AI systems.

## Features

- **AIFL Parser and Executor**: Parse and execute AIFL expressions using a standardized set of symbols and grammar.
- **Standardized Symbols and Grammar**: Utilize a consistent set of symbols and grammar rules defined in the `docs/SYMBOLS.md` and `docs/GRAMMAR.md` files.
- **Communication Protocols**: Define protocols for AI agent communication to enable seamless interaction between different AI systems.
- **Extensibility**: Easily extend the language and protocols to accommodate new requirements and AI functionalities.
- **Security Measures**: Implement data encryption and security protocols to ensure safe communication and data handling between AI agents.

## Project Structure

- `src/`: Contains the source code files, including the parser (`aifl_parser.py`), executor (`aifl_executor.py`), and other core components.
- `tests/`: Includes all test files to ensure the correctness and reliability of the codebase.
- `docs/`: Contains documentation files, such as symbols definitions, grammar rules, communication protocols, and the project roadmap.
- `assets/`: Holds images and other asset files used in documentation or the project.

## Installation

To get started with AIFL-Documentation, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/gcharris/AIFL-Documentation.git
   cd AIFL-Documentation
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.7 or higher installed. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:

   If your project uses environment variables (e.g., for API keys), set them up accordingly. **Do not include your actual API key in any files or commit it to version control.**

   For Unix-based systems:

   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

   For Windows PowerShell:

   ```powershell
   $env:OPENAI_API_KEY='your-api-key-here'
   ```

   **Note**: Replace `'your-api-key-here'` with your actual API key when running the commands, but **do not** include the key in your code or documentation.

## Usage

You can use the AIFL executor to parse and execute AIFL expressions. Here's an example:

```python
from src.aifl_executor import AIFLExecutor

executor = AIFLExecutor()
expression = "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256') ∧ ΔΙ5 ⇒ ΔΖ3"
result = executor.execute(expression)
print(result)
```

**Sample Output**:

```
Executed operation: ⇒
  Left: Executed operation: ∧
    Left: Executed function: ΔΕ1(Data: SensitiveInfo, EncryptionType: AES256)
    Right: Executed symbol: ΔΙ5
  Right: Executed symbol: ΔΖ3
```

## Communication Protocols

To enable AI agents to communicate seamlessly, we've defined standardized communication protocols documented in `docs/PROTOCOLS.md`.

- **Message Format**: JSON-based messages that include sender, receiver, message type, and content.
- **Transport Layer**: Uses HTTP with RESTful APIs for communication between agents.
- **Security**: Communications are secured using TLS encryption and include authentication mechanisms.

For detailed information, refer to the [Communication Protocols Documentation](docs/PROTOCOLS.md).

## Documentation

- **Symbols Definition**: See `docs/SYMBOLS.md` for a comprehensive list of symbols and their meanings.
- **Grammar Rules**: Refer to `docs/GRAMMAR.md` for detailed grammar rules used in parsing AIFL expressions.
- **Project Roadmap**: Check `docs/ROADMAP.md` for upcoming milestones and development plans.

## Contributing

We welcome contributions to AIFL-Documentation! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) to get started.

To contribute:

1. **Fork the Repository**: Click the "Fork" button on GitHub.

2. **Create a Feature Branch**:

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**:

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the Branch**:

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**: Submit your changes for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need assistance, please [open an issue](https://github.com/gcharris/AIFL-Documentation/issues) on GitHub.

## Acknowledgments

- **Contributors**: Thank you to all the contributors who have helped develop this project.
- **Resources**: This project utilizes libraries such as Lark for parsing and follows AI communication standards inspired by FIPA.
