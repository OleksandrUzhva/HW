import datetime
import json
from dataclasses import dataclass

import requests

middle_currency = "CHF"
API_KEY = "D5G28HSZ0FWYD5WQ"


@dataclass
class Price:
    value: int
    currency: str

    def __str__(self):
        return f"Price(value={self.value}, currency='{self.currency}')"

    def __add__(self, other: "Price") -> "Price":
        if self.currency == other.currency:
            return Price(
                value=self.value + other.value,
                currency=self.currency,
            )

        left_in_middel: float = convert_to(
            value=self.value,
            currency_from=self.currency,
            currency_to=middle_currency,
        )

        right_in_middle: float = convert_to(
            value=other.value,
            currency_from=other.currency,
            currency_to=middle_currency,
        )

        total_in_middle: float = left_in_middel + right_in_middle
        total_in_left_currency = convert_to(
            value=total_in_middle,
            currency_from=middle_currency,
            currency_to=self.currency,
        )
        return Price(value=total_in_left_currency, currency=self.currency)


def convert_to(value: float, currency_from: str, currency_to: str) -> float:
    response: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={API_KEY}"
    )

    result: dict = response.json()
    with open("log.json", "a") as log:
        time_now = datetime.datetime.now()
        time: str = time_now.strftime("%d/%m/%y %H:%M")
        log_data = {
            "currency_from": result["Realtime Currency Exchange Rate"][
                "1. From_Currency Code"
            ],
            "currency_to": result["Realtime Currency Exchange Rate"][
                "3. To_Currency Code"
            ],
            "rate": result["Realtime Currency Exchange Rate"]["5. Exchange Rate"],
            "timestamp": time,
        }

        json.dump(log_data, log, indent=2)
        log.write("\n")

    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )
    return value * coefficient


flight = Price(value=200, currency="USD")
hotel = Price(value=350, currency="GBP")
total = flight + hotel
print(total)

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
