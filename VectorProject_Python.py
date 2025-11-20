print("Welcome! Type 'start' to start. :)")
begin = input()


if begin == "start":
    print("Pick one of the options below")
    print("For Converting Coordinates to Degrees: Type '1'")
    print("For Resultant Vector using Vector Distance Formulas: Type '2'")
    print("For Resultant Vector using Haversine Formulas: Type '3'")
    print("For exiting the program: Type 'exit'")
    choice = input()
else:
    print("Type 'start' to start")
    begin = input()