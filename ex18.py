#this one is like yout scripts with argv
def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")

#ok that args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

#this just makes one argument
def print_one(arg1):
  print(f"arg1: {arg1}")

#this one takes no arguments
def print_name():
  print("I will just print this one here with no variables/ arguments.")

print_two("One", "Two")
print_two_again("one", "two")
print_one("oNE")
print_name()

def multiply(x, y):
  print(x * y)

multiply(2,6)