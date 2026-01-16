
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Friend server is running 🚀"}




















