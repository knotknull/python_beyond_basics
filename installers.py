#!/usr/bin/env python3.6

#
#
# Installing 3rd party packages: distutils, easy_install, pip
#
#   distutils:  same as python setup.py install

# easy_install / pip :
#       - search for packages in central repo: Python Package Index (PyPI)
#       - download and install along with dependencies
#       - pypi.python.org/pypi
#
# NOTE: you can use easy_install to install pip (how meta)
#
#    Install easy_install:
#    1. go to virtualenv
#    2. cd palindrome;  source venv/bin/activate
#    3. Download ez_setup.py: wget https://bootstrap.pypa.io/ez_setup.py
#    4. Install  ez_setup.py: python ez_setup.py
#    5. Install 3rd party software:   ez_install <package_name>
#
# OR
#
#  sudo python3.6 ez_setup.py
#  sudo easy_install-3.6 pip
#
# pip install <package_name>
#
# sudo pip3.6 install nose
#
# map@hexagon:/palindrome/> python3.6
# Python 3.6.0 (default, Jan 13 2017, 00:00:00)
# [GCC 4.8.4] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import nose
# >>> nose.__file__
# '/usr/local/lib/python3.6/dist-packages/nose/__init__.py'
