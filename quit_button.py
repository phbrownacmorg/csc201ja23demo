# Program to open a graphics window and draw nothing, correctly.
from graphics import *
from typing import cast

def inButton(button: Rectangle, p: Point) -> bool:
    p1: Point = button.getP1()
    p2: Point = button.getP2()
    minX: float = min(p1.getX(), p2.getX())
    maxX: float = max(p1.getX(), p2.getX())
    minY: float = min(p1.getY(), p2.getY())
    maxY: float = max(p1.getY(), p2.getY())
    return minX <= p.getX() <= maxX and minY <= p.getY() <= maxY

def makeButton(p1: Point, p2:Point, text: str, win:GraphWin) -> Rectangle:
    button: Rectangle = Rectangle(p1, p2)
    button.draw(win)
    center: Point = button.getCenter()
    label: Text = Text(center, text)
    label.draw(win)
    return button

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)
    win.setCoords(-1, -1, 1, 1)

    button: Rectangle = makeButton(Point(-.1, .1), Point(.1, -.1), 'Quit', win)
    mouseLabel: Text = Text(Point(0, .9), 'Mouse: (none)')
    mouseLabel.draw(win)

    for i in range(8):
        click: Point = cast(Point, win.getMouse()) # Wait for a mouse click
        mouseLabel.setText('Mouse: ({0:.4f}, {1:.4f})'.format(click.getX(), click.getY()))

        if inButton(button, click):
            win.close()
            break

    # Close the window when clicked on
    if not win.isClosed():
        win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)