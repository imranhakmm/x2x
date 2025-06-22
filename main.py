from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse

app = FastAPI(title="x2 Calculator")


@app.get("/calculator/{value}", response_class=HTMLResponse)
async def double(
    value: float = Path(..., description="Number to double", alias="value")
):
    result = value * 2
    # inline HTML so no template engine is needed
    return f"""
    <html>
      <head><title>x2 Calculator</title></head>
      <body style="display:flex;justify-content:center;align-items:center;
                   height:100vh;font-family:sans-serif;">
        <h1 style="font-size:4rem;margin:0;">{result}</h1>
      </body>
    </html>
    """
