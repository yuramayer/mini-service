"""Test service for the shipping"""

from fastapi import FastAPI, Request
import tomllib
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()

logger.info('mini-service started')


with open('config.toml', 'rb') as f:
    config = tomllib.load(f)


@app.middleware('http')
async def log_requests(request: Request, call_next):
    logger.info(f' >> {request.method} {request.url}')
    response = await call_next(request)
    logger.info(f' << {response.status_code} {request.url}')
    return response


@app.get("/health")
def health():
    """Такая вот заглушка"""
    return {"status": "ok"}


@app.get('/config_message')
def config_message():
    """Месседж из конфига"""
    return {'msg': config['server']['message']}
