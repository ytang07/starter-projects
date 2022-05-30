# imports
import os # good 
from os import dup # good 
from os.path import dirname # good
from os import * # BAD

# whitespace and indentation
def function():
    # ... (this doesn't compile)
    pass # placeholder code that does compile

# single line comment
'''
multiline comment
'''
"""
also a multiline comment
"""

abc0 = [0, 1, 2]
abc1 = range(3)
abc2 = [_ for _ in range(3)]

xyz = "abc{x}".format(x=abc0)
print(xyz)
print(f"abc{abc0}") # Python 3
# print "abc" # Python 2
