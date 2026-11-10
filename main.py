name = input("What is your name adventurer? ")

print(f"Companion: Welcome to Gielinor, {name}!")


drop = input("Did you just recieve a rare drop? ").lower()

if drop == "yes":
    print("Companion: Congratulations! Thats a huge drop!")
elif drop == "no":
    print("Companion: Keep grinding! Your drop is coming!")
else:
    input('Please answer with "yes" or "no"')
