from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import uvicorn

from module_1 import add
from module_2 import sub
from module_3 import mult

app = FastAPI()

@app.get("/")
def root():
    return{"status":"Ok"}

@app.get("/index", response_class=HTMLResponse)
def index():
    html_content = Path("static/index.html").read_text()
    return html_content

@app.get("/add")
def addition(a:float,b:float=10):
    return add(a,b)

@app.get("/sub")
def substraction(a:float,b:float=10):
    return sub(a,b)

@app.get("/mult")
def multiplication(a:float,b:float=10):
    return mult(a,b)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)