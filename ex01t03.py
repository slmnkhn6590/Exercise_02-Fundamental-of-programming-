ask = int(input("input a three digit number"))




#getting the last number
last_digit = ask % 10
ask = ask // 10

#getting the middle number
middle_digit = ask % 10
ask = ask // 10

#getting the first number
first_number = ask


#now we will add alll the digits that we have
Sum_of_digits = first_number + middle_digit + last_digit

print(f"The sum of all your numbers is {Sum_of_digits}")