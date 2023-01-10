# Program to open a graphics window and draw nothing, correctly.
from graphics import *

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 700, 300)
    win.setCoords(-1, -1, 1, 1)

    instructions: Text = Text(Point(0, 0.8), 
        'Enter a color specification (name or hex specification) in the blank.  Click elsewhere to use it.')
    instructions.draw(win)

    colorblank: Entry = Entry(Point(0, 0.6), 16)
    colorblank.draw(win)

    swatch: Rectangle = Rectangle(Point(-.8, .5), Point(.8, -.9))
    swatch.draw(win)

    win.getMouse()
    colorspec:str = colorblank.getText()
    swatch.setFill(colorspec)
    instructions.setText('Click once more to exit.')

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)