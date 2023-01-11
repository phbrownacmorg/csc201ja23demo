# Program to do nothing, correctly.

def main(args: list[str]) -> int:

    string1: str = 'The dog '
    string2: str = 'ran.'
    string3: str = string1 + string2
    # Concatenation
    print(string3)

    # Repetition.  Either side, and the integer is any integer expression.
    print(5 * string2)
    print(string2 * (3 + 2))

    print(len(string1), len(string2), len(string1 + string2))
    print()
    
    # Iterate over the string by character
    i = 0
    for c in (string3):
        print(i, c, i - len(string3))
        i = i+1

    print()
    # Iterate over a string by index
    for i in range(len(string1)):
        print(i, string1[i], i - len(string1), string1[i - len(string1)])

    print()
    phone: str = '800-867-5309'
    areacode: str = phone[:3]
    exchange: str = phone[4:7]
    number: str = phone[-4:]
    print(phone, areacode, exchange, number)

    # Methods
    print(string3.split())
    print(phone.split('-'))

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)