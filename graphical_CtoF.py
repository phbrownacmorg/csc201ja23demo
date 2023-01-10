# Program to open a graphics window and draw nothing, correctly.
from graphics import *

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 550, 100)
    win.setCoords(-1, -1, 1, 1)

    instructions: Text = Text(Point(0, 0.8),
        'Enter a temperature in Celsius.  Click outside the box to convert to Fahrenheit.')
    instructions.draw(win)

    degC_blank: Entry = Entry(Point(-0.5, 0), 5)
    degC_blank.draw(win)
    degC_label: Text = Text(Point(-0.3, 0), '\u00b0C')
    degC_label.draw(win)

    win.getMouse() # Wait for the click to convert

    # Now, do the conversion
    degC: float = float(degC_blank.getText())
    degF: float = (degC * 9/5) + 32

    # Display the result
    results_label: Text = Text(Point(0.2, 0), 
                            '= ' + str(round(degF, 1)) + '\u00b0 F')
    results_label.draw(win)

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)