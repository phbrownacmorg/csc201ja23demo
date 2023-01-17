# Program to print the lyrics to "Old MacDonald".

def printVerse(animal: str, sound: str) -> None:
    print('Old MacDonald had a farm, e-i-e-i-o!')
    print('And on that farm he had some {0}, e-i-e-i-o!'.format(animal))
    print('With a {0}, {0} here and a {0}, {0} there,'.format(sound))
    print('Here a {0}, there a {0}, everywhere a {0}, {0},'.format(sound))
    print('Old MacDonald had a farm, e-i-e-i-o!')
    print()

def main(args: list[str]) -> int:
    printVerse('cows', 'moo')
    printVerse('hens', 'cluck')
    printVerse('pigs', 'oink') # Apparently from New Jersey; article should be 'an'
    printVerse('dogs', 'woof')
    printVerse('horses', 'neigh')    


    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)