# Program to do nothing, correctly.

def main(args: list[str]) -> int:
    # Range() with one argument: range(stop)
    # From 0 up to, but not including, stop
    stop: int = 8
    print('range(' + str(stop) + ') =>', list(range(stop)))
    stop = 27
    print('range(' + str(stop) + ') =>', list(range(stop)))
    # If stop <= 0, returns no values
    stop = -1
    print('range(' + str(stop) + ') =>', list(range(stop)))

    # range() with two arguments: range(start, stop)
    # From start up to, but not including, stop
    stop = 8
    start: int = 4
    print('range(' + str(start) + ',' + str(stop) + ') =>', list(range(start, stop)))
    start = 12
    # if start > stop, returns no values
    print('range(' + str(start) + ',' + str(stop) + ') =>', list(range(start, stop)))
    stop = 27
    print('range(' + str(start) + ',' + str(stop) + ') =>', list(range(start, stop)))

    # range() with three arguments: range(start, stop, step)
    step = 2
    print('range(' + str(start) + ',' + str(stop) + ',' + str(step) +') =>',
         list(range(start, stop, step)))
    start = 4
    stop = 8
    print('range(' + str(start) + ',' + str(stop) + ',' + str(step) +') =>',
         list(range(start, stop, step)))
    start = 12
    step = -1
    print('range(' + str(start) + ',' + str(stop) + ',' + str(step) +') =>',
         list(range(start, stop, step)))
    step = -3
    print('range(' + str(start) + ',' + str(stop) + ',' + str(step) +') =>',
         list(range(start, stop, step)))
    stop = 27
    step = 5
    print('range(' + str(start) + ',' + str(stop) + ',' + str(step) +') =>',
         list(range(start, stop, step)))
    start = -28
    print('range(' + str(start) + ',' + str(stop) + ',' + str(step) +') =>',
         list(range(start, stop, step)))
    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)