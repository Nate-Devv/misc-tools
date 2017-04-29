#!/usr/bin/env python3
DIG_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def find_validator(dig_string, old_base):
    dig_sum = sum_digits(dig_string, old_base)
    return dig_sum[-1:].upper()
    
def sum_digits(dig_string, old_base):
    int_sum = 0
    while dig_string:
        int_sum += int(dig_string[:1], base=old_base)
        dig_string = dig_string[1:]
    dig_sum = unint(int_sum, old_base)
    return dig_sum
    
def unint(int_val, new_base):
    if int_val < new_base:
        return DIG_CHARS[int_val]
    else:
        return unint(int_val//new_base, new_base) + DIG_CHARS[int_val%new_base]
    
if __name__ == "__main__":
    print("Welcome to find_validator.py!\nPlease enter an invalid base to quit" +
        "\nor q at the validator to choose a new base.")
    work_base = 1
    while 0 < work_base < 35:
        dig_string = ""
        work_base = int(input("\nEnter the base of the number(s) you would like to validate: "))
        if work_base <= 0 or work_base > 35:
            break
        while dig_string.lower() != "q":
            dig_string = input("Enter a number to validate: ")
            if dig_string.lower() == "q":
                break
            print("The validator is:", find_validator(dig_string, work_base))
