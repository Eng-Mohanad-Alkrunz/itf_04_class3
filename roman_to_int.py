
def roman_to_int(roman_number:str):
    total = 0

    if "IV" in roman_number:
        total += (roman_number.count("IV") * 4)
        roman_number = roman_number.replace("IV","")
        
    if "IX" in roman_number:
        total += (roman_number.count("IX") * 9)
        roman_number = roman_number.replace("IX", "")
        
    if "XL" in roman_number:
        total += (roman_number.count("XL") * 40)
        roman_number = roman_number.replace("XL", "")
        
    if "XC" in roman_number:
        total += (roman_number.count("XC") * 90)
        roman_number = roman_number.replace("XC", "")

    if "CD" in roman_number:
        total += (roman_number.count("CD") * 400)
        roman_number = roman_number.replace("CD", "")

    if "CM" in roman_number:
        total += (roman_number.count("CM") * 900)
        roman_number = roman_number.replace("CM", "")

    print(roman_number)


    if "I" in roman_number:
        total += (roman_number.count("I") * 1)

    if "V" in roman_number:
        total += (roman_number.count("V") * 5)

    if "X" in roman_number:
        total += (roman_number.count("X") * 10)

    if "L" in roman_number:
        total += (roman_number.count("L") * 50)

    if "C" in roman_number:
        total += (roman_number.count("C") * 100)

    if "D" in roman_number:
        total += (roman_number.count("D") * 500)

    if "M" in roman_number:
        total += (roman_number.count("M") * 1000)

    return total



def get_value(char):

    if char == "I":
        return 1
    if char == "V":
        return 5
    if char == "X":
        return 10
    if char == "L":
        return 50
    if char == "C":
        return 100
    if char == "D":
        return  500
    if char == "M":
        return 1000

def roman_to_int_for_loop(roman_number:str):
    roman_number = roman_number[::-1]
    last_added = 0
    total = 0
    for char in roman_number:
        if last_added > get_value(char) :
            total -= get_value(char)
        else:
            total += get_value(char)
        last_added = get_value(char)

    return total



x = input("Enter Roman Number")
print(roman_to_int_for_loop(x))

