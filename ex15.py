from sys import argv

script, filename = argv
#here I am opinging a specified filename
txt = open(filename)

print(f"Here is the name of the file you want to open: {filename}.")
#to actially read the contents I need to use x.read() function
print(f"The contents of the file is: \n{txt.read()}")
print("\n\n")
filename2 = input("What file would you like to open? : ")
txt2 = open(filename2)
print("The contents of the second file is:", end=" ")
print(txt2.read())
print("\n\n")
#this is how you do this in one line, if want to hardcode it in the script
print(open("ex15_sample.txt").read())
#this is how you close a file
txt.close()
