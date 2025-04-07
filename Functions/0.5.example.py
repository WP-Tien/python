from datetime import datetime

def show_date() -> None:
    print('This is the current date and time:')
    print(datetime.now())

show_date()


def greet(name: str) -> None:
    print(f'Hello {name}')

greet('Vincent')
greet('Ruby')


def add(a: float, b: float) -> float:
    return a + b

print(add(6, 4))