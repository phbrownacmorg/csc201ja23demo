# Program to open a graphics window and draw nothing, correctly.
from graphics import *
import math

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)

    P: float = 1000
    rate: float = 0.02
    periods: int = 10

    # Make a bar graph

    origin: Point = Point(50, 750)
    end: Point = Point(750, 750)

    # X axis
    xAxis: Line = Line(origin, end)
    xAxis.setArrow('last')
    xAxis.draw(win)

    # Y axis
    end.move(-700, -700)
    yAxis: Line = Line(origin, end)
    yAxis.setArrow('last')
    yAxis.draw(win)

    # Bars
    x_axis_length: float = abs(xAxis.getP2().getX() - xAxis.getP1().getX())
    y_axis_length: float = abs(yAxis.getP2().getY() - yAxis.getP1().getY())
    bar_width: int = math.floor(x_axis_length / (periods+1))
    # Blithely assume P doesn't do more than double
    height_per_dollar: float = y_axis_length / (2*P)

    # Now, do bars  
    bar: Rectangle = Rectangle(origin,
                                Point(origin.getX() + bar_width,
                                    origin.getY() - P * height_per_dollar))
    bar.setFill('green')
    bar.draw(win)
    for i in range(periods):
        # Find the interest
        interest: float = P * rate

        # Add on the interest
        P = P + interest

        # Draw the bar
        next_bar: Rectangle = bar # next_bar is now an alias for bar
        next_bar_clone: Rectangle = bar.clone() # No aliasing here!
        next_bar_clone.draw(win)

        # Also moves bar (same object), but next_bar_clone stays (different object)
        next_bar.move(bar_width, -interest) 

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)