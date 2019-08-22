from sys import argv
#argv stands for argument variable
#read the WYSS section for how to run this
script, first, second, third, fourth = argv

#go to script parameters to run script with arguments or modules, also you dont need to define first arguments
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("This is the last variable:", fourth)
y = input("Was this a good exercise?")
print(y)
print(">>>> argv=", repr(argv))
