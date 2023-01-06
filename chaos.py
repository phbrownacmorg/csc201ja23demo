# File: chaos.py
# A simple program illustrating chaotic (mathematical) behavior.
import math

def main(args: list[str]) -> int:
    print('This program illustrates a chaotic function.')
    # Accumulator variable
    x: float = float(input('Enter a number between 0 and 1: '))

    EPSILON: float = 0.000001 # Really small value

    # Clamp x to the range [0, 1], in case the user didn't
    x = min(x, 1 - EPSILON) # Handles x too big
    x = max(x, 0 + EPSILON) # Handles x too small

    # Loop
    for i in range(10): # type: int
        # Each time through the loop, the accumulator variable
        # is modified to include the next piece of answer.
        x = 3.9 * x * (1 - x)
        print(x)
    return 0  # Conventional return value for successful completion

if __name__ == '__main__':
    import sys
    main(sys.argv)
