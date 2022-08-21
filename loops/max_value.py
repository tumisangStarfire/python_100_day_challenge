list_of_numbers = [78,65,89,86,55,91,64,89]

max = 0
for n in range(0,len(list_of_numbers)):
    if list_of_numbers[n] > max:
        max = list_of_numbers[n]
print(max)