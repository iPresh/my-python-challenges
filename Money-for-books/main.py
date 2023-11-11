number_of_books = int(input("How many books do you want to buy? "))

amount = int(input("How much do you have? "))

amount_required = number_of_books * 20


if amount >= amount_required: 
  print("You have enough money, go for it!")
else:
  actual_amount = amount_required - amount
  
  print("You need $" + str(actual_amount) + " more to buy that number of books")