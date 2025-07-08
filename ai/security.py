from fastapi import Request, HTTPException
import requests

async def verify_xsuaa_token(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Missing authorization token")

    # Verify the token with xsuaa service
    response = requests.post("https://xsuaa-service-url/verify", headers={"Authorization": token})
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid authorization token")

    return True
