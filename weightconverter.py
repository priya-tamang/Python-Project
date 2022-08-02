print("Welcome to the Weight Converter!!!")

weight = int(input("Enter your weight : "))
choice = input("(L)bs or (K)kg : ")

if choice.upper() == "L":
    converter = weight * 0.453592
    print("Converted",weight,"lbs to ", converter, "kg")
elif choice.upper() == "K":
    converter = weight * 2.20462
    print("Converted",weight,"kg to ", converter, "lbs")
else:
    print("Please choice between L and K")
