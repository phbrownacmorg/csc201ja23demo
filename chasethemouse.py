# Program to open a graphics window and draw nothing, correctly.
from graphics import *

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)
    win.setCoords(-1, -1, 1, 1)

    mouse: Circle = Circle(Point(0, 0), 0.05)
    mouse.setFill('gray30')
    mouse.draw(win)

    label: Text = Text(Point(0, 0.9), 'Mouse click: (none)')
    label.draw(win)

    # 5 is an arbitrary number of mouse clicks to collect
    for i in range(5):
        click: Point = win.getMouse()
        label.setText('Mouse click: Point({0:0.3f}, {1:0.3f})'.format(click.getX(), click.getY()))

        mousePos: Point = mouse.getCenter()
        mouse.move(click.getX() - mousePos.getX(),
                    click.getY() - mousePos.getY())

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)