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
    amounts: list[float] = [P]
    for i in range(periods):
        interest: float = P * rate
        P = P + interest
        amounts.append(round(P, 2))
    print(amounts)

    max_P: float = max(amounts)
    print('Maximum principal is $' + str(round(P, 2)))

    margin: float = 0.1

    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)

    # Set the coordinates the match the problem.
    # Effectively, bar_width == 1 and height_per_dollar = 1
    win.setCoords(-margin * (len(amounts)), -margin * max_P, 
                len(amounts)/(1 - margin), max_P / (1 - margin))
    
    origin: Point = Point(0, 0)
    end: Point = Point(len(amounts) * (1 + (margin/2)), 0)
    x_axis: Line = Line(origin, end)
    x_axis.setArrow('last')
    x_axis.draw(win)

    # Axis labels
    ## X axis
    ### Tick marks
    #### Find the spacing for the tick marks so there aren't *too* many of them
    tick_spacing: int = 1
    while (len(amounts) / tick_spacing) > 30:
        tick_spacing = tick_spacing * 10
    # Using math.ceil so the tick marks go all the way to the end of the axis
    for i in range(math.ceil(len(amounts)/ tick_spacing)):
        top: Point = Point(i * tick_spacing + 0.5, 0)
        bottom: Point = Point(i * tick_spacing + 0.5, 
                                -margin/10 * max_P)
        tick: Line = Line(top, bottom)
        tick.draw(win)

    end = Point(0, max_P * (1 + margin/2))
    y_axis: Line = Line(origin, end)
    y_axis.setArrow('last')
    y_axis.draw(win)

    # Axis labels
    ## Y axis
    ### Tick marks
    #### Find the spacing for the tick marks so there aren't *too* many of them
    tick_spacing = 1
    while (max_P / tick_spacing) > 30:
        tick_spacing = tick_spacing * 10

    # Using math.ceil so the tick marks go all the way to the end of the axis
    for i in range(math.ceil(max_P / tick_spacing)):
        right: Point = Point(0, i * tick_spacing)
        left: Point = Point(-margin/10 * len(amounts), 
                            i * tick_spacing) 
        tick = Line(left, right)
        tick.draw(win)

        # Y-axis label
        label:Text = Text(Point((-margin/2) * len(amounts), i * tick_spacing), 
                        '$' + str(i * tick_spacing))
        label.draw(win)



    # Bars
    for i in range(len(amounts)):
        # Draw bars
        bar: Rectangle = Rectangle(Point(i, 0), Point(i+1, amounts[i]))
        bar.setFill('green')
        bar.draw(win)

        # Period labels
        label = Text(Point(i+0.5, -margin/4 * max_P), str(i))
        label.draw(win)

        # Amount labels
        label = Text(Point(i+0.5, (margin/5 * max_P) + amounts[i]),
                        '$' + str(amounts[i]))
        label.setSize(6)
        label.draw(win)
        

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)