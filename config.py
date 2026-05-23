from dotenv import load_dotenv
import os
import sys
# Load local environment variables if testing locally

load_dotenv()

# --- CONFIGURATION & SECURITY GATEKEEPER ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")
DB_NAME = os.getenv("DB_NAME", "summaries.db")

if not GEMINI_API_KEY:
    sys.exit(1)
