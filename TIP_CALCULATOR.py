print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
a = (tip/100)*bill
b= a+bill
people = int(input("How many people to split the bill? "))
c=b//people
final=round(c,3)
print(f"each person amt is :{final}")







