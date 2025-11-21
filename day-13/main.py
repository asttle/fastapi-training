from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from collections import defaultdict
from typing import Dict

app = FastAPI()

class AdvancedMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.rate_limit_records: Dict[str, float] = defaultdict(float)
    
    async def log_message(self, message: str):
        # Here you would implement logging to a file or external service
        print(f"LOG: {message}")

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        # Rate limiting: allow one request every 2 seconds per IP
        if current_time - self.rate_limit_records[client_ip] < 2:
            await self.log_message(f"Rate limit exceeded for IP: {client_ip}")
            return Response("Too Many Requests", status_code=429)

        self.rate_limit_records[client_ip] = current_time

        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        
        response.headers["X-Process-Time"] = f"{process_time:.4f}s"

        await self.log_message(
            f"Request from {client_ip} took {process_time:.4f} seconds"
        )

        return response

app.add_middleware(AdvancedMiddleware)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}