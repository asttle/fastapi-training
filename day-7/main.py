from fastapi import FastAPI, HTTPException, Depends, Request
from mangum import Mangum

app = FastAPI()

handler = Mangum(app)

@app.get("/")
async def home(request: Request):
    return {"message": "Hello, FastAPI on AWS Lambda!"}