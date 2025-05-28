import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Please set the GEMINI_API_KEY environment variable.")
    exit()

genai.configure(api_key=api_key)

result = genai.embed_content(
    model="models/embedding-001",
    content="Something is better than nothing"
)

print(result['embedding'])
