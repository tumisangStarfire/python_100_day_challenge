student_heights = input("Please provide student heights ").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
total_length = 0

for heights in student_heights:
    total_height += heights
    total_length = total_length + 1

print(total_height)
print(total_length)
avarage = total_height / total_length
print(avarage)