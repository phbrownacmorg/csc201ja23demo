# Program to open a graphics window and draw nothing, correctly.
from graphics import *
from typing import cast

def drawTriangle(win: GraphWin) -> None:
    pts: list[Point] = [] # 1. Accumulator variable
    for i in range(3):    # 2. Loop
        p: Point = cast(Point, win.getMouse())
        p.draw(win)
        pts.append(p) # 3. Update the accumulator in the loop

    # Once we've accumulated 3 points, draw a triangle
    tri: Polygon = Polygon(pts)
    tri.draw(win)

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)
    win.setCoords(-1, -1, 1, 1)

    drawTriangle(win)

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)