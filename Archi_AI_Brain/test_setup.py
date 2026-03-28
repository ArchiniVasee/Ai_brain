import os
from dotenv import load_dotenv

# This line looks for your .env file
load_dotenv()

def test_imports():
    try:
        import langchain
        import openai
        import pinecone
        print("✅ Success: All AI libraries are installed correctly!")
    except ImportError as e:
        print(f"❌ Error: Missing a library: {e}")

if __name__ == "__main__":
    test_imports()
    print("Next step: Wait for Monday to add the API Keys!")