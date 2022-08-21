import re
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message 

def caesar(start_text, shift_amount,cipher_direction):
    end_text = ""  
    alphabet_only = " ".join(re.findall("[a-zA-Z]+", start_text))
    
    if cipher_direction == "decode":
        shift_amount *= -1 
    for character in start_text:  
        if character in alphabet:
            index_of_letter = alphabet.index(character)
            new_letter_position = index_of_letter + shift_amount; 
            end_text += alphabet[new_letter_position]  
        else: 
            end_text += character
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue =  True

while should_continue : 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%). 
    if shift > len(alphabet):
        shift = shift % len(alphabet)

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction) 
    promt_user = input("Type 'yes' if you want to go again. Otherwise Type 'no. \n").lower()
    if promt_user == "no": 
        should_continue = False 
        print("Good Bye")