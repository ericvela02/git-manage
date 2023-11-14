import sys
from core.args_parser import *
from core.terminal_input import *

def main():
    args = parse_args(sys.argv[1:])

    print(args)

    if not args.directory and not args.drive and confirm_full_search():
        print('Searching through all drives...')
    elif not args.drive:
        if (validate_directory(args.directory)):
            print('Searching through directory...')
        else:
            print('The provided directory does not exist.')
            sys.exit(1)
    elif not args.directory:
        if (validate_drive(args.drive)):
            print('Searching through drive...')
        else:
            print('The provided drive does not exist.')
            sys.exit(1)
    else:
        if (validate_dir_in_drive(args.drive, args.directory)):
            print('Searching through directory in drive...')
        else:
            print('The provided directory in drive does not exist.')
            sys.exit(1)

if __name__ == '__main__':
    main()