print(""" Welcome to the Bill Calculator""")

total_amount = int(input("What was the total bill? :"))
tip = int(input("Do  yo want to give tips? if yes, how much do you want to give? :"))
person = int(input("How many people you want to give? :"))

result = (total_amount-tip)/person

print("Each person sould pay : ",result)
