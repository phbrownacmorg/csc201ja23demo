# Program to represent a phone book as a dictionary.  The key of each
# entry is the person's name; the value is the phone number.  (The value
# *could*, of course, be an entire dictionary with the person's address,
# nickname, several phone numbers, birthday, and anything else relevant,
# just like an entry in a contacts list.  But for now, we'll stick to
# the value being just the phone number.)

from datetime import date
from typing import Any, cast

def parse_user(values: list[str], fieldnames: list[str]) -> dict[str, Any]:
    userdict: dict[str, Any] = {}
    for i in range(len(fieldnames)):
        field: str = fieldnames[i]
        val: str = values[i].strip()
        # Handle a couple of fields specially
        # accesses is an int, default 0
        if field == 'accesses':
            if val == '':
                userdict['accesses'] = 0
            else:
                userdict['accesses'] = int(val)
        elif fieldnames[i] == 'lastchanged':
            userdict[field] = date.fromisoformat(val)
        # Everything else is just a string
        else:
            userdict[field] = val

    return userdict

def read_phonebook(fname: str) -> dict[str, Any]:
    phonebook: dict[str, Any] = {}
    with open(fname, 'r') as f:
        lines: list[str] = f.readlines()
        # Read the fields
        fields: list[str] = lines[0].strip().split(',')
        # read the entries
        for line in lines[1:]:
            parts = line.strip().split(',')
            userdict: dict[str, Any] = parse_user(parts, fields)
            phonebook[userdict['name']] = userdict

    return phonebook

def print_entry(phonebook: dict[str, Any], name: str) -> None:
    try:
        entry: dict[str, Any] = phonebook[name]
        # Increase the access count
        entry['accesses'] = entry['accesses'] + 1
    except KeyError:
            print('The phonebook has no entry for ' + name)
    else:
        print('Entry for {0}:'.format(name))
        for field in entry.keys():
            print('\t{0:11}\t{1}'.format(field + ':', entry.get(field, '')))

def entry_phone(entry: tuple[str, dict[str, Any]]) -> str:
    return cast(str, entry[1]['phone']) # Phone number

def entry_last_name(entry: tuple[str, dict[str, Any]]) -> str:
    name: str = entry[0]
    # Extract last name
    parts: list[str] = name.split()
    return parts[-1]

def sort_and_print(phonebook: dict[str, dict[str, Any]]) -> None:
    entries: list[tuple[str, dict[str, Any]]] = list(phonebook.items())
    entries.sort(key=entry_last_name, reverse=True) # Only time you refer to a function without parentheses
    for entry in entries:
        print_entry(phonebook, entry[0])

def main(args: list[str]) -> int:
    phonebook: dict[str, dict[str, Any]] = read_phonebook('phonebook.csv')
    #print(phonebook)

    name: str = input('Please enter a name to look up, or hit Enter to quit: ')
    while name != '':
        print_entry(phonebook, name)
        name = input('Please enter a name to look up, or hit Enter to quit: ')

    sort_and_print(phonebook)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)