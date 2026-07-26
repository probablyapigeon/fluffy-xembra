import random

def apply_volatility(mood):
    mood += random.uniform(-15, 15)
    return max(0, min(100, mood))
