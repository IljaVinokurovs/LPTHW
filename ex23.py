# we are actually importing the whole sys module
import sys
# here we say that we want to use argv out of the sys module and we will need 3 variables script name that we want to run, input_encoding = the encoding type we want and what should the script do with the errors
script, input_encoding, error = sys.argv

#main function can be used only within this file and not when the file is imported
def main(langugage_file, encoding, errors):
    #reading the next line
    line = langugage_file.readline()
    #checking if line exists
    if line:
        #calling the other function print_line
        print_line(line, encoding, errors)
        #I think this is kind of a while loop that executes the main function within itself while there are any lines left
        return main(langugage_file, encoding, errors)

def print_line(line, encoding, errors):
    #strip() removes leading and trailing characters like spaces can be also used to remove specific characters if parameter is defined strip("a") will remove all a characters
    next_lang = line.strip()
    #encode(encoxing, errors) is used to encode the strings to the specific encoding to make them bytes, usuelly it is UTF - 8 or ACSI, it takes two parameters, one being to what encoding should the string be converted and second is what to do with errors
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #decode is used to decode the encoded string to the original state, it uses two paramenters: the encoding version of the string and how to deal with the errors
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    #comparing of the two strings
    print(raw_bytes, "<====>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
