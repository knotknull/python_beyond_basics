#!/usr/bin/python3.5
from pprint import pprint as pp
import sys

# How to open a file:
# open():
#      file: path to file (required)
#      mode: read / write / append, binary / text
#      encoding: text encoding
#
#  NOTE: files opened as binary are read as bytes objects (raw data)
#        files opened as text are read as text strings of str
#        [text utilizes encoding and universal newlines]
print ("encoding = {}".format(sys.getdefaultencoding()))

# Python encoding standards
# http://docs.python.org/3/library/codecs.html#standard-encodings

# Let's write a file:
#   Modes:
#       'r'     open for reading (default)
#       'w'     open for writing, truncating the file first
#       'x'     open for exclusive creation, fail if the file already exists
#       'a'     open for writing, appending to the end of the file if it exists
#       'b'     binary mode
#       't'     text mode(default)
#       '+'     open a disk file for updating (reading and writing)
#       'U'     universal newlines mode (for backwards compatability, should
#               not be used in new code)


def writecnt(xcnt):
    print("write count: {}".format(xcnt))

f = open('/tmp/write_test.txt', mode="wt", encoding='utf-8')
print("type(f) = {}".format(type(f)))   # type is _io.TextIOWrapper

# f.write() returns the number of codepoints written and not bytes
# for example: a newline is counted as 1 codepoint but two bytes for \r\n vs \n
writecnt(f.write("What light "))
writecnt(f.write("through yonder window \n"))
writecnt(f.write(" ... breaks wind "))
f.close()

# Let's read the file this time mode=rt == read text
rdr = open('/tmp/write_test.txt', mode="rt", encoding='utf-8')
# f.read() returns str because file was opened in text mode
# read 11 characters
print(rdr.read(11))
# read the rest of the file
print(rdr.read())

# read at end of the file returns empty string
print(rdr.read())

# move file pointer to beginning of file
rdr.seek(0)

# read a line at a time, terminated w/ newline
print(rdr.readline())
print(rdr.readline())
print(rdr.readline())

# move file pointer to beginning of file
rdr.seek(0)
# read all lines of a file into a list (reads entire thing into memory)
print(rdr.readlines())

rdr.close()

# Now let's append to the same file
# mode=at == append text
app = open('/tmp/write_test.txt', mode="at", encoding='utf-8')

# call writelines: writes iterable series of strings to a stream
#  NOTE: MUST PROVIDE newlines
app.writelines(
    ['\nThat all\n',
     'Folks!!!\n',
     ])
app.close()
