#!/usr/bin/python
# -*- coding: utf-8 -*-
# from bitcoin public key to uncompressed address
# as per https://en.bitcoin.it/w/images/en/9/9b/PubKeyToAddr.png
# we want: 


import hashlib


shasha = hashlib.sha256("94176137926187438630526725483965175646602324181311814940191841477114099191175").hexdigest()
rmd = hashlib.new('ripemd160') # import from OpenSSL
