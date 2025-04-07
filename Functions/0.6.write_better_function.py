from datetime import datetime
from collections.abc import Iterable

# 1. Short and concise
# 2. Specify a return type 
# 3. Make as simple and reusable as posible
# 4. Document all your functions
# 5. Handle errors approriately

def get_time() -> str:
    now: datetime = datetime.now()
    return f'{now:%X}'

print(get_time())


x = 10

def get_total_discount(prices: Iterable[float], percent: float) -> float:
    global x
    
    # Validate input
    if not ( 0 <= percent <= 1 ) :
        raise ValueError(f'Invalid discount rate: {percent}. Must be between 0 and 1 inclusive.')

    if not all(isinstance(price, (int, float)) and price >= 0 for price in prices):
        raise ValueError('All prices mus be non-negative number.')

    total: float = sum(prices)
    return total * (1-percent)


print( get_total_discount([100.0, 50.0, 25.0], 0.2) )