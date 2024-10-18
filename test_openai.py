import openai
import os

def test_openai_setup():
    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        print("OpenAI library imported successfully and API key is set.")
        return True
    except ImportError:
        print("Failed to import OpenAI library.")
        return False
    except KeyError:
        print("OpenAI API key not found in environment variables.")
        return False

if __name__ == "__main__":
    test_openai_setup()
