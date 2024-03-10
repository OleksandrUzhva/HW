import json

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/currency-exchange")
async def currency(currency_from, currency_to):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey=D5G28HSZ0FWYD5WQ"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        rate = response.json()
        with open("currency.json", "a") as log:
            log_data = {
                "currency_from": rate["Realtime Currency Exchange Rate"][
                    "1. From_Currency Code"
                ],
                "currency_to": rate["Realtime Currency Exchange Rate"][
                    "3. To_Currency Code"
                ],
                "rate": rate["Realtime Currency Exchange Rate"]["5. Exchange Rate"],
            }

        json.dump(log_data, log, indent=2)
        log.write("\n")

    return rate


# {
#     "Realtime Currency Exchange Rate": {
#         "1. From_Currency Code": "USD",
#         "2. From_Currency Name": "United States Dollar",
#         "3. To_Currency Code": "JPY",
#         "4. To_Currency Name": "Japanese Yen",
#         "5. Exchange Rate": "150.72200000",
#         "6. Last Refreshed": "2024-02-14 14:04:02",
#         "7. Time Zone": "UTC",
#         "8. Bid Price": "150.71710000",
#         "9. Ask Price": "150.72900000"
#     }
# }
