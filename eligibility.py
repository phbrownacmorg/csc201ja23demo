# Program to do nothing, correctly.

def eligibleHR(age: int, cit: int) -> bool:
    eligible: bool = True
    if age < 25 or cit < 7:
        eligible = False
    return eligible

def eligibleSenate(age: int, cit: int) -> bool:
    eligible: bool = True
    if age < 30 or cit < 9:
        eligible = False
    return eligible

def main(args: list[str]) -> int:
    age: int = int(input("What is the person's age? "))
    cit: int = int(input("How long has this person been a U.S. citizen? "))
    # age >= cit >= 0 for any person

    print('A person age {0} who has been a U.S. citizen for {1} years is'.format(age, cit))

    print('\t- ', end='')
    if not eligibleHR(age, cit):
        print('NOT', end=' ')
    print('eligible to serve in the U.S. House of Representatives, and')

    print('\t- ', end='')
    if not eligibleSenate(age, cit):
        print('NOT', end=' ')
    print('eligible to serve in the U.S. Senate.')

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)