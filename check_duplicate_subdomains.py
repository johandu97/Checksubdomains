#!/usr/bin/env python

import sys
from termcolor import colored

def main():

    if len(sys.argv) < 3:
        print ('Program argument must be 3')
        sys.exit()

    f1 = open(sys.argv[1], 'r')
    f2 = open(sys.argv[2], 'r')

    text1 = f1.readlines()
    text2 = f2.readlines()

    count = 0

    for _text1 in text1:
        if _text1 in text2:
            count += 1
        else:
            print colored(_text1, 'red')
            
    print count



if __name__ == '__main__':
    main()
