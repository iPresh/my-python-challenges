x = int(input("Enter a number: "))

if x % 3 == 0 and x % 5 == 0:
    print("your mumber is a multiple of both 3 and 5")

elif x % 3 == 0:
    print("your number is a multiple of 3")

elif x % 5 == 0:
    print("your number is a multiple of 5")

else:
    print(x)
