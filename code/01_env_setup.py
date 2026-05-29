import os
from dotenv import load_dotenv

load_dotenv()

# Use OpenRouter key from .env (starts with sk-or-)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
