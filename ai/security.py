from fastapi import HTTPException
import os

def get_current_user(token: str):
    # Validate the token with xsuaa service
    xsuaa_url = os.getenv("XSUAA_URL")
    response = requests.get(f"{xsuaa_url}/userinfo", headers={"Authorization": f"Bearer {token}"})
    
    if response.status_code == 200:
        return response.()
    else:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
