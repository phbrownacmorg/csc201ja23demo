# Program to do nothing, correctly.

def main(args: list[str]) -> int:
    # Read a list of numbers
    numlist: list[float] = eval(input('Please enter a list of numbers: '))
    # Test it
    print('The list is', numlist)

    # Accumulator variable #1
    listsum: float = 0
    # Accumulator variable #2
    listsize: int = 0
    # Loop
    for n in numlist:
        # Accumulate the answer into the accumulator variable #1
        listsum = listsum + n
        # Accumulate the length of the list into accumlator variable #2
        listsize = listsize + 1

    # Print the answers
    print('The sum of this list is', listsum)
    print('The average of this list is', (listsum/listsize))

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)