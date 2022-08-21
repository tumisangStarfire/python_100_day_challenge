#Write your code below this line 👇

def prime_checker(number):
    is_prime = False
    for i in range(2,number):
        if number % i == 0:
            is_prime = True 
    if is_prime: 
        print("It is not a prime number")
    else: 
        print("It is a prime number")
            




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)