print("welcome to the world of guessing")
number_01 = int(input("Type the first number plz: "))
number_02 = int(input("Type the second number plz: "))

print(f"the range is from  {number_01} to {number_02}.\n")

guess_number = int(input("Type a number between the Range: "))

if guess_number > number_02 or guess_number < number_01:
    print("The number is not in the specified space")
else:
    if guess_number > number_01 or guess_number < number_02:
        print("the number is inside the specified zone")
