# Program to do nothing, correctly.

def main(args: list[str]) -> int:
    infilename: str = 'names.csv'
    outfilename: str = 'userids.csv'

    with open(infilename,'r') as infile:
        with open(outfilename, 'w') as outfile:
            # Write header line to outfile
            outfile.write('idnumber,userid,lastname,firstname,middlename\n')

            for line in infile.readlines()[1:]:
                # Split name into its components
                # Pull off the last name
                nameparts: list[str] = line.split(',')
                lastname: str = nameparts[1]
                givennames: list[str] = nameparts[2:]

                # Clean up the last name
                badchars: str = " '.,"  # No biscuit.  This string can be expanded as additional bad characters are encountered.
                for c in badchars:
                    lastname = lastname.replace(c, '')

                id: str = ''
                for name in givennames:
                    id = id + name[0]
                id = (id + lastname).lower() + '001'
                
                outfile.write('{0},{1},{2},{3},{4}\n'.format(nameparts[0], id, nameparts[1], nameparts[2], nameparts[3].strip()))


    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)