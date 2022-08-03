from datetime import date
age = int(input("Enter your age : "))
today = date.today()
result = today.year - age
print("Your Birthday Year was : ",result)

birthday = int(input("Enter your birthday date year :"))
today = date.today()
age = today.year - birthday
print(age)