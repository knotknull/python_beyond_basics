#!/usr/bin/python3.5
from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        # story_words has list of bytes, decode to str
        # bytes => decode() => str => encode() => bytes ...
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print("story_words = ", story_words)
