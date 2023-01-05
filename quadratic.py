# Program to do nothing, correctly.
import math

def main(args: list[str]) -> int:
    # Read the quadratic system (a, b, and c)
    print('Solve a quadratic system of the form a * x**2 + b * x + c = 0')
    a: float = float(input('Please enter a value for a: '))
    b: float = float(input('Please enter a value for b: '))
    c: float = float(input('Please enter a value for c: '))
    print('The system is', a, '* x**2 +', b, '* x +', c, '= 0')

    # Find the determinant
    det: float = math.pow(b, 2) - 4*a*c
    # Test
    #print(det)
    # Take the square root of the determinant
    # (Yes, this may crash if the determinant is negative.
    #  We'll see how to avoid that later in the course.)
    detroot: float = math.sqrt(det)

    # Test that
    #print(detroot)

    # Find the roots
    root1: float = (-b + detroot)/(2*a)
    root2: float = (-b - detroot)/(2*a)
    print('The roots are:', root1, root2)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)