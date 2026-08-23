import json
from helpers import celsius_to_fahrenheit, is_palindrome

words = ["python", "AI", "react", "native", "ml"]
long_words = [w.upper() for w in words if len(w) > 4]
print(long_words)

word_lengths = {w: len(w) for w in words}
print(word_lengths)

lengths = {len(w) for w in words}
print(lengths)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None

print(divide(10, 2))   
print(divide(10, 0))

def get_value(data: dict, key: str):
    try:
        return data[key]
    except KeyError:
        print(f"Key '{key}' not found")
        return None
    except TypeError:
        print("data must be a dictionary")
        return None
    
profile = {"name": "Aaqib"}
print(get_value(profile, "age"))

def read_something():
    try:
        print("Trying...")
        raise ValueError("Something broke")
    except ValueError as e:
        print(f"Caught: {e}")
    finally:
        print("This always runs (e.g. closing a file/connection)")

read_something()

def set_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Validation failed: {e}")

with open("notes.txt", "w") as f:
    f.write("Day 2 learning log\n")
    f.write("Comprehensions, error handling, file I/O\n")

# Reading a file — line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("notes.txt", "a") as f:
    f.write("Appended line\n")            

# Reading the whole file at once
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
    

profile = {"name": "Aaqib", "role": "AI Developer", "skills": ["Python", "React Native"]}
with open("profile.json", "w") as f:
    json.dump(profile, f)           

with open("profile.json", "r") as f:
    loaded_profile = json.load(f)
    print(loaded_profile["skills"])

print(celsius_to_fahrenheit(30))     
print(is_palindrome("Was it a car or a cat I saw"))    
    
