# Program to open a graphics window and draw nothing, correctly.
from graphics import *
import math

def main(args: list[str]) -> int:
    # Read input
    # Initial amount invested (principal)
    P: float = float(input('Please input the amount to invest: $'))
    # Interest rate *per compounding period*
    rate: float = float(input('Please input the interest rate, in percent: '))
    # Number of periods to invest for
    periods: int = int(input('Please enter the number of periods for which to invest: '))

    # Echo back the initial conditions
    print('Investing $' + str(round(P, 2)), 'at', str(rate) + '% for', periods, 'periods.')

    # Convert rate from a percentage to a straight quantity
    rate = rate/100
    max_P: float = P * (1 + rate)**periods
    print('Maximum principal is $' + str(round(P, 2)))

    margin: float = 0.1

    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 500, 500)

    # Set the coordinates the match the problem.
    # Effectively, bar_width == 1 and height_per_dollar = 1
    win.setCoords(-margin * (periods+1), -margin * max_P, 
                (periods + 1)/(1 - margin), max_P / (1 - margin))
    
    origin: Point = Point(0, 0)
    end: Point = Point((periods + 1) * (1 + (margin/2)), 0)
    x_axis: Line = Line(origin, end)
    x_axis.setArrow('last')
    x_axis.draw(win)
    
    end = Point(0, max_P * (1 + margin/2))
    y_axis: Line = Line(origin, end)
    y_axis.setArrow('last')
    y_axis.draw(win)

    # Bars
    for i in range(periods+1):
        bar: Rectangle = Rectangle(Point(i, 0), Point(i+1, P))
        bar.setFill('green')
        bar.draw(win)

        interest: float = P * rate
        P = P + interest

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)