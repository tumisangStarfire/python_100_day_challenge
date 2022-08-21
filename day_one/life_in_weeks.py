title ="Let's calculate how long you have to live"
print(title)
age = int(input("What is your current age..? \n"))

average_death_age = 90
weeks = 52
days = 365 
months = 12


years_left = 90 - age

months_left = years_left * months

weeks_left = years_left * weeks 

days_left = years_left * days 

message = f"You have  { months_left } months, { weeks_left } weeks and { days_left} days remaining. "
print(message)



