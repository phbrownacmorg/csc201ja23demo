# Program to convert Celsius to Fahrenheit temperatures.

import math

def main(args: list[str]) -> int:
    # Read a temperature in Celsius
    degC: float = float(input('Please enter a temperature in Celsius: '))

    # Do the actual conversion
    degF: float = (degC * 9/5) + 32

    # Output the result
    print(str(degC) +'\u00B0 C =', str(degF) + '\u00b0 F')

    # Rounding
    print('Nearest \u00b0F:', round(degF))
    print('Ceiling:', math.ceil(degF))
    print('Floor:', math.floor(degF))

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)