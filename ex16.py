from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL + C.")
print("If you are OK to do that hit Enter")

input("?")

print("Opening file....")
#in this case we dont really need to use truncate() function as w in the open() parameters already does it by default
#if we wanted to add the info and not delete the previous contents we should use 'a'. The 'a' stands for append
target = open(filename, 'w')

print(""""Truncating (deleting the contents) the file. Goodbye!""")
target.truncate()

print("Now let's add some text to the file.")
line1 = input("What should be in the first line: ")
line2 = input("Second line: ")
line3 = input("Third line: ")

print("These values will be written to the file now.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
escape = "\n"
target.write(line1 + escape + line2 + escape + line3 + escape)

print("Finally we Save and Close he file.")
target.close()

print("\n\nLet's open and see whats in the file now.")
#in thi scase if I dont assing variable to the openging of the file it is opened read and closed at the same instance,
#so no need to close the file - it is already closed
print(open(filename).read())
print(open(filename).readlines()[2])
#filename.close()
