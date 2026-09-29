def extract_even(l: list) -> list:
    """Return a list containing only the even intergers from the input list."""
    return [num for num in l if num % 2 == 0]

sample_list = [1, 4, 5, -1, 10]
even_numbers = extract_even(sample_list)
print(even_numbers) 