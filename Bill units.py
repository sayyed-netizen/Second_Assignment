units = int(input(" Please enter Number of Units you Consumed : "))

if(units <= 50):
    amount = units * 3
elif(units <=100 ):
    amount = units * 6
elif(units <= 150):
    amount = units * 9
elif(units <= 200):
    amount = units * 12
else:
    amount = units * 15
total = amount 
print("\nElectricity Bill = %.2f"  %total)