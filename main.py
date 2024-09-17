from fastapi import FastAPI, HTTPException
import requests
import time
from pydantic import BaseModel

app = FastAPI()

# A Pydantic model for the input data
class ReelInput(BaseModel):
    url: str

EXTERNAL_API = "https://instastorysave.com/api/reel?url="
MAX_RETRIES = 5
RETRY_DELAY = 0.5  # Seconds between retries

def get_instagram_data(url: str):
    """Call the existing external API to fetch data with retry logic."""
    attempt = 0
    while attempt < MAX_RETRIES:
        response = requests.get(f"{EXTERNAL_API}{url}")
        if response.status_code == 200:
            return response.json()
        else:
            attempt += 1
            if attempt < MAX_RETRIES:
                print(f"Retrying... {attempt}/{MAX_RETRIES}")
                time.sleep(RETRY_DELAY)  # Wait before retrying
            else:
                raise HTTPException(status_code=400, detail="Error fetching reel data after retries")

@app.post("/fetch-reel")
async def fetch_reel(data: ReelInput):
    
    # Call external API to fetch reel data
    reel_data = get_instagram_data(data.url)
    return reel_data

# Test endpoint to verify the API is up and running
@app.get("/")
async def root():
    return {"message": "Reel Fetcher API is live!"}
