# Day 6: FastAPI Training

## Overview

This project demonstrates a simple FastAPI application with HTML template rendering.

## Files

- **main.py**: Contains the FastAPI application logic.
- **templates/home.html**: HTML template rendered for the home route.

## Features

- Serves a homepage using Jinja2 templates.
- Uses FastAPI's `Request` object for template context.
- Renders `home.html` at the root (`/`) endpoint.

## Usage

1. **Install dependencies**:
    ```bash
    pip install fastapi uvicorn jinja2
    ```

2. **Run the server**:
    ```bash
    uvicorn main:app --reload
    ```

3. **Access the app**:
    Open [http://localhost:8000](http://localhost:8000) in your browser.

## main.py Example

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
     return templates.TemplateResponse("home.html", {"request": request})
```

## home.html Example

```html
<!DOCTYPE html>
<html>
<head>
     <title>FastAPI Home</title>
</head>
<body>
     <h1>Welcome to FastAPI Training Day 6!</h1>
</body>
</html>
```

## Notes

- Ensure the `templates` folder is in the same directory as `main.py`.
- Modify `home.html` to customize the homepage content.
- Use FastAPI's template support for dynamic HTML rendering.
