amount = int(input("Enter Purchases amount: "))
if(amount>100):
    if amount<=1000:
       disc = amount*0
    elif amount<=2000:
        disc=amount*0.10
    elif amount<=3000:
        disc=0.20 * amount
    else:
         disc=0.25 * amount

    print("Discount : ",disc)
    print("Total_bill  : ",amount-disc)
else:
    print("Invalid Amount")
