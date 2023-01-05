# Program to calculate a factorial using the accumulator pattern.

def main(args: list[str]) -> int:
    print('This program calculates a factorial.')
    # Read the number
    n: int = int(input('Please enter a positive integer: '))
    print(str(n) + '! =', end=' ')

    # Accumulator variable
    fact: int = 1 # Initial value is the identity element for multiplication

    # Loop
    for i in range(1, n+1): # type: int
        # Accumulate the answer into the accumulator variable
        fact = fact * i

    print(fact)
    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)