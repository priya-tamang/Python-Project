print("""Welcome to Our Name Generator!!!""")

name = input("Enter the your name :")
othername = input("Enter the other loveone name :")

result =  othername[:3] + name[-2:] 
print("The name generate for your is : ",result)
