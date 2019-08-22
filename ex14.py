from sys import argv

script, user_name = argv
#this will go inside the input for a static prompt that we can change in one spot
prompt = 'Type your answer here: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd line to ask you a few questions.")
print(f"Do you like me {user_name}?")
#here I create a variable likes and ask user to input value, the prompt(question) is already defined above in the
#variable called prompt
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")
