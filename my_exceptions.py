class ZeroError(Exception):
    """Custom exception for the ZeroError."""

def is_zero(x):
    if x == 0:
        raise ZeroError("Error: x cannot be zero.")

class IsHundredError(Exception):
    """Custom exception for the IsHundredError."""

def is_hundred(n):
    if n >= 100:
        raise IsHundredError("You´ve reached the limit of 100 units")