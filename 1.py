#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib

mystring = raw_input("Give a string to hash:")

def main():
    rolo = rololo = ''
    rolo = hashlib.sha256(mystring).hexdigest()
    rololo = hashlib.md5(rolo).hexdigest()
    print 'md5 hex digest of the sha256 hex digest of the \'', mystring, '\' string is: ', rololo

if __name__ == '__main__':
    main()
