#!/bin/bash

printf "$1" > ciphertext

openssl enc -a -d -in ./ciphertext -out binarytext

#openssl rsautl -decrypt -in ./binarytext -out plaintext -inkey 4.key
