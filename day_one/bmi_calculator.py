print("Welcome to the BMI Calculator")
weight = float(input("What is your weight (kg)..? \n"))
height = float(input("What is your height (cm) ..? \n")) 

result = weight / (height /100) **2 

message = f"Your BMI is { round(result)}"
print(message)