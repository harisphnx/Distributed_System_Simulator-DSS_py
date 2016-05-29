import multiprocessing
import time
import sys
# for compatibility with Python 2.7 and 3
try:
    from Queue import Empty, Full
except ImportError:
    from queue import Empty, Full
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

# This is the file which contains your user-defined functions (to be given to
# the machines for execution)
from functions import *
