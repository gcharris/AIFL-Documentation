import os

def verify_openai_api_key():
    if 'OPENAI_API_KEY' in os.environ:
        print("OpenAI API key is present in the environment variables.")
        return True
    else:
        print("OpenAI API key is not found in the environment variables.")
        return False

if __name__ == "__main__":
    verify_openai_api_key()
