def get_divisors(n):
    '''Return a sorted list of all divisors of a number'''
    if n <= 0:
        return []

    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors
print(get_divisors(36))


