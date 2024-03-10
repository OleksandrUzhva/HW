from datetime import datetime, timedelta

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


cached_exchange_rate = {"timestamp": None, "data": None}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def is_cache_valid():
    timestamp = cached_exchange_rate["timestamp"]
    if timestamp is None:
        return False
    current_time = datetime.utcnow()
    return (current_time - timestamp) < timedelta(seconds=10)


@app.get("/currency-exchange")
async def currency(currency_from: str, currency_to: str):
    if is_cache_valid():
        return {"rate": cached_exchange_rate["data"], "cached": True}

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey=D5G28HSZ0FWYD5WQ"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        rate = response.json()

    cached_exchange_rate["timestamp"] = datetime.utcnow()
    cached_exchange_rate["data"] = rate

    return {"rate": cached_exchange_rate["data"], "cached": False}
