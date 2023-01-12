# File: chaos.py
# A simple program illustrating chaotic (mathematical) behavior.
import math

def main(args: list[str]) -> int:
    print('This program illustrates a chaotic function.')
    filename: str = input('Please enter a filename to read seeds from: ')

    EPSILON: float = 0.000001 # Really small value

    with open(filename, 'r') as infile:
        with open('chaos-out.txt', 'w') as outfile:
            for line in infile.readlines():
                numbers: list[str] = line.split()
                x: float = float(numbers[0]) # Seed.  Functions as an accumulator variable.
                n: int = int(numbers[1])     # Number of iterations

                # Clamp x to the range [0, 1], in case the user didn't
                x = min(x, 1 - EPSILON) # Handles x too big
                x = max(x, 0 + EPSILON) # Handles x too small

                outfile.write('\n')
                outfile.write(' i\t    x\n')
                outfile.write('-' * 20 + '\n')
                # Loop
                for i in range(n): # i is an int
                    # Each time through the loop, the accumulator variable
                    # is modified to include the next piece of answer.
                    x = 3.9 * x * (1 - x)
                    outfile.write('{0:>3d}\t{1:0.6f}\n'.format(i+1,x))

    return 0  # Conventional return value for successful completion

if __name__ == '__main__':
    import sys
    main(sys.argv)
