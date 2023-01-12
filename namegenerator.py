# Program to read first names from a CSV file,
# last names from another CSV file, and create a
# third CSV file with names.

def main(args: list[str]) -> int:
    first_names_filename: str = 'first-names.csv'
    last_names_filename: str = 'last-names.csv'
    output_filename: str = 'names.csv'

    first_names: list[str] = []
    first_name_pct: list[float] = []
    last_names: list[str] = []
    last_name_prop100k: list[float] = []

    with open(first_names_filename, 'r') as f:
        for line in f.readlines()[1:]:
            parts: list[str] = line.split(',')
            first_names.append(parts[1])
            first_name_pct.append(float(parts[0]))

    # shove the percentages down one slot
    for i in range(len(first_name_pct)-1):
        first_name_pct[i] = first_name_pct[i+1]
    # delete the unmatched pair at the end
    del first_names[-1]
    del first_name_pct[-1]

    # for i in range(len(first_names)):
    #     print(first_names[i], first_name_pct[i])

    with open(last_names_filename, 'r') as f:
        for line in f.readlines()[1:]:
            parts = line.split(',')
            last_names.append(parts[1])
            last_name_prop100k.append(float(parts[0]))

    # shove the percentages down one slot
    for i in range(len(last_name_prop100k)-1):
        last_name_prop100k[i] = last_name_prop100k[i+1]
    # delete the unmatched pair at the end
    del last_names[-1]
    del last_name_prop100k[-1]

    # for i in range(len(last_names)):
    #     print(i, last_names[i], last_name_prop100k[i])

    n: int = int(input('How many names should be generated?'))

    with open(output_filename, 'w') as f:
        # write the column headers
        f.write('id,firstname,middlename,lastname\n')
        for i in range(n):
            pass



    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)