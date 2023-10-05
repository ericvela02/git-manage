import argparse

def validate_directory(directory):

    return 0

def validate_drive(drive):

    return 0

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Manage git repositories in your system.')

    parser.add_argument('-d', '--directory',
                        help='Specify a directory to search for repositories.',
                        type=str)
    
    parser.add_argument('-D', '--drive',
                        help='Specify a drive to search for repositories.',
                        type=str)
    
    return parser.parse_args(args)
