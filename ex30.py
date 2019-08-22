people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should walk.")
else:
    print("Do whatever you want!")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("That's a good ratio.")
else:
    print("Thats weird!")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
