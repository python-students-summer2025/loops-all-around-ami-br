
def get_starting_number():
    while True :
        starting_number = (input("How many bottles of beer on the wall? "))
        if starting_number.isnumeric() and int(starting_number) >= 1 :
            starting_number = int(starting_number)
            return starting_number
        else :
            continue

def sing(starting_number) :
    for i in range(starting_number , 0 , -1) :
        if i != 1 :
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            next = i - 1
            if next == 1 :
                print("Take one down, pass it around, 1 bottle of beer on the wall.")
            else :
                print(f"Take one down, pass it around, {next} bottles of beer on the wall. ")
        elif i == 1 :
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
