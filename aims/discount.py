def total_cost_with_discount(total, percent):
    """Return the total after a percentage discount in the range 0..100."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return total * (1 - percent / 100)
