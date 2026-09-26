import requests
from pydantic import BaseModel, ValidationError
import matplotlib.pyplot as plt


class RateSnapshot(BaseModel):
    base: str
    date: str
    rates: dict[str, float]


def fetch_rates(base_currency: str = "USD") -> RateSnapshot | None:
    try:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}", timeout=5
        )
        response.raise_for_status()
        return RateSnapshot(**response.json())
    except (requests.exceptions.RequestException, ValidationError) as e:
        print(f"Failed to fetch/validate rates: {e}")
        return None


data = fetch_rates("USD")

if data:
    # Pick a few currencies to compare
    currencies = ["PKR", "EUR", "GBP", "INR", "AED"]
    values = [data.rates[c] for c in currencies if c in data.rates]
    labels = [c for c in currencies if c in data.rates]

    plt.bar(labels, values)
    plt.title(f"Exchange Rates vs {data.base} ({data.date})")
    plt.ylabel("Rate")
    plt.show()

    print(f"1 {data.base} = {data.rates['PKR']} PKR as of {data.date}")
