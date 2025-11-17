from fastapi import FastAPI
from redis import Redis
import httpx
import json

app = FastAPI()
redis_client = Redis(host='localhost', port=6379)

@app.on_event("startup")
async def startup_event():
    # Initialize Redis connection or any other startup tasks
    app.state.redis = Redis(host='localhost', port=6379)
    app.state.http_client = httpx.AsyncClient()
    print("Application startup: Redis and HTTP client initialized.")

@app.on_event("shutdown")
async def shutdown_event():
    # Clean up resources on shutdown
    app.state.redis.close()
    print("Application shutdown: Resources cleaned up.")

@app.get("/entries")
async def read_item():
    value = app.state.redis.get("list")
    if value is None:
        response = await app.state.http_client.get("https://api.artic.edu/api/v1/artworks/search?q=cats")
        data_str = json.dumps(response.json())
        app.state.redis.set("list", data_str)
        return response.json()
    return json.loads(value)



