# Program to do nothing, correctly.
import math

def interactive_running_sum() -> None:
    numlist: list[float] = []

    # Start value as a nonsense value
    instring: str = input("Please enter a number, or Q to quit: ")
    quitsign: str = 'Q'.casefold() # Sentinel

    while instring.strip().casefold() != quitsign:
        num: float = float(instring)
        numlist.append(num)
        print(numlist, sum(numlist), sum(numlist) / len(numlist))
        instring = input("Please enter a number, or Q to quit: ")

def negative_sentinel() -> None:
    numlist: list[float] = []

    # Start value as a nonsense value
    num: float = float(input("Please enter a number, or a negative number to quit: "))

    while num >= 0:
        numlist.append(num)
        print(numlist, sum(numlist), sum(numlist) / len(numlist))
        num = float(input("Please enter a number, or a negative number to quit: "))

def empty_string_sentinel() -> None:
    numlist: list[float] = []

    # Start value as a nonsense value
    instring: str = input("Please enter a number, or just hit Enter to quit: ")
    quitsign: str = '' # Sentinel

    while instring.strip() != quitsign:
        num: float = float(instring)
        numlist.append(num)
        print(numlist, sum(numlist), sum(numlist) / len(numlist))
        instring = input("Please enter a number, or just hit Enter to quit: ")

def exception_sentinel() -> None:
    numlist: list[float] = []

    try:
        # Start value as a nonsense value

        while True:
            num: float = float(input("Please enter a number, or anything else to quit: "))
            numlist.append(num)
            print(numlist, sum(numlist), sum(numlist) / len(numlist))
    except ValueError:
        pass

def readline_running_sum(fname: str) -> None:
    numlist: list[float] = []

    with open(fname, 'r') as f:
        line = f.readline()
        while line != '':
            lineparts: list[str] = line.split()
            try:
                num: float = float(lineparts[0])
            except ValueError:
                pass
            else:
                numlist.append(num)
                print(numlist, sum(numlist), sum(numlist) / len(numlist))
            line = f.readline()

def readline_nested_running_sum(fname: str) -> None:
    numlist: list[float] = []

    with open(fname, 'r') as f:
        line = f.readline()
        while line != '':
            lineparts: list[str] = line.split()
            i: int = 0
            while i < len(lineparts):
                try:
                    num: float = float(lineparts[i])
                except ValueError:
                    pass
                else:
                    numlist.append(num)
                    print(numlist, sum(numlist), sum(numlist) / len(numlist))
                finally:
                    i = i + 1
            line = f.readline()




def main(args: list[str]) -> int:
    # interactive_running_sum()
    # negative_sentinel()
    # empty_string_sentinel()
    # exception_sentinel()
    fname = input('Please enter the name of a file to read from: ')
    # readline_running_sum(fname)
    readline_nested_running_sum(fname)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)