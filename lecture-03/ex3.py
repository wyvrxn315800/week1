inchar = input("Input a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You input an uppercase letter.", inchar) 
elif inchar>= 'a' and inchar <= 'z':
    print("You input a lowercase letter.", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input Number.", inchar)
else:
    print("It's not a letter or number.", inchar)