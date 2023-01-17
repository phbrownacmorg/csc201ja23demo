# Program to open a graphics window and draw nothing, correctly.
from graphics import *
import math
from typing import cast

def makeMouseEar(x_sign: int, r: float, color: str) -> GraphicsObject:
    angle: float = 55 # angle from horizontal in degrees
    scale: float = 1.3
    x_offset: float = x_sign * scale * r * math.cos(math.radians(angle))
    y_offset: float = scale * r * math.sin(math.radians(angle))
    ear: Circle = Circle(Point(x_offset, y_offset), r * 0.6)
    ear.setFill(color)
    ear.setOutline(color)
    return ear

def makeEye(x_sign: int, r: float, color: str) -> GraphicsObject:
    angle: float = 50
    x_offset: float = x_sign * r * math.cos(math.radians(angle))
    y_offset: float = r * math.sin(math.radians(angle))
    topPt: Point = Point(x_offset, y_offset)
    x_offset = x_sign * r * 0.1
    bottomPt: Point = Point(x_offset, 0)
    eye: Oval = Oval(topPt, bottomPt)
    eye.setFill(color)
    return eye

def makeMouthLine(x_sign: int, r: float) -> Line:
    angle: float = 20 # Angle below vertical in degrees
    y_below: float = r * -0.3
    inPt: Point = Point(0, y_below)
    scale: float = 0.4
    out_x: float = x_sign * r * math.cos(math.radians(angle)) * scale
    out_y: float = y_below - r * math.sin(math.radians(angle)) * scale
    outPt: Point = Point(out_x, out_y)
    return Line(inPt, outPt)

def makeWhisker(x_sign: int, y_val: int, r: float) -> Line:
    angle: float = y_val * 10
    in_scale: float = 0.8
    out_scale: float = 1.8
    x: float = x_sign * in_scale * r * math.cos(math.radians(angle))
    y: float = in_scale * r * math.sin(math.radians(angle))
    inPt: Point = Point(x, y)
    x = x_sign * out_scale * r * math.cos(math.radians(angle))
    y = out_scale * r * math.sin(math.radians(angle))
    outPt: Point = Point(x, y)
    return Line(inPt, outPt)

def makeCatEar(x_sign: int, r: float, color: str) -> GraphicsObject:
    centralAngle: float = 55 # angle from horizontal in degrees
    widthAngle: float = 10
    outer_scale: float = 1.3

    x = x_sign * outer_scale * r * math.cos(math.radians(centralAngle))
    y = outer_scale * r * math.sin(math.radians(centralAngle))
    tip: Point = Point(x, y)
    x = x_sign * r * math.cos(math.radians(centralAngle + widthAngle))
    y = r * math.cos(math.radians(centralAngle + widthAngle))
    base1: Point = Point(x, y)
    x = x_sign * r * math.cos(math.radians(centralAngle - widthAngle))
    y = r * math.cos(math.radians(centralAngle - widthAngle))
    base2: Point = Point(x, y)
    ear: Polygon = Polygon(tip, base1, base2)
    ear.setFill(color)
    ear.setOutline(color)
    return ear

# Define an animal as a list of GraphicsObjects, all of which
# move together.  It always starts at the origin.
def makeMouse(r: float) -> list[GraphicsObject]:
    color: str = 'gray30'
    animal: list[GraphicsObject] = []
    head: Circle = Circle(Point(0, 0), r)
    head.setFill(color)
    animal.append(head)

    # Make ears
    for x_sign in [-1, 1]:
        animal.append(makeMouseEar(x_sign, r, color))

    # Ears and eyes aren't interleaved to ensure the right order in the list
    for x_sign in [-1, 1]: 
        animal.append(makeEye(x_sign, r, 'black'))

    # Nose
    nose = Circle(Point(0, 0), r * 0.1)
    nose.setFill('black')
    animal.append(nose)

    # Mouth
    for x_sign in [-1, 1]:
        animal.append(makeMouthLine(x_sign, r))

    for x_sign in [-1, 1]:
        for y_val in [-1, 0, 1]:
            animal.append(makeWhisker(x_sign, y_val, r))

    return animal

def makeCat(r: float) -> list[GraphicsObject]:
    cat: list[GraphicsObject] = []
    color: str = 'orange'
    head: Circle = Circle(Point(0, 0), r)
    head.setFill(color)
    cat.append(head)

    for x_sign in [-1, 1]:
        cat.append(makeCatEar(x_sign, r, color))

    return cat

def drawAnimal(animal: list[GraphicsObject], win: GraphWin) -> None:
    for part in animal:
        part.draw(win)

def animalCenter(animal: list[GraphicsObject]) -> Point:
    return cast(Circle, animal[0]).getCenter()

def moveAnimal(animal: list[GraphicsObject], dx: float, dy: float) -> None:
    for part in animal:
        part.move(dx, dy)

def main(args: list[str]) -> int:
    # Create and open a window to draw in
    win: GraphWin = GraphWin('Graphics window', 800, 800)
    win.setCoords(-1, -1, 1, 1)

    mouse: list[GraphicsObject] = makeMouse(0.05)
    drawAnimal(mouse, win)

    cat: list[GraphicsObject] = makeCat(0.125)
    moveAnimal(cat, 2, 2) # Put the cat out
    drawAnimal(cat, win)

    label: Text = Text(Point(0, 0.9), 'Mouse click: (none)')
    label.draw(win)

    # 5 is an arbitrary number of mouse clicks to collect
    for i in range(5):
        click: Point = cast(Point, win.getMouse())
        label.setText('Mouse click: Point({0:0.3f}, {1:0.3f})'.format(click.getX(), click.getY()))

        # Mouse jumps to the click
        mousePos: Point = animalCenter(mouse)
        moveAnimal(mouse, click.getX() - mousePos.getX(),
                    click.getY() - mousePos.getY())

        # Cat jumps to where the mouse just was
        catPos: Point = animalCenter(cat)
        moveAnimal(cat, mousePos.getX() - catPos.getX(),
                    mousePos.getY() - catPos.getY())

    # Close the window when clicked on
    win.getMouse() # Wait for a mouse click
    win.close()

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)