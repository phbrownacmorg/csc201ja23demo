# Program to do nothing, correctly.

def validSSN(ssn: str) -> bool:
    valid: bool = True
    # 9 digits, maybe two hyphens
    # Handle the hyphens first.  They can then be gotten rid of.
    if len(ssn) == 11: # hyphens
        # If hyphens, they're in positions 3 and 6
        if ssn[3] != '-' or ssn[6] != '-':
            valid = False
        else:
            ssn = ssn.replace('-', '') # Get rid of the hyphens

    # At this point, should be a string of exactly 9 digits
    if (len(ssn) != 9) or (not ssn.isascii()) or (not ssn.isdigit()):
        valid = False
    # area number (first three digits) can't be 000, 666, or 900-999
    elif ssn[:3] == '000' or ssn[:3] == '666' or ssn[0] == '9':
        valid = False
    # group number (fourth and fifth digits) can't be 00
    elif ssn[3:5] == '00':
        valid = False
    # serial number (last four digits) can't be 0000
    elif ssn[-4:] == '0000':
        valid = False

    return valid

def main(args: list[str]) -> int:
    ssn: str = input('Please enter a Social Security number, with or without hyphens: ')
    print(ssn, 'is', end = ' ')

    if not validSSN(ssn):
        print('NOT', end=' ')
    
    print('a valid SSN.')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)