# Program to do nothing, correctly.
from typing import cast

def readlist() -> list[float]:
    # Read a list of numbers
    return cast(list[float], eval(input('Please enter a list of numbers: ')))

def find_sum_avg(number_list: list[float]) -> tuple[float, float]:
    # Accumulator variable #1
    listsum: float = 0
    # Accumulator variable #2
    listsize: int = 0
    # Loop
    for n in number_list:
        # Accumulate the answer into the accumulator variable #1
        listsum = listsum + n
        # Accumulate the length of the list into accumlator variable #2
        listsize = listsize + 1

    return listsum, listsum / listsize

def main(args: list[str]) -> int:
    # Read a list of numbers
    numlist: list[float] = readlist()
    # Test it
    print('The list is', numlist)

    listsum, listavg = find_sum_avg(numlist)

    # Print the answers
    print('The sum of this list is', listsum)
    print('The average of this list is', listavg)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)