# Program to calculate the future value of a fixed-rate investment.

def main(args: list[str]) -> int:
    # Read input
    # Initial amount invested (principal)
    # This is the accumulator variable
    P: float = float(input('Please input the amount to invest: $'))
    # Attempt to validate P
    if not (P > 0): # Wall Street, we have a problem
        print('The amount to invest must be positive.  Please try again.')
        return 1 # No sensible way to recover
    # No maximum investmant (practically speaking)

    # Interest rate *per compounding period*
    rate: float = float(input('Please input the interest rate, in percent: '))
    if not (rate > 0):
        print('The rate must be greater than 0.  Please try again.')
        return 1 # No sensible way to recover
    # No maximum interest rate (practically speaking)

    # Doubling the investment
    target_P: float = 2 * P

    # Echo back the initial conditions
    print('Investing $' + str(round(P, 2)), 'at', str(rate) + '% until it doubles.')
    print()

    # Print the column headers for the table
    print('Period\tInterest\tAmount')
    # Print the first line of the table
    print('Initial\t\t\t$' + str(P))

    # Convert rate from a percentage to a straight quantity
    rate = rate/100
    # Calculate and print the rest of the rows
    # Loop (for the accumulator pattern)
    i: int = 0
    while P < target_P:
        # Print the period column
        print(i+1, end='\t')

        # Find the interest
        interest: float = P * rate
        # Print the interest
        print('$' + str(round(interest, 2)), end='\t\t')

        # Add on the interest
        # (or, accumulate a little more of the answer into
        #  the accumulator variable)
        P = P + interest
        # Print the new principal
        print('$' + str(round(P, 2)), end='')

        print() # End the line
        # Update the period number
        i = i + 1

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)