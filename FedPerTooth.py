feed_rate = float(input("What is your feed rate?"))
spindle_speed = float(input("What is your spindle speed?"))
Num_teeth = float(input("What is the number of flutes/teeth on your cutting tool?"))

fpt = feed_rate / (spindle_speed * Num_teeth)

print("Your current feed per tooth is " + str(fpt) + " inches.")