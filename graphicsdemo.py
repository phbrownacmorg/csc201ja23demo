# Program to open a graphics window and draw nothing, correctly.
from graphics import *

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)

    # Plot a few pixels
    win.plotPixel(10, 10, 'red')
    win.plotPixel(10, 790, 'green')
    win.plotPixel(790, 10, 'blue')
    win.plotPixel(790, 790, 'orange')

    # Points
    center: Point = Point(400, 400)
    center.setOutline('black')
    center.draw(win)
    p1: Point = Point(200, 200)
    p1.setOutline('red')
    p1.draw(win)
    p2: Point = Point(600, 200)
    p2.setOutline('blue')
    p2.draw(win)
    p3: Point = Point(200, 600)
    p3.setOutline('green')
    p3.draw(win)
    p4: Point = Point(600, 600)
    p4.setOutline('orange')
    p4.draw(win)
    p5: Point = Point(400, 600)
    p5.setOutline('brown')
    p5.draw(win)
    p6: Point = Point(600, 400)
    p6.setOutline('purple')
    p6.draw(win)


    # Line
    line: Line = Line(p1, p2)
    line.setOutline('green')
    line.draw(win)

    # Rectangle
    rect: Rectangle = Rectangle(p1, p5)
    rect.setFill('skyblue')
    rect.draw(win)

    # Circle
    circ: Circle = Circle(center, 40)
    circ.setFill('lightgreen')
    circ.draw(win)

    # Oval
    oval: Oval = Oval(p6, p1)
    oval.setFill('pink')
    oval.draw(win)

    # Polygons
    tri: Polygon = Polygon(center, p2, p4)
    tri.setFill('gray')
    tri.draw(win)

    # Text
    text: Text = Text(center, 'Hello, world!')
    text.draw(win)

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)