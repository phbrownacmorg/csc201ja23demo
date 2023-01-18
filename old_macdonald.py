# Program to print the lyrics to "Old MacDonald".

def article(word: str) -> str:
    result: str = 'a'
    if word[0].lower() in 'aeiou':
        result = 'an'
    return result

def printVerse(animal: str, sound: str) -> None:
    print('Old MacDonald had a farm, e-i-e-i-o!')
    print('And on that farm he had some {0}, e-i-e-i-o!'.format(animal))
    print('With {1} {0}, {0} here and {1} {0}, {0} there,'.format(sound, article(sound)))
    print('Here {1} {0}, there {1} {0}, everywhere {1} {0}, {0},'.format(sound, article(sound)))
    print('Old MacDonald had a farm, e-i-e-i-o!')
    print()

def main(args: list[str]) -> int:
    printVerse('cows', 'moo')
    printVerse('hens', 'cluck')
    printVerse('pigs', 'oink') # Apparently from New Jersey; article should be 'an'
    printVerse('dogs', 'arf')
    printVerse('horses', 'neigh')    


    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)