"""EX01 - Simple Battleship - A cute step toward Battleship."""
__author__ = "730554479"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

hit_var: str = RED_BOX
miss_var: str = WHITE_BOX
blank_box: str = BLUE_BOX

boat_location_str: str = input("Pick a secret boat location between 1 and 4: ")
boat_location: int = int(boat_location_str)
if boat_location > 4:
    exit(print("Error! " + str(boat_location) + "too high!"))
if boat_location < 1:
    exit(print("Error! " + str(boat_location) + "too low!"))

boat_location_str2: str = input("Pick a secret boat location between 1 and 4: ")
boat_location_2: int = int(boat_location_str2)
if boat_location_2 > 4:
    exit(print("Error! " + str(boat_location_2) + "too high!"))
if boat_location_2 < 1:
    exit(print("Error! " + str(boat_location_2) + "too low!"))
if boat_location_2 == boat_location:
    print("Correct! You hit the ship.")
    if boat_location_2 == 1:
        print(hit_var + blank_box + blank_box + blank_box)
    if boat_location_2 == 2:
        print(blank_box + hit_var + blank_box + blank_box)
    if boat_location_2 == 3:
        print(blank_box + blank_box + hit_var + blank_box)
    if boat_location_2 == 4:
        print(blank_box + blank_box + blank_box + hit_var)
else:
    print("Incorrect! You missed the ship.")
    if boat_location_2 == 1:
        print(miss_var + blank_box + blank_box + blank_box)
    if boat_location_2 == 2:
        print(blank_box + miss_var + blank_box + blank_box)
    if boat_location_2 == 3:
        print(blank_box + blank_box + miss_var + blank_box)
    if boat_location_2 == 4:
        print(blank_box + blank_box + blank_box + miss_var)