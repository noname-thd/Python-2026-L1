def print_pattern(m: int, n: int) -> None:
    '''Prints a hollow rectangular pattern of asterisks with m rows and n columns.'''
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print('', end='  ')
        print()

print_pattern(4, 5)