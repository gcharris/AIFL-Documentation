# Installation

This guide will walk you through the process of installing AIFL in your development environment.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Steps

1. Clone the AIFL repository:
   ```
   git clone https://github.com/your-username/AIFL-Documentation.git
   cd AIFL-Documentation
   ```

2. Install the required dependencies:
   ```
   pip install openai cryptography
   ```

3. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```

   Note: Replace 'your-api-key-here' with your actual OpenAI API key. Never share your API key publicly.

4. Verify the installation:
   ```
   python verify_api_key.py
   ```

   If the installation is successful, you should see a message confirming that the OpenAI API key is present in the environment variables.

## Next Steps

Once you've completed the installation, proceed to the [Quick Start](quick-start.md) guide to begin using AIFL.
