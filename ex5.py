name = 'Zed A. Shaw'
age = 33 # not a lie
hight = 190 #in cm
weight = 180 #lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {hight} cm tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exaclt rights
total = age + hight + weight
print(f"If I add {age}, {hight}, and {weight} I get {total}.")

cm = 190
ratio = 0.393701
inches = cm * ratio

print(f"If you are {cm} tall, in inches that would be  {round(inches)}.")
