import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fin-agent-hackathon-key-2026')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    
    # Storage Paths
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    SAMPLE_FOLDER = os.path.join(BASE_DIR, 'static', 'samples')
    DATABASE_PATH = '/tmp/financial_agent.db'
    
    # LangSmith Observability
    LANGCHAIN_TRACING_V2 = os.environ.get('LANGCHAIN_TRACING_V2', 'true')
    LANGCHAIN_API_KEY = os.environ.get('LANGCHAIN_API_KEY', '')
    LANGCHAIN_PROJECT = os.environ.get('LANGCHAIN_PROJECT', 'SME-Financial-Document-Agent')
    
    # App Settings
    MAX_CONTENT_LENGTH = 32 * 1024 * 1024  # 32 MB max upload
    ALLOWED_EXTENSIONS = {'pdf', 'csv', 'xlsx', 'xls', 'png', 'jpg', 'jpeg'}

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
os.makedirs(Config.SAMPLE_FOLDER, exist_ok=True)
