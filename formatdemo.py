# Program to do nothing, correctly.

def main(args: list[str]) -> int:
    # Format a phone number
    phone: str = '864-867-5309'
    print('({0}) {1}-{2}'.format(phone[:3], phone[4:7], phone[-4:]))
    print('1-{0}-{1}-{2}'.format(phone[:3], phone[4:7], phone[-4:]))
    print('+1 {0}-{1}-{2}'.format(phone[:3], phone[4:7], phone[-4:]))
    print('{0}-{1}-{2}'.format(phone[:3], phone[4:7], phone[-4:]))
    print('{0}.{1}.{2}'.format(phone[:3], phone[4:7], phone[-4:]))

    print()
    ssn: str = '123456789'
    print('SSN: {0}-{1}-{2}'.format(ssn[:3], ssn[3:5], ssn[-4:]))

    print()
    month: int = 1
    day: int = 11
    year: int = 2023
    print('US numeric: {1}/{0}/{2}'.format(day, month, year))
    print('US numeric, short year: {1}/{0}/{2}'.format(day, month, year % 100))
    print('UK numeric: {0}/{1}/{2}'.format(day, month, year))
    print('UK numeric, short year: {0}/{1}/{2}'.format(day, month, year % 100))
    print('European numeric: {0}.{1}.{2}'.format(day, month, year))
    print('European numeric, leading zeroes: {0:02d}.{1:02d}.{2}'.format(day, month, year))
    print('European numeric, short year: {0}.{1}.{2}'.format(day, month, year % 100))
    print('ISO 8601: {2}-{1:02d}-{0:02d}'.format(day, month, year))

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)