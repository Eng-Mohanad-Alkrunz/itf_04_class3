

def roman_to_int(s):

    total = 0
    if "IV" in s:
        total += (s.count("IV") * 4)
        s = s.replace("IV","")
    if "IX":
        total += (s.count("IX" * 9))
        s = s.replace("IX","")

    if "XL" :
        total += (s.count("XL") * 40)
        s = s.replace("XL", "")

    if "XC":
        total += (s.count("XC") * 90)
        s = s.replace("XC", "")

    if "CD":
        total += (s.count("CD") * 400)
        s = s.replace("CD", "")

    if "CM":
        total += (s.count("CM") * 900)
        s = s.replace("CM", "")

    if "I" in s:
        total += (s.count("I") * 1)
        s = s.replace("I","")

    if "V" in s:
        total += (s.count("V") * 5)
        s = s.replace("V", "")

    if "X" in s:
        total += (s.count("X") * 10)
        s = s.replace("X", "")

    if "L" in s:
        total += (s.count("L") * 50)
        s = s.replace("L", "")

    if "C" in s:
        total += (s.count("C") * 100)
        s = s.replace("C", "")

    if "D" in s:
        total += (s.count("D") * 500)
        s = s.replace("D", "")

    if "M" in s:
        total += (s.count("M") * 1000)
        s = s.replace("M", "")


    return total


print(roman_to_int("MCMXCIV"))