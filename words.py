#!/usr/bin/env python3.5
import sys
from urllib.request import urlopen
# Module docstrings
""" Retrieve and print out words from a URL

    Usage: python3 words.py <URL>
"""


# create a function
def get_words(url):
    # was with urlopen('http://sixty-north.com/c/t.txt') as story:
    # Add docstrings via """. Below is Google Python Style Guide
    # can be accessed via help(get_words)
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containting the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            # story_words has list of bytes, decode to str
            # bytes => decode() => str => encode() => bytes ...
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print all items passed in from a collection.

    Args:
        items: A collection of items.
    """
    for item in items:
        print(item)  # NOTE: implicit return or return only returns None


def main(url):
    """ Print Each word for a text document at a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    # was with urlopen('http://sixty-north.com/c/t.txt') as story:
    words = get_words(url)
    print_items(words)

# see how we are called: when imported with becomes modules name,
# i.e. __name__ == words when run as a script __name__ ==  __main__
# print(__name__)
# for argument parsing look at: argparse or 3rd party docopt
if __name__ == '__main__':
    if len(sys.argv) == 1:
        arg1 = "http://sixty-north.com/c/t.txt"
    else:
        arg1 = sys.argv[1]
    main(arg1)   # use argv[1] for paramter, argv[0] is the filename
