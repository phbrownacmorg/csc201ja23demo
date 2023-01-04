# Program to convert Celsius to Fahrenheit temperatures.

def main(args: list[str]) -> int:
    # Read a temperature in Celsius
    degC: float = float(input('Please enter a temperature in Celsius: '))

    # Do the actual conversion
    degF: float = (degC * 9/5) + 32

    # Output the result
    print(degC, 'degrees Celsius =', degF, 'degrees Fahrenheit')
    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)