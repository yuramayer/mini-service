"""Test service for the shipping"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    """Такая вот заглушка"""
    return {"status": "ok"}
