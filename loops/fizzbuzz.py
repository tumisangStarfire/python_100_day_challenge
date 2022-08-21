for n in range(1,100):
    if n % 3 == 0: 
        print(n,'fizz') 
    if n % 5 == 0: 
        print (n,'buzz')
    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuz')