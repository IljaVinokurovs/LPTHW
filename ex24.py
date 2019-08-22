print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#!!!!!!nice way to define all three varivables as function returnes 3 variables
beans, jars, crates= secret_formula(start_point)

#one way to format a string
print("With a starting point of: {}".format(start_point))

#its purpuse is similar to f"" starting
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do it this way:")
formula= secret_formula(start_point)
#this is an easy way to apply a list to a format starting the * means that we dont kow how many times we need to define the variable
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

print(secret_formula(start_point))
