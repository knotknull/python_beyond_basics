#!/usr/bin/env python3.6
import urllib
import urllib.request

# a package can contain a module or other packages with other modules
# NOTE: Here urllib.request resides in urllib, hence urllib.request is a module
# and urllib is a package

# NOTE: both types come up as module
#
print("{}".format(type(urllib)))
print("{}".format(type(urllib.request)))

# Packages are generally directories
print("{}".format(urllib.__path__))

# Modules are generally files
# BTW, this won't work
print("{}".format(urllib.request.__path__))
