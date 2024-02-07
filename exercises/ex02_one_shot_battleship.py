"""One Shot Battleship"""
__author__ = "730554479"

# Step 1: Establishing a secret and promoting for a guess
grid_area: int = 4
secret_row: int = 3
secret_column: int= 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Step 2: Guessing a row
row_safe = False
while not row_safe:
    row_guess_str: str = input("Guess a row: ")
    row_guess: int = int(row_guess_str)
    if 1 <= row_guess <= grid_area:
        row_safe = True
    else:
        valid_input = False
        while not valid_input:
            row_guess = int(input("The gris is only 4 by 4. Try again: "))
            if 1 <= row_guess <= grid_area:
                valid_input = True
                row_safe = True
            else:
                valid_input = False

# Step 3: Guessing a column
column_safe = False
while not column_safe:
    column_guess_str: str = input("Guess a column: ")
    column_guess: int = int(column_guess_str)
    if 1 <= column_guess <= grid_area:
        column_safe = True
    else:
        valid_input2 = False
        while not valid_input2:
            column_guess = int(input("The grid is only 4 by 4. Try again: "))
            if 1 <= column_guess <= grid_area:
                valid_input2 = True
                column_safe = True
            else:
                valid_input2 = False

# Step 4: Emojis for correct guesses
if column_guess == secret_column and row_guess == secret_row:
    print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
    print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
else:
    guess_miss: str = WHITE_BOX
    guess_hit: str = RED_BOX
    open_box: str = BLUE_BOX
    row_count: int = 1
    while row_count <= grid_area:
        row_str: str = ""
        col_count: int = 1
        if row_count == row_guess:
            while col_count <= grid_area:
                if col_count == column_guess:
                    row_str += guess_miss
                else:
                    row_str += open_box
                col_count += 1
        else:
            while col_count <= grid_area:
                row_str += open_box
                col_count += 1
        print(row_str)
        row_count += 1

# Step 5: Guess repsoneses
if column_guess == secret_column and row_guess == secret_row:
    print("Hit!")
elif column_guess == secret_column:
    print("Close! Correct column, wrong row.")
elif row_guess == secret_row:
    print("CLose! Correct row, wrong column.")
else:
    print("Miss!")
            