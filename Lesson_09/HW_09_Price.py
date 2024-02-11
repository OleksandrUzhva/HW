class Price:
    def __init__(self, value: int, currency: str, exchange_rates: dict):
        self.value: int = value
        self.currency: str = currency
        self.exchange_rates: dict = exchange_rates

    def __str__(self):
        return f"Price(value={self.value}, currency='{self.currency}')"

    def convert_to(self, currency: str) -> "Price":
        chf_currency = self.exchange_rates[self.currency]
        chf_value = self.value * chf_currency
        converted_value = chf_value

        return Price(
            value=converted_value, currency=currency, exchange_rates=self.exchange_rates
        )

    def __add__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(
                value=self.value + other.value,
                currency=self.currency,
                exchange_rates=self.exchange_rates,
            )
        else:
            price = self.convert_to(self.currency) + other.convert_to(self.currency)
            return price.convert_to(self.currency)

    def __sub__(self, other) -> "Price":
        if self.currency == other.currency:
            return Price(
                value=self.value - other.value,
                currency=self.currency,
                exchange_rates=self.exchange_rates,
            )
        else:
            price = self.convert_to(self.currency) - other.convert_to(self.currency)
            return price.convert_to(self.currency)


exchange_rates = {
    "USD": 0.87,
    "EUR": 0.94,
    "GBP": 0.90,
    "UAH": 0.023,
    "CNY": 0.12,
}

flight = Price(value=200, currency="USD", exchange_rates=exchange_rates)
hotel = Price(value=1300, currency="GBP", exchange_rates=exchange_rates)
total = flight + hotel
print(total)
