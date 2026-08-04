def is_armstrong(number):
    number_text = str (number)
    digitat_count= len(number_text)
    result = 0
    for digit in number_text:
        result += int(digit) ** digitat_count
    return result == number
print(is_armstrong(153))  # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))  # False
