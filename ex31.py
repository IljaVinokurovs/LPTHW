print("""You enter a dark room with two doors.
Do you go through door #1 or door 2#?""")

door = input(">")

def game(door):
    # as input is a string we have to compare the variable with string
    if door == "1":
        print("There's a giant bear eating a cheese cake.")
        print("What do you do?")
        print("1. Take the cake.")
        print("2. Screem at the bear.")

        bear = input(">")

        if bear =="1":
            print("The bear eats your face off. Good job!")
        elif bear =="2":
            print("The bear eats your legs off. Good job!")
        else:
            print(f"Well, doing {bear} is probably better.\nBear Runs away.")
    elif door == "2":
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1. Blueberries.")
        print("2. Yellow jacket clothspins.")
        print("3. Understanding revolvers yelling melodies.")

        insanity = input(">")

        if insanity  == "1" or insanity == "2":
            print("Your body survives powered by a mind og jello.")
            print("Good job!")
        else:
            print("The insanity rots your eyes into a pool of muck.\nGood job!")
    else:
        door = input("Invalid input, please choose values \"1\" or \"2\"\n>")
        game(door)
# first you need to define the function and only yhen you can run it
game(door)
