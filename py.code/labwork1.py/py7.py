def remove_dollar_sign(s: str) -> str:
    """Removes all dollar signs from a given string."""
    return s.replace("$", "")

# Example Usage:
text = "$100.00 is $50 more than $50"
result = remove_dollar_sign(text)
print(result)