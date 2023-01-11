# Program to do nothing, correctly.

def main(args: list[str]) -> int:

    # Read name
    name: str = input('Please enter your name in "last, first middle" format: ')
    print(name)

    # Split name into its components
    # Pull off the last name
    nameparts: list[str] = name.split(',')
    print(nameparts)

    lastname: str = nameparts[0]
    givennames: list[str] = nameparts[1].split()
    print(lastname, givennames)

    # Clean up the last name
    badchars: str = " '.,"  # No biscuit.  This string can be expanded as additional bad characters are encountered.
    for c in badchars:
        lastname = lastname.replace(c, '')

    id: str = ''
    for name in givennames:
        id = id + name[0]
    id = (id + lastname).lower() + '001'
    print(id)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)