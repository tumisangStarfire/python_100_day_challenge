#name = input("what is your name..?")
#nameLength = len(name) 
#print(type(name))  

#write a program that adds digits in a 2 digit number 

digit_number = input("Please enter 2 digit number \n") 

if(len(digit_number) < 2): 
  first_num = digit_number[0]
  second_num = digit_number[1]

  result = int(first_num) + int(second_num) 
  print(result)
else : 
    print("Not a two digit number")




