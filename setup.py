#!/usr/bin/env python3.6
from distutils.core import setup
#
# distutils: module that allows you to write a python script that will
#            your python module into any installation.
#
#   ex. from distutils.core import setup
#   NOTE: script name by convention is setup.py

setup(
    name='palindrone',      # name of module
    version='1.0b',         # version of module
    py_modules=['palindrone'],  # modules to install, module names withou .py

    # metadata
    author='Me',
    author_email='me@mimi.com',
    description='a module to file palidrom(n)e type numbers',
    license='Free',
    keywords='palidrome'

)


# NOTE: created new virtualenv via:
#            virtualenv -p python3.6 venv
#
# map@hexagon:/venv/> ls -ltr
# total 12
# drwxr-xr-x 3 map map 4096 Mar 15 22:32 lib
# -rw-r--r-- 1 map map   60 Mar 15 22:32 pip-selfcheck.json
# drwxr-xr-x 2 map map 4096 Mar 15 22:32 bin
#
#
# Now run setup.py in virtualenv:
#  python setup.py install
# (venv) map@hexagon:/palindrome/> python setup.py install
# running install
# running build
# running build_py
# creating build
# creating build/lib
# copying palindrone.py -> build/lib
# running install_lib
# copying build/lib/palindrone.py -> /home/map/python/setup/palindrome/venv/lib/python3.6/site-packages
# byte-compiling /home/map/python/setup/palindrome/venv/lib/python3.6/site-packages/palindrone.py to palindrone.cpython-36.pyc
# running install_egg_info
# Writing
# /home/map/python/setup/palindrome/venv/lib/python3.6/site-packages/palindrone-1.0b.egg-info
#
#  NOTE: 3rd party packages are usually installed in site-packages directory

# Next, load palindrone from REPL but first cd ..
# (venv) map@hexagon:/palindrome/> cd ..
# (venv) map@hexagon:/setup/> ls -l
# total 4
# drwxr-xr-x 4 map map 4096 Mar 15 22:45 palindrome
# (venv) map@hexagon:/setup/> python
# Python 3.6.0 (default, Jan 13 2017, 00:00:00)
# [GCC 4.8.4] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import palindrone
# >>> palindrone.__file__
# '/home/map/python/setup/palindrome/venv/lib/python3.6/site-packages/palindrone.py'
# >>>

# Create different types of distribution formats:
#      python setup.py sdist - -format zip      # sdist = source distribution
# (venv) map@hexagon:/palindrome/> python setup.py sdist --format zip
# running sdist
# running check
# warning: check: missing required meta-data: url
#
# warning: sdist: manifest template 'MANIFEST.in' does not exist (using default file list)
#
# warning: sdist: standard file not found: should have one of README, README.txt
#
# writing manifest file 'MANIFEST'
# creating palindrone-1.0b
# making hard links in palindrone-1.0b...
# hard linking palindrone.py -> palindrone-1.0b
# hard linking setup.py -> palindrone-1.0b
# creating dist
# creating 'dist/palindrone-1.0b.zip' and adding 'palindrone-1.0b' to it
# adding 'palindrone-1.0b/palindrone.py'
# adding 'palindrone-1.0b/setup.py'
# adding 'palindrone-1.0b/PKG-INFO'
# removing 'palindrone-1.0b' (and everything under it)
# (venv) map@hexagon:/palindrome/> ls -ltr
# total 24
# -rw-r--r-- 1 map map 1567 Mar 15 22:20 palindrone.py
# drwxr-xr-x 4 map map 4096 Mar 15 22:40 venv
# -rw-r--r-- 1 map map  969 Mar 15 22:44 setup.py
# drwxr-xr-x 3 map map 4096 Mar 15 22:45 build
# -rw-r--r-- 1 map map   66 Mar 15 22:53 MANIFEST
# drwxr-xr-x 2 map map 4096 Mar 15 22:53 dist
# (venv) map@hexagon:/palindrome/> cd dist
# (venv) map@hexagon:/dist/> ls -ltr
# total 4
# -rw-r--r-- 1 map map 1761 Mar 15 22:53 palindrone-1.0b.zip
# (venv) map@hexagon:/dist/> unzip -lv palindrone-1.0b.zip
# Archive:  palindrone-1.0b.zip
#  Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
# --------  ------  ------- ---- ---------- ----- --------  ----
#     1567  Defl:N      701  55% 2017-03-15 22:20 05473c3d  palindrone-1.0b/palindrone.py
#      969  Defl:N      488  50% 2017-03-15 22:44 36031345  palindrone-1.0b/setup.py
#      234  Defl:N      168  28% 2017-03-15 22:53 413ee6a0  palindrone-1.0b/PKG-INFO
# --------          -------  ---                            -------
#     2770             1357  51%                            3 files
#
# NOTE: the zip file contains the source (palindrone.py) and setup.py

# NOTE: To see other sdist formats use python setup.py sdist --help-formats
# (venv) map@hexagon:/palindrome/> python setup.py sdist --help-formats
# List of available source distribution formats:
#   --formats=bztar  bzip2'ed tar-file
#   --formats=gztar  gzip'ed tar-file
#   --formats=tar    uncompressed tar file
#   --formats=xztar  xz'ed tar-file
#   --formats=zip    ZIP file
#   --formats=ztar   compressed tar file
#
# python setup.py --help
# (venv) map@hexagon:/palindrome/> python setup.py --help
# Common commands: (see '--help-commands' for more)
#
#   setup.py build      will build the package underneath 'build/'
#   setup.py install    will install the package
#
# Global options:
#   --verbose (-v)      run verbosely (default)
#   --quiet (-q)        run quietly (turns verbosity off)
#   --dry-run (-n)      don't actually do anything
#   --help (-h)         show detailed help message
#   --no-user-cfg       ignore pydistutils.cfg in your home directory
#   --command-packages  list of packages that provide distutils commands
#
# Information display options (just display information, ignore any commands)
#   --help-commands     list all available commands
#   --name              print package name
#   --version (-V)      print package version
#   --fullname          print <package name>-<version>
#   --author            print the author's name
#   --author-email      print the author's email address
#   --maintainer        print the maintainer's name
#   --maintainer-email  print the maintainer's email address
#   --contact           print the maintainer's name if known, else the author's
#   --contact-email     print the maintainer's email address if known, else the
#                      author's
#   --url               print the URL for this package
#   --license           print the license of the package
#   --licence           alias for --license
#   --description       print the package description
#   --long-description  print the long package description
#   --platforms         print the list of platforms
#   --classifiers       print the list of classifiers
#   --keywords          print the list of keywords
#   --provides          print the list of packages/modules provided
#   --requires          print the list of packages/modules required
#   --obsoletes         print the list of packages/modules made obsolete
#
# usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
#    or: setup.py --help [cmd1 cmd2 ...]
#    or: setup.py --help-commands
#    or: setup.py cmd --help
