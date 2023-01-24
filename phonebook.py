# Program to represent a phone book as a dictionary.  The key of each
# entry is the person's name; the value is the phone number.  (The value
# *could*, of course, be an entire dictionary with the person's address,
# nickname, several phone numbers, birthday, and anything else relevant,
# just like an entry in a contacts list.  But for now, we'll stick to
# the value being just the phone number.)

def read_phonebook(fname: str) -> dict[str, str]:
    phonebook: dict[str, str] = {}
    with open(fname, 'r') as f:
        for line in f.readlines()[1:]:
            parts: list[str] = line.split(',')
            name: str = parts[0].strip()
            number: str = parts[1].strip()
            phonebook[name] = number

    return phonebook

def main(args: list[str]) -> int:
    phonebook: dict[str, str] = read_phonebook('phonebook.csv')
    #print(phonebook)

    name: str = input('Please enter a name to look up, or hit Enter to quit: ')
    while name != '':
        try:
            number: str = phonebook[name]
            print('The number for {0} is {1}.'.format(name, number))
        except KeyError:
            print('The phonebook has no number for ' + name)
        name = input('Please enter a name to look up, or hit Enter to quit: ')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)