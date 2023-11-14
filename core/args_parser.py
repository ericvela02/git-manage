import argparse
from core.common_directories import COMMON
import os

def validate_directory(directory):

    if directory == '.': # Current directory
        return True
    
    if directory == '..': # Parent directory
        return True
    
    if directory == '~': # Home directory
        return True
    
    if directory.lower() in COMMON.keys(): # Common directory
        return True

    if os.path.isdir(directory):
        return True
    
    return False

def validate_drive(drive):

    drive.strip()

    if len(drive) > 1:
        if drive[1] == ":":
            drive = drive[0].upper() + ":\\"
        else:
            drive = drive[0].upper() + drive[1:].replace('/', '\\')
    else:
        drive = drive.upper() + ':\\'

    print(drive)

    if os.path.isdir(drive):
        return True
    
    return False

def validate_dir_in_drive(drive, directory):
    
    if os.path.isdir(os.path.join(drive, directory)):
        return True
    
    return False
    

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Manage git repositories in your system.')

    parser.add_argument('-d', '--directory',
                        help='Specify a directory to search for repositories.',
                        type=str)
    
    parser.add_argument('-D', '--drive',
                        help='Specify a drive to search for repositories.',
                        type=str)
    
    parser.add_argument('-p', '--path', 
                        help='Specify a path to search for repositories.',
                        type=str)
    
    return parser.parse_args(args)
