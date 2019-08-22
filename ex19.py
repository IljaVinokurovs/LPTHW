def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} ceeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers")
  print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
cheese = 10
crackers = 20

cheese_and_crackers(cheese, crackers)

print("We can do math insude brackets too:")
cheese_and_crackers(20 + 10, 30 + 20)

print("And we can combine the two, variables and math:")
cheese_and_crackers(10 + cheese, 30 + crackers)

print("And now we try with user input:")
cheese_and_crackers(input("How many cheeses you have?\n"), input("How many crackers you have?\n"))

print("Why not function inside a function, with return function")
def cnc():
  cheese = 123
  return cheese
cheese_and_crackers(cnc(), 321)

