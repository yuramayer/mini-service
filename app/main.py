"""Test service for the shipping"""

from fastapi import FastAPI
import tomllib

app = FastAPI()


@app.get("/health")
def health():
    """Такая вот заглушка"""
    return {"status": "ok"}


with open('config.toml', 'rb') as f:
    config = tomllib.load(f)
