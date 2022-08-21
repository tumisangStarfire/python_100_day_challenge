title =  "Welcome to the tip calculator."
bill_amount = float(input("What was the total bill..? \n"))
tip_percentage = float(input("What percentage tip would you like to tip..? \n"))
split_count = int(input("How many people will split the bill..? \n"))

tip_amount = bill_amount * tip_percentage / 100 

# Bill each_person_has_to_pay
total_amount = (bill_amount + tip_amount ) / split_count
print(total_amount)