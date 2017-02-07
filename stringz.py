#!/usr/bin/python3.5

# strings : immutable sequences of Unicode codepoints (?)
sstr = 'single "quote"'
dstr = " double 'quote'"
print (sstr)
print (dstr)

# Multiline strings
tripledq = """ The following multiline string
is delimited by triple quotes.
"""
print (tripledq)
triplesq = ''' The following multiline string
is delimited by triple quotes.
'''
print(triplesq)

# Note: Python 3 has Universal newline support that translates
#       newline character for that platform on input / output.
#       See PEP 278
escaper = "Various esapes:  tab => \t  newline => \n  sqt => \'  dqt => \" "
print(escaper)
