import os

zen = open('zen.txt', 'r')

wordlist = zen.readlines()

for i in range(len(wordlist) -1, -1, -2):
    print(wordlist[i], end='')
