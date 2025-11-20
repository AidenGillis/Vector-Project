import math

def Coord_to_degrees():
    print("You have chosen to convert coordinates to decimal degrees. First we need some information.")
    Lat_deg = float(input("Enter Latitude Degrees: "))
    Lat_min = float(input("Enter Latitude Minutes: "))
    Lat_sec = float(input("Enter Latitude Seconds: "))

    Lat_hem = input("Enter Hemisphere")
    while Lat_hem not in ("N", "W", "S", "E"):
         print("Invalid Hemisphere")
    if Lat_hem == "N" or input() == "W":
            hem_val = 1
    elif  Lat_hem == "S" or input() == "E":
            hem_val = -1

    Lon_deg = float(input("Enter Longitude Degrees: "))
    Lon_min = float(input("Enter Longitude Minutes: "))
    Lon_sec = float(input("Enter Longitude Seconds: "))

    Lon_hem = input("Enter Hemisphere")
    while Lon_hem not in ("N", "W", "S", "E"):
         print("Invalid Hemisphere")
    if Lon_hem == "N" or input() == "W":
            hem_val = 1
    elif  Lon_hem == "S" or input() == "E":
            hem_val = -1

    Lat_decimal = (Lat_deg + (Lat_min / 60) + (Lat_sec / 3600)) * Lat_hem
    Lon_decimal = Lon_deg + (Lon_min / 60) + (Lon_sec / 3600) * Lon_hem
    print(f"Decimal Latitude: {Lat_decimal}")
    print(f"Decimal Longitude: {Lon_decimal}")
    print("You better write those down cuz I'm not saving them for you!")

def Resultant_Vector_VDF():
    print("You have chosen to calculate the Resultant Vector using Vector Distance Formulas. First we need some information.")
    Lat1 = float(input("Enter Latitude 1 in Decimal Degrees: "))
    Lon1 = float(input("Enter Longitude 1 in Decimal Degrees: "))
    Lat2 = float(input("Enter Latitude 2 in Decimal Degrees: "))
    Lon2 = float(input("Enter Longitude 2 in Decimal Degrees: "))   

    X1 = Lon1 * (40000 / 360)
    Y1 = Lat1 * (40000 / 360)
    X2 = Lon2 * (40000 / 360)
    Y2 = Lat2 * (40000 / 360)

    X_vector = X2 - X1
    Y_vector = Y2 - Y1

    Distance = (X_vector**2 + Y_vector**2)**0.5
    Angle_rad = math.atan2(Y_vector, X_vector)
    Angle_deg = math.degrees(Angle_rad)
    print(f"i = {X_vector} km j = {Y_vector} km")
    print(f"Resultant Distance: {Distance} km")
    print(f"Resultant Angle (radians): {Angle_rad}")
    print(f"Resultant Angle (degrees): {Angle_deg}")

def Resultant_Vector_HF():
    print("You have chosen to calculate the Resultant Vector using Haversine Formulas. First we need some information.")
    Lat1 = float(input("Enter Latitude 1 in Decimal Degrees: "))
    Lon1 = float(input("Enter Longitude 1 in Decimal Degrees: "))
    Lat2 = float(input("Enter Latitude 2 in Decimal Degrees: "))
    Lon2 = float(input("Enter Longitude 2 in Decimal Degrees: "))   

    R = 6371  # Radius of the Earth in kilometers
    dLat = math.radians(Lat2 - Lat1)
    dLon = math.radians(Lon2 - Lon1)
    a = (math.sin(dLat / 2) ** 2 + 
         math.cos(math.radians(Lat1)) * math.cos(math.radians(Lat2)) * 
         math.sin(dLon / 2) ** 2)
    Distance = 2 * 6371 * (math.asin(math.sqrt(a)))

    X_vector = (Lon2 - Lon1) * (40000 / 360)
    Y_vector = (Lat2 - Lat1) * (40000 / 360)

    Angle_rad = math.atan2(Y_vector, X_vector)
    Angle_deg = math.degrees(Angle_rad)
    print(f"Resultant Distance: {Distance} km")
    print(f"Resultant Angle (radians): {Angle_rad}")
    print(f"Resultant Angle (degrees): {Angle_deg}")

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

    while choice not in ["1", "2", "3", "exit", "goblin"]:
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
    elif choice == "goblin":
            print("           ⣠⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("         ⣠⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("   ⠀⠀⠀⠀⠀⢀⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀")
            print(" ⠢⣤⣀⡀⠀⠀⠀⢿⣧⣄⡉⠻⢿⣿⣿⡿⠟⢉⣠⣼⡿⠀⠀⠀⠀⣀⣤⠔")
            print("  ⠈⢻⣿⣶⠀⣷⠀⠉⠛⠿⠶⡴⢿⡿⢦⠶⠿⠛⠉⠀⣾⠀⣶⣿⡟⠁⠀")
            print("⠀⠀⠀⠀⠻⣿⡆⠘⡇⠘⠷⠠⠦⠀⣾⣷⠀⠴⠄⠾⠃⢸⠃⢰⣿⠟⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠋⢠⣾⣥⣴⣶⣶⣆⠘⣿⣿⠃⣰⣶⣶⣦⣬⣷⡄⠙⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⢋⠛⠻⠿⣿⠟⢹⣆⠸⠇⣰⡏⠻⣿⠿⠟⠛⡙⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠈⢧⡀⠠⠄⠀⠈⠛⠀⠀⠛⠁⠀⠠⠄⢀⡼⠁⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠃⠀⣿⡆⢰⣿⠀⠘⢀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠘⠇⠸⠃⢀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⣄⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")


    