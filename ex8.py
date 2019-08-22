#here we define that the string x will have 4 "replacement fields". That means that when we use str.format() method we can replace/ define these replacement fields the way we want
x = "{} {} {} {}"
#here we replace the fields with integers
print(x.format(1, 2, 3, 4))
#here we replace them with other strings, note that even though we definced 5 fields they are not all visible as we have only four replacement fields in string x
print(x.format("one", "two", "three", "four", "five"))
#we can also define them as booleans
print(x.format(True, False, False, True))
#you can also replace the replacement fiel with itself
print(x.format(x,x,x,x))
#here I replace it with new line and longer strings. end = "" cannot be defined inside this method, it can be defined after that. 
print(x.format(
  "This is a test\n",
  "I want to see what is does \n",
  "Maybe it does\n",
  "Maybe it doesn't"
))
#just showing off that I know how to count the length of the string
print(len(x))