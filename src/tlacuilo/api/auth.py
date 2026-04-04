from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

from tlacuilo.core import config

API_KEY = config.API_KEY
api_key_header = APIKeyHeader(name="X-API-Key")


def verify_key(key: str = Security(api_key_header)):
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return key
