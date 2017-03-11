#!/usr/bin/env python3.5
import pdb             # python debugger module


# Python Debugger (PDB): debugger module
#                       start via pdb.set_trace()
#
# (pdb) help
# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where
#
# Miscellaneous help topics:
# ==========================
# exec  pdb

# starting a python script under pdb:
#       python3 -m pdb palindrone.py
#
#    -m :  run first argument as script and remaining arg passed to that script

# NOTE: below shows that import unittest is the line that will be run next
#       calling the where command shows where in the file it is located.
#
# > /home/map/git/python_beyond_basics/palindrone.py(2)<module>()
# -> import unittest
# (Pdb) where
#   /usr/lib/python3.5/bdb.py(431)run()
# -> exec(cmd, globals, locals)
#   <string>(1)<module>()
# > /home/map/git/python_beyond_basics/palindrone.py(2)<module>()
# -> import unittest
# (Pdb)

# NOTE: next command will move to the next statement
# > /home/map/git/python_beyond_basics/palindrone.py(2)<module>()
# -> import unittest
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(8)<module>()
# -> def digits(x):
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(27)<module>()
# -> def is_palindrome(x):

# NOTICE: that def digits is encountered and next brings up def is_palindrome.
#         However, the debugger did not step into the body of digits,
#         def digits isn't EVALUATED!! Function could only be run when there
#         are arguments passed to it, HENCE FUNCTION BODIES EVALUATED WHEN
#         EXECUTED.

# call cont and enter CTRL-C to break out of infinite loop.

# Running 'cont' or 'step' will restart the program
# (Pdb) cont
# ^C
# Program interrupted. (Use 'cont' to resume).
# --Call--
# > /usr/lib/python3.5/signal.py(45)signal()
# -> @_wraps(_signal.signal)
# (Pdb) next
# > /usr/lib/python3.5/signal.py(47)signal()
# -> handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
# (Pdb) next
# > /usr/lib/python3.5/signal.py(48)signal()
# -> return _int_to_enum(handler, Handlers)
# (Pdb) next
# --Return--
# > /usr/lib/python3.5/signal.py(48)signal()-><bound method...7f75dd22d6a0>>
# -> return _int_to_enum(handler, Handlers)
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(21)digits()
# -> digs.append(mod)
# (Pdb) list
#  16  	    [4, 5, 8, 6, 3, 7, 8]
#  17  	    """
#  18  	    digs = []
#  19  	    while x != 0:
#  20  	        div, mod = divmod(x, 10)
#  21  ->	    digs.append(mod)
#  22  	        x = mod  # THIS IS THE BUG
#  23  	        # x = div
#  24  	    return digs
#  25
#  26
# NOTE: After hitting CTRL-C, a signal wrapper intercepted the interupt.
#       I called next severl more times to get thru several system calls
#       and came to problem area in the code.  Calling 'list', shows the
#       lines of the script

# Call 'return' to try to run to the end of the current function. If it does
# not return, then infinite loop.  Have to hit CTRL-C again to break out
# (Pdb) return
#
# ^CTraceback (most recent call last):
#   File "/usr/lib/python3.5/pdb.py", line 1661, in main
#     pdb._runscript(mainpyfile)
#   File "/usr/lib/python3.5/pdb.py", line 1542, in _runscript
#     self.run(statement)
#   File "/usr/lib/python3.5/bdb.py", line 431, in run
#     exec(cmd, globals, locals)
#   File "<string>", line 1, in <module>
#   File "/home/map/git/python_beyond_basics/palindrone.py", line 2, in <module>
#     import unittest
#   File "/usr/lib/python3.5/unittest/main.py", line 94, in __init__
#     self.runTests()
#   File "/usr/lib/python3.5/unittest/main.py", line 255, in runTests
#     self.result = testRunner.run(self.test)
#   File "/usr/lib/python3.5/unittest/runner.py", line 176, in run
#     test(result)
#   File "/usr/lib/python3.5/unittest/suite.py", line 84, in __call__
#     return self.run(*args, **kwds)
#   File "/usr/lib/python3.5/unittest/suite.py", line 122, in run
#     test(result)
#   File "/usr/lib/python3.5/unittest/suite.py", line 84, in __call__
#     return self.run(*args, **kwds)
#   File "/usr/lib/python3.5/unittest/suite.py", line 122, in run
#     test(result)
#   File "/usr/lib/python3.5/unittest/case.py", line 648, in __call__
#     return self.run(*args, **kwds)
#   File "/usr/lib/python3.5/unittest/case.py", line 600, in run
#     testMethod()
#   File "/home/map/git/python_beyond_basics/palindrone.py", line 52, in test_negative
#     self.assertFalse(is_palindrome(1234))
#   File "/home/map/git/python_beyond_basics/palindrone.py", line 40, in is_palindrome
#     dig = digits(x)
#   File "/home/map/git/python_beyond_basics/palindrone.py", line 19, in digits
#     while x != 0:
#   File "/home/map/git/python_beyond_basics/palindrone.py", line 19, in digits
#     while x != 0:
#   File "/usr/lib/python3.5/bdb.py", line 48, in trace_dispatch
#     return self.dispatch_line(frame)
#   File "/usr/lib/python3.5/bdb.py", line 65, in dispatch_line
#     if self.stop_here(frame) or self.break_here(frame):
#   File "/usr/lib/python3.5/bdb.py", line 148, in break_here
#     filename = self.canonic(frame.f_code.co_filename)
# KeyboardInterrupt
# Uncaught exception. Entering post mortem debugging
# Running 'cont' or 'step' will restart the program
# > /usr/lib/python3.5/bdb.py(148)break_here()
# -> filename = self.canonic(frame.f_code.co_filename)
# (Pdb)
#
# Exit pdb with 'quit' command.

# NOTE: After adding the below code in the method, you can just call the script
#       as: python3 palindrone.py since set_trace() is set.
#
#     import pdb
#     pdb.set_trace()

# Calling 'where' returns the call stack:
#
# map@hexagon:/python_beyond_basics/> python3.5 palindrone.py
# > /home/map/git/python_beyond_basics/palindrone.py(22)digits()
# -> digs = []
# (Pdb) where
#   /home/map/git/python_beyond_basics/palindrone.py(68)<module>()
# -> unittest.main()
#   /usr/lib/python3.5/unittest/main.py(94)__init__()
# -> self.runTests()
#   /usr/lib/python3.5/unittest/main.py(255)runTests()
# -> self.result = testRunner.run(self.test)
#   /usr/lib/python3.5/unittest/runner.py(176)run()
# -> test(result)
#   /usr/lib/python3.5/unittest/suite.py(84)__call__()
# -> return self.run(*args, **kwds)
#   /usr/lib/python3.5/unittest/suite.py(122)run()
# -> test(result)
#   /usr/lib/python3.5/unittest/suite.py(84)__call__()
# -> return self.run(*args, **kwds)
#   /usr/lib/python3.5/unittest/suite.py(122)run()
# -> test(result)
#   /usr/lib/python3.5/unittest/case.py(648)__call__()
# -> return self.run(*args, **kwds)
#   /usr/lib/python3.5/unittest/case.py(600)run()
# -> testMethod()
#   /home/map/git/python_beyond_basics/palindrone.py(56)test_negative()
# -> self.assertFalse(is_palindrome(1234))
#   /home/map/git/python_beyond_basics/palindrone.py(44)is_palindrome()
# -> dig = digits(x)
# > /home/map/git/python_beyond_basics/palindrone.py(22)digits()
# -> digs = []

# NOTE:  Calling print on a variable name will print the value at that point:

# map@hexagon:/python_beyond_basics/> python3.5 palindrone.py
# > /home/map/git/python_beyond_basics/palindrone.py(22)digits()
# -> digs = []
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(23)digits()
# -> while x != 0:
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(24)digits()
# -> div, mod = divmod(x, 10)
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(25)digits()
# -> digs.append(mod)
# (Pdb) print(div)
# 123
# (Pdb) print(x)
# 1234
# (Pdb) print(mod)
# 4
# (Pdb) print(digs)
# []
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(26)digits()
# -> x = mod  # THIS IS THE BUG
# (Pdb) print(x)
# 1234
# (Pdb) print(mod)
# 4
# (Pdb) next
# > /home/map/git/python_beyond_basics/palindrone.py(23)digits()
# -> while x != 0:
# (Pdb) print(x)
# 4
