print("calculate n raise to the power of n ")
print("caclulate the sum of arithmetic numbers ")
choose_1 = input("Choose one of these (1 or 2) ")
choose_number = int(input("write a number you want to do maths with "))

#make a boolean which will look and take a decision
if choose_1 == "1":
    print( "this is the power of numbers you want ",choose_number ** choose_number)
elif choose_1 == "2":
    print( "this is the sum of arithmetic numbers you want", choose_number * ((1 + choose_number) / 2))
