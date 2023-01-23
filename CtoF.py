# Program to convert Celsius to Fahrenheit temperatures.

import math

def main(args: list[str]) -> int:
    # Read a temperature in Celsius
    try:
        degC: float = float(input('Please enter a temperature in Celsius: '))
    except TypeError as e:
        print('PROBLEM: degrees Celsius must be a floating-point numbr.')
        print(e.args[0].capitalize())
    else:
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