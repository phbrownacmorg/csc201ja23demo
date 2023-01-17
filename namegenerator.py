# Program to read first names from a CSV file,
# last names from another CSV file, and create a
# third CSV file with names.

import random

def read_file(fname: str) -> tuple[list[str], list[float]]:
    names: list[str] = []
    probs: list[float] = []
    with open(fname, 'r') as f:
        for line in f.readlines()[1:]:
            parts: list[str] = line.split(',')
            names.append(parts[1])
            probs.append(float(parts[0]))
    return names, probs

def read_names(fname: str) -> tuple[list[str], list[float]]:
    names, probs = read_file(fname)

    # pull the probabilities forward one slot
    for i in range(len(probs) - 1):
        probs[i] = probs[i+1]
    # delete the unmatched pair at the end
    del names[-1]
    del probs[-1]

    return names, probs

def pick_name(names: list[str], probs: list[float]) -> str:
    p: float = random.random() * probs[-1]
    i = 0
    while probs[i] < p:
        i = i + 1
    return names[i].capitalize()

def make_names(n: int, first_names: list[str], first_name_pct: list[float],
                    last_names: list[str], last_name_prop100k: list[float]) \
                        -> list[tuple[str, str, str]]:
    namelist: list[tuple[str, str, str]] = []
    for i in range(n):
        firstname: str = pick_name(first_names, first_name_pct)
        middlename: str = pick_name(first_names, first_name_pct)
        lastname: str = pick_name(last_names, last_name_prop100k)
        namelist.append((lastname, firstname, middlename))
    return namelist

def write_names(names: list[tuple[str, str, str]], fname: str) -> None:
    with open(fname, 'w') as f:
        # Write the header row
        f.write('id,lastname,firstname,middlename\n')
        # Write the names
        for i in range(len(names)):
            f.write(str(i))
            for j in range(3):
                f.write(',' + names[i][j])
            f.write('\n')

def main(args: list[str]) -> int:
    first_names_filename: str = 'first-names.csv'
    last_names_filename: str = 'last-names.csv'
    output_filename: str = 'names.csv'

    first_names, first_name_pct = read_names(first_names_filename)
    last_names, last_name_prop100k = read_names(last_names_filename)

    n: int = int(input('How many names should be generated? '))

    names: list[tuple[str, str, str]] = make_names(n, first_names, first_name_pct,
                                                    last_names, last_name_prop100k)
    write_names(names, output_filename)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)