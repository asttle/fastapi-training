import os
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv

# Load .env from project tree regardless of cwd
_dotenv_path = find_dotenv(usecwd=True)
load_dotenv(_dotenv_path)

username_raw = os.getenv("MONGODB_USERNAME", "")
password_raw = os.getenv("MONGODB_PASSWORD", "")
username = quote_plus(username_raw)
password = quote_plus(password_raw)
cluster_url = os.getenv("MONGODB_CLUSTER_URL", "test-cluster.fqaqn7y.mongodb.net")
app_name = os.getenv("MONGODB_APP_NAME", "test-cluster")

if not username_raw or not password_raw:
    raise RuntimeError("Missing MongoDB credentials: set MONGODB_USERNAME and MONGODB_PASSWORD in environment or .env")

uri = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName={app_name}"

client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]