name = "Aaqib"
age = 28
is_learning = True

print(f"{name} is {age} years old")

skills = ["React Native", "Kotlin", "Python"]
skills.append("FastAPI")

print(skills)

squares = [x**2 for x in range(10)]
print(squares)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

profile = {"name": "Aaqib", "role": "AI Developer", "years_exp": 3.5}
for key, value in profile.items():
    print(f"{key}: {value}")  

def greet(name: str, times: int = 1) -> str:
    return f"Hello {name}! " * times    

print(greet("World", 3))

class Developer:
    def __init__(self, name: str, stack: list):
        self.name = name
        self.stack = stack

    def introduce(self):
        return f"{self.name} works with {', '.join(self.stack)}"

me = Developer("Aaqib", ["React Native", "Python"])
print(me.introduce())