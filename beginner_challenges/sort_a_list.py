from typing import List
import random
"""Create a function that accepts two parameters, the first will be a list of numbers, the second
Will be a String that can be one of the follwoing: asc,desc and none
"""

def sort_asc(numbers : List[int]):
    new_list =  sorted(numbers)
    return new_list

def sort_desc(numbers : List[int]):
    new_list =  sorted(numbers,reverse=True)
    return new_list

def list_sort(numbers : List[int], sort_type : str):

    if sort_type == "asc":
        my_list = sort_asc(numbers) 
        print(my_list)
    elif sort_type == "desc" : 
        my_list = sort_desc(numbers)
        print(my_list)
    else: 
        print(numbers) 


my_numbers = []
for x in range(1,101):
    my_numbers.append(x)  

random.shuffle(my_numbers)

ask_sort_type = input("How do you want to sort he numbers: [asc,desc,none] \n").lower()

list_sort(my_numbers,ask_sort_type)