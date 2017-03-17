#!/usr/bin/python2.7

import difflib
import sys

if __name__ == '__main__':
    print 'XYZ DIFFER.'
    if sys.argv[4] != sys.argv[7]:
        print 'File permissions differ.'
    file1 = ''
    file2 = ''
    with open(sys.argv[2], 'r') as fd:
        file1 = fd.readlines()
    with open(sys.argv[5], 'r') as fd:
        file2 = fd.readlines()
    diff = difflib.unified_diff(file1, file2)
    diff_string = ''.join(diff)
    if diff_string:
        print diff_string
    else:
        print 'Files are identical.'
