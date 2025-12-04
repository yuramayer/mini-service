"""Test service for the shipping"""

from fastapi import FastAPI
import tomllib

app = FastAPI()


with open('config.toml', 'rb') as f:
    config = tomllib.load(f)


@app.get("/health")
def health():
    """Такая вот заглушка"""
    return {"status": "ok"}


@app.get('/config_message')
def config_message():
    """Месседж из конфига"""
    return {'msg': config['server']['message']}
