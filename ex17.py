from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long.")

print(f"does the output file exist {exists(to_file)}")
#print("Ready, hit RETURN to continue. CTRL + C to abort.")
#input()

out_file = open(to_file, 'a+')
out_file.write(indata)
#as the reading/ writing is the same as tape, we first need to roll back the tape to be able to read the file from beginning
out_file.seek(0)
new_text = out_file.read()
print(new_text)
#this i sto see that type if variable is in_file
print(">>>> in_file= ", repr(in_file))

print("All done!")

out_file.close()
in_file.close()
#print(open(to_file).read())




