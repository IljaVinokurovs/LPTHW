#here we define the value for variable, it will get funny later
types_of_people = 10
#we print a string that contains the above variable
x= f"There are {types_of_people} types of people."

#we define two variables and use them inside the string
binary = "binary"
do_not = "don't"
y = f"Those who now {binary} and those who {do_not}."

#we print these variables one after another
print(x)
print(y)

# we pring the string variables inside a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

#we define if the joke was funny
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#we print the conclusion ( inside )
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
