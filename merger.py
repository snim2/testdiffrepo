#!/usr/bin/python2.7

import sys

def print_nth_line(lines, n):
    if n >= len(lines):
        print ''
    else:
        print lines[n]


if __name__ == '__main__':
    print 'XYZ MERGER TOOL, marker size: %d.' % int(sys.argv[4])
    with open(sys.argv[1], 'r') as fd:
        file_ancestor = fd.read().split('\n')
    with open(sys.argv[2], 'r') as fd:
        file_current = fd.read().split('\n')
    with open(sys.argv[3], 'r') as fd:
        file_other = fd.read().split('\n')
    merged_lines = list()
    for lineno in xrange(max(len(file_ancestor), len(file_current), len(file_other)) - 1):
        print 'Select (1), (2) or (3):'
        print '(1)',
        print_nth_line(file_ancestor, lineno)
        print '(2)',
        print_nth_line(file_current, lineno)
        print '(3)',
        print_nth_line(file_other, lineno)
        selection = None
        while True:
            try:
                selection = int(raw_input('> '))
                if selection < 1 or selection > 3:
                    continue
                else:
                    if selection == 1:
                        merged_lines.append(file_ancestor[lineno])
                    elif selection == 2:
                        merged_lines.append(file_current[lineno])
                    elif selection == 3:
                        merged_lines.append(file_other[lineno])
                    break
            except ValueError:
                continue
        with open(sys.argv[2], 'w') as fd:
            fd.write('\n'.join(merged_lines))
