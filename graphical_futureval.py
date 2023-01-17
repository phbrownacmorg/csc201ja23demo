# Program to open a graphics window and draw nothing, correctly.
from graphics import *
import math

def read_params() -> tuple[float, float, int]:
    # Read input
    # Initial amount invested (principal)
    P: float = float(input('Please input the amount to invest: $'))
    # Interest rate *per compounding period*
    rate: float = float(input('Please input the interest rate, in percent: '))
    # Number of periods to invest for
    periods: int = int(input('Please enter the number of periods for which to invest: '))

    # Converts rate from a percentage to a straight quantity
    return P, (rate / 100), periods

def find_amounts(P: float, rate: float, periods: int) -> list[float]:
    amounts: list[float] = [P]
    for i in range(periods):
        interest: float = P * rate
        P = P + interest
        amounts.append(P)
    return amounts

def find_tick_spacing(max_value: float) -> int:
    #### Find the spacing for the tick marks so there aren't *too* many of them
    MAX_TICKS = 20
    spacing = 1
    while (max_value / spacing) > MAX_TICKS:
        spacing = spacing * 10
    return spacing

def draw_line(start: Point, end: Point, w: GraphWin) -> Line:
    line: Line = Line(start, end)
    line.draw(w)
    return line

def draw_axis(direction: Point, max_x: float, max_y: float, margin: float, win: GraphWin,
                decoration: str = '') -> None:
    # Draw an axis, with tick marks and labels.  Only works for axes
    # in the positive direction. 

    dir_x: float = direction.getX()
    dir_y: float = direction.getY()
    origin: Point = Point(0, 0)
    # direction is 0 in the dimension where the axis doesn't go
    end: Point = Point(dir_x * max_x * (1 + (margin/2)),
                        dir_y * max_y * (1 + (margin/2)))
    axis: Line = draw_line(origin, end, win)
    axis.setArrow('last')

    ### Tick marks
    axis_length: float = max(dir_x * max_x, dir_y * max_y)
    #### Find the spacing for the tick marks so there aren't *too* many of them
    tick_spacing: float = find_tick_spacing(axis_length)
    # Using math.ceil so the tick marks go all the way to the end of the axis
    for i in range(math.ceil(axis_length / tick_spacing)):
        tick_length: float = max((margin/10) * max_x * dir_y,
                                (margin/10) * max_y * dir_x)
        axis_pos: float = i * tick_spacing + 0.5

        # Tick marks
        inside: Point = Point(axis_pos * dir_x, axis_pos * dir_y)
        outside: Point = Point(axis_pos * dir_x + -tick_length * dir_y,
                                axis_pos * dir_y + -tick_length * dir_x)
        draw_line(inside, outside, win)

        # Axis labels
        # Offset from axis is different in X and Y because we write horizontally
        anchor: Point = Point(axis_pos * dir_x + -tick_length * 5 * dir_y,
                                axis_pos * dir_y + -tick_length * 3 * dir_x)
        text: str = decoration + str(int(axis_pos))
        label: Text = Text(anchor, text)
        label.draw(win)

def draw_bars(amounts: list[float], margin: float, win: GraphWin) -> None:
    max_y: float = max(amounts)
    for i in range(len(amounts)):
        # Draw bars
        bar: Rectangle = Rectangle(Point(i, 0), Point(i+1, amounts[i]))
        bar.setFill('green')
        bar.draw(win)

        # Amount labels
        label = Text(Point(i+0.5, (margin/5 * max_y) + amounts[i]),
                        '${0:.2f}'.format(amounts[i]))
        label.setSize(8) # Specific to the window size
        label.draw(win)

def show_on_graph(amounts: list[float]) -> None:     
    max_x: float = len(amounts)
    max_y: float = max(amounts)
    print('Maximum principal is $' + str(round(max_y, 2)))

    margin: float = 0.1

    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)

    # Set the coordinates the match the problem.
    # Effectively, bar_width == 1 and height_per_dollar = 1
    win.setCoords(-margin * (max_x), -margin * max_y, 
                max_x/(1 - margin), max_y / (1 - margin))
    
    origin: Point = Point(0, 0)

    # Axis labels
    ## X axis
    draw_axis(Point(1, 0), max_x, max_y, margin, win)
    ## Y axis
    draw_axis(Point(0, 1), max_x, max_y, margin, win, '$')

    draw_bars(amounts, margin, win)
        
    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

def main(args: list[str]) -> int:
    # Read input
    P, rate, periods = read_params()

    # Echo back the initial conditions
    print('Investing $' + str(round(P, 2)), 'at', str(rate) + '% for', periods, 'periods.')

    amounts: list[float] = find_amounts(P, rate, periods)

    show_on_graph(amounts)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)