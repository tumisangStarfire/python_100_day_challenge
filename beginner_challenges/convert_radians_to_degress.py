#Write a function that accepts one numeric parameter. This parameter will be the measure of an angle in radians

import math


def convert_deg_rad():
    num = int(input("Input Degree: "))
    radian_number = math.radians(num)
    print(radian_number) 

convert_deg_rad()