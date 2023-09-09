def print_pattern(n, symbol='*', pattern_type='solid'):
    """
    Prints diamond pattern of a specified type.

    Args:
        n (int): The size of the pattern.
        symbol (str, optional): The symbol to use for the pattern. Defaults to '*'.
        pattern_type (str, optional): The type of pattern to print ('border', 'solid', or 'hollow'). Defaults to 'solid'.

    Returns:
        None
    """
    if pattern_type == "border":
        for y in range(0, 2 * n + 1):
            for x in range(0, 2 * n + 1):
                if -y == x - n or y == x - n or y == x + n or -y == x - 3 * n:
                    print(symbol, end='')
                else:
                    print(' ', end='')
            print()
    elif pattern_type == "solid":
        for y in range(0, 2 * n + 1):
            for x in range(0, 2 * n + 1):
                if -y <= x - n and y >= x - n and y <= x + n and -y >= x - 3 * n:
                    print(symbol, end='')
                else:
                    print(end=' ')
            print()
    elif pattern_type == "hollow":
        for y in range(0, 2 * n + 1):
            for x in range(0, 2 * n + 1):
                if -y < x - n and y > x - n and y < x + n and -y > x - 3 * n:
                    print(' ', end='')
                else:
                    print(symbol, end='')
            print()
    else:
        print("Invalid pattern_type. Please choose 'border', 'solid', or 'hollow'.")

# Example usage:
n = 4
pattern_type = "border"
print_pattern(n, pattern_type=pattern_type)
