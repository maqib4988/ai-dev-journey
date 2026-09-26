from pydantic import BaseModel, Field, ValidationError
from typing import Optional


# Define the shape of data you expect
class ExchangeRate(BaseModel):
    base: str
    date: str
    rates: dict[str, float]


# Validate real API data against it
import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
raw_data = response.json()

validated = ExchangeRate(**raw_data)  # unpacks dict into the model
print(validated.base)
print(validated.rates["PKR"])


# What happens with BAD data — this is the whole point of pydantic
class UserProfile(BaseModel):
    name: str
    age: int
    email: Optional[str] = None  # optional field, defaults to None if missing


try:
    good_user = UserProfile(name="Aaqib", age=27)
    print(good_user)

    bad_user = UserProfile(name="Sara", age="abc")  # wrong type
except ValidationError as e:
    print("Validation failed:")
    print(e)


# Field constraints — add validation rules
class Product(BaseModel):
    name: str
    price: float = Field(gt=0)  # must be greater than 0
    quantity: int = Field(ge=0)  # must be >= 0


try:
    p1 = Product(name="Laptop", price=1200, quantity=5)
    print(p1)

    p2 = Product(name="Broken item", price=-10, quantity=3)  # invalid price
except ValidationError as e:
    print(e)

# Converting a validated model back to a dict or JSON
print(p1.model_dump())  # -> dict
print(p1.model_dump_json())  # -> JSON string
