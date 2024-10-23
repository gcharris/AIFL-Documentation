#!/bin/bash
# install.sh

echo "Installing AIFL dependencies..."

# Install core requirements
pip install --no-cache-dir flask==2.2.2 python-dotenv==0.19.0 lark-parser==0.11.3

# Install AI-related packages
pip install --no-cache-dir openai>=1.0.0 requests>=2.26.0

# Install testing packages
pip install --no-cache-dir pytest>=7.0.0 watchdog>=2.1.9

echo "Dependencies installed successfully!"
