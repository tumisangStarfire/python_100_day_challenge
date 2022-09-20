"""  Write down the number.
    Divide it by 2 and note the remainder.
    Divide the quotient obtained by 2 and note the remainder.
    Repeat the same process till we get 0 as the quotient.
    Write the values of all the remainders starting from the bottom to the top."""


def convert_decimal_binary(num : int):

    if num > 1:
        convert_decimal_binary(num // 2)

    print(num % 2)

decimal_number = int(input("Provide digit to be converted: "))

convert_decimal_binary(decimal_number)