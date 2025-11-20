def Coord_to_degrees():
    print("You have chosen to convert coordinates to decimal degrees. First we need some information.")
    Lat_deg = float(input("Enter Latitude Degrees: "))
    Lat_min = float(input("Enter Latitude Minutes: "))
    Lat_sec = float(input("Enter Latitude Seconds: "))
    Lon_deg = float(input("Enter Longitude Degrees: "))
    Lon_min = float(input("Enter Longitude Minutes: "))
    Lon_sec = float(input("Enter Longitude Seconds: "))
    Lat_decimal = Lat_deg + (Lat_min / 60) + (Lat_sec / 3600)
    Lon_decimal = Lon_deg + (Lon_min / 60) + (Lon_sec / 3600)
    print(f"Decimal Latitude: {Lat_decimal}")
    print(f"Decimal Longitude: {Lon_decimal}")
    print("You better write those down cuz I'm not saving them for you!")

print("Welcome! Type 'start' to start. :)")
begin = input()

while begin != "start":
    print("Type 'start' to start")
    begin = input()

if begin == "start":
    print("Pick one of the options below:")
    print("For Converting Coordinates to Degrees: Type '1'")
    print("For Resultant Vector using Vector Distance Formulas: Type '2'")
    print("For Resultant Vector using Haversine Formulas: Type '3'")
    print("For exiting the program: Type 'exit'")
    choice = input()

    while choice not in ["1", "2", "3", "exit"]:
        print("Invalid choice. Please pick one of the options below:")
        print("For Converting Coordinates to Degrees: Type '1'")
        print("For Resultant Vector using Vector Distance Formulas: Type '2'")
        print("For Resultant Vector using Haversine Formulas: Type '3'")
        print("For exiting the program: Type 'exit'")
        choice = input()

    if choice == "1":
        Coord_to_degrees()
    elif choice == "2":
        Resultant_Vector_VDF()
    elif choice == "3":
        Resultant_Vector_HF()
    elif choice == "exit":
        print("Exiting the program. Goodbye :)")
    