import logging
from fastapi import HTTPException
import os
import requests
from cachetools import TTLCache

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cache for token validation
token_cache = TTLCache(maxsize=100, ttl=300)

def get_current_user(token: str):
    # Check if token is cached
    if token in token_cache:
        logger.info("Token found in cache")
        return token_cache[token]

    # Validate the token with xsuaa service
    xsuaa_url = os.getenv("XSUAA_URL")
    try:
        response = requests.get(f"{xsuaa_url}/userinfo", headers={"Authorization": f"Bearer {token}"})
        response.raise_for_status()
        user_info = response.()

        # Cache validated token
        token_cache[token] = user_info
        logger.info(f"Token validated and cached for user: {user_info['user_name']}")
        return user_info
    except requests.exceptions.RequestException as e:
        logger.error(f"Token validation failed: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid or expired token")
