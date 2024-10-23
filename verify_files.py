# verify_files.py
import py_compile
import os

def verify_files():
    # List of files to check
    files_to_check = [
        'src/aifl/ai_integrations/base.py',
        'src/aifl/ai_integrations/openai_integration.py',
        'src/aifl/ai_integrations/claude_integration.py',
        'src/aifl/ai_integrations/gemini_integration.py',
        'src/aifl/ai_integrations/__init__.py',
        'src/aifl/__init__.py',
        'src/aifl/aifl_executor.py',
        'src/aifl/aifl_parser.py',
        'src/aifl/encryption.py',
        'src/aifl/config.py',
        'src/app.py'
    ]

    for file_path in files_to_check:
        try:
            if os.path.exists(file_path):
                print(f"Verifying {file_path}...")
                py_compile.compile(file_path, doraise=True)
                print(f"✓ {file_path} is valid Python code")
            else:
                print(f"✗ File not found: {file_path}")
        except Exception as e:
            print(f"✗ Error in {file_path}: {str(e)}")

if __name__ == "__main__":
    verify_files()