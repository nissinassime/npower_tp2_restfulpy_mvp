import random

MAX_INT32 = 2**31 - 1

def generate_ids() -> int:
    return random.randint(1, MAX_INT32)