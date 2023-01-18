# Program to do nothing, correctly.

def clean(name: str) -> str:
    cleanname: str = ''
    for c in name:
        if (c.isascii() and c.isalpha()) or (c == '-'):
            cleanname = cleanname + c
    return cleanname

def read_names(fname: str) -> list[list[str]]:
    namelist: list[list[str]] = []
    with open(fname,'r') as f:
        for line in f.readlines()[1:]:
            namelist.append(line.split(','))
    return namelist                

def make_userids(names: list[list[str]]) -> list[list[str]]:
    idlist: list[list[str]] = []
    for name in names:
        idnum: str = name[0].strip()
        lastname: str = name[1].strip()
        firstname: str = name[2].strip()
        middlename: str = name[3].strip()
        userid: str = lastname
        if len(middlename) > 0:
            userid = firstname[0] + middlename[0] + userid
        else:
            userid = firstname[0] + lastname
        userid = clean(userid).lower()
        idlist.append([idnum, userid, lastname, firstname, middlename])
    return idlist


def write_id_file(idlist: list[list[str]], fname: str) -> None:
    with open(fname, 'w') as f:
        # Write header line
        f.write('idnumber,userid,lastname,firstname,middlename\n')
        for id in idlist:
            for i in range(4):
                f.write(id[i] + ',')
            f.write(id[4] + '\n')

def main(args: list[str]) -> int:
    infilename: str = 'names.csv'
    outfilename: str = 'userids.csv'

    names: list[list[str]] = read_names(infilename)
    idlist: list[list[str]] = make_userids(names)
    write_id_file(idlist, outfilename)

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)