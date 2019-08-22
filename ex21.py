def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def substract(a, b):
  print(f"SUBSTRACTING {a} - {b}")
  return a - b

def multiply(a,b):
  print(f"MULTIPLY {a} * {b}")
  return a * b

def devide(a, b):
  print(f"DEVIDE {a} / {b}")
  return a / b

print("Let's fo some math with just functions!")

age = add(30, 3)
height = substract(210, 20)
weight = multiply(100, 2)
iq = devide(100, 5)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}!")

#A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, devide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
