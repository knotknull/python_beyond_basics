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
escaper = "Various esapes:  backslash => \\ tab => \t  newline => \n  "
escaper = escaper + "            :  sqt => \'        dqt => \" "
escaper = escaper + "            :  bell => \a       backspace => \b "
escaper = escaper + "            :  formfeed => \f   linefeed => \n "
escaper = escaper + "            :  crgrtn=> \r      horiz tab => \t "
escaper = escaper + "            :  vert tab=> \v      "
# \ooo       character octal value
# \xhh       character hex value
# \N{name}   character named name in Unicode database
# \uxxxx     character with 16-bit hex value xxxx
# \uxxxxxxxx character with 32-bit hex value xxxxxxxx
print(escaper)

raw_str = r'String where \n escapes are \t  not interpreted \r'
print(raw_str)

# get an index of a String
print(raw_str[5])

# call method on String object
nwk = "newark"
print(nwk.capitalize())

uni_code = 'Vi er s\u00e5 glad for \u00e5 h\u00f8re og l\u00e6re om Python!'
print(uni_code)
