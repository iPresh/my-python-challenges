NAIRA_PER_DOLLAR = 410.59 

your_amount = float(input("How much USD do you have?"))
your_value = (your_amount * NAIRA_PER_DOLLAR)
print(f"{your_value:.2f} NGN")