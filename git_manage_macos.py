import sys
from core.args_parser import parse_args

def main():
    args = parse_args(sys.argv[1:])
    print(args)

if __name__ == '__main__':
    main()