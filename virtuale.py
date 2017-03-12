#!/usr/bin/env python3.5
import venv

#
# https://docs.python.org/3/library/venv.html
#
# virtual environment:  light-weight, self-contained python installation
#       users can create without needing admin rights on system.
#       pyvenv is depcrecated as of python 3.6, new way is
#       python3 -m venv /path/to/new/virtual/environment
#  NOTE: python-virtualenv only works for insalling python 2.x modules
#        modules in a python virutal environment.
#
# mkvirtualenv py3 -p /usr/bin/python3
#
# NOTE 2:
#  pyvenv is python 3.3 stdlib package wrapper script but is depcrecated in 3.6
#  venv in 3.3 stdlib package to improve and replaycc PyPi virutalenv package
#  python-virtualenv meant to be used like python2 -m virtualenv py2
#  virtualenv can be used instead ??

# NOTE: running below creates a 2.7 virutal environment called envtest
#            virtualenv envtest
#
#       next activate the environment via:
#            source envtest/bin/activate
#            (envtest) map@hexagon:/virt/>
#
#      You are now in virutal environment and the python run is from that
#      virutal environment.
