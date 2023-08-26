#optimize function
from pprint import pprint
def first():
  return 1
def second():
  return 2
def third():
  return 3
def defualt():
  return 0
number: int = 1
variables : dict = {1:first, 2: second, 3: third }
test_return = variables.get(number, defualt)

pprint(test_return)
